# Supress warnings
from typing import Tuple
import warnings; warnings.filterwarnings('ignore')

# Data and math operations
import re
import numpy as np
import pandas as pd

# Compute DTW distance
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

# Image processing
import cv2
import mediapipe as mp

# Image visualizations
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import plotly.express as px
import plotly.graph_objects as go

# Read mediapipe labels
from google.protobuf.json_format import MessageToDict

# OS functions
import os
import time

# Progress bar
from tqdm.auto import tqdm

# Mediapipe instances
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


# Image drawing colors
BLUE   = '#00fafd'    # rgb(0,250,253)
YELLOW = '#f5b324'    # rgb(245,179,36)

# Landmark styles
HAND_CONNECTIONS = mp_hands.HAND_CONNECTIONS
# DEFAULT_LANDMARK_POINTS = mp_drawing_styles.get_default_hand_landmarks_style()
# DEFAULT_LANDMARK_CONNECTIONS = mp_drawing_styles.get_default_hand_connections_style()
LANDMARK_DRAWING_SPECS = mp_drawing.DrawingSpec(
        color=(36, 179, 245), 
        thickness=1, 
        circle_radius=4
)
CONNECTIONS_DRAWING_SPECS=mp_drawing.DrawingSpec(
        color=(253, 250, 0), 
        thickness=2, 
        circle_radius=5
)
FONT_ARGS = {
    'fontFace'  : cv2.FONT_HERSHEY_SIMPLEX,
    'fontScale' : 1,
    'color'     : (253, 250, 0),
    'thickness' : 2,
    'lineType'  : cv2.LINE_AA
}
LETTER_ARGS = {
    'fontFace'  : cv2.FONT_HERSHEY_SIMPLEX,
    'fontScale' : 3,
    'color'     : (0, 250, 253),
    'thickness' : 2,
    'lineType'  : cv2.LINE_AA
}



REFERENCE_SIGNS = 'LOAD PICKLE'

'''
process_results
|
|--get_hand_coordinates
|
|--create_hand_gesture
|   |
|   |--get_landmark_angles
|      |
|      |--calculate_3D_angle
|-> hand_gesture_arrays
'''

# Create coordinates dataframes for each landmarks results
def get_hand_coordinates(results_list, verbose=False) -> Tuple[list,list]:
    # Store mapping for each hand
    left_hand_list = []
    right_hand_list = []

    # Iterate over results
    for frame_number, results in enumerate(results_list):
        # Check if any hand was detected
        if results.multi_hand_landmarks:

            # Iterate over hands (right or left)
            for hand_number, hand_landmark in enumerate(results.multi_hand_landmarks):

                # Extract hand orientation str
                hand_label = MessageToDict(results.multi_handedness[hand_number])
                hand_label = hand_label['classification'][0]['label']

                # Create dataframe to store node coordinates
                hand_map_df = pd.DataFrame()

                # Iterate over landmarks of current hand
                for node_id, landmark in enumerate(hand_landmark.landmark):
                    # Get coordinates and labels
                    _row = pd.DataFrame(
                            data={
                                'x'          : landmark.x,
                                'y'          : landmark.y,
                                'z'          : landmark.z,
                            }, index=[node_id])
                    # Append row to dataframe
                    hand_map_df = pd.concat([hand_map_df, _row])

                # Add mapping for into the corresponding hand
                if hand_label == 'Left':
                    left_hand_list.append(hand_map_df)
                elif hand_label == 'Right':
                    right_hand_list.append(hand_map_df)
        #print(f'Frame {frame_number}, Left={len(left_hand_list)}, Right={len(right_hand_list)}')
    if verbose:
        print(f'Frames detected:\nLeft hand:{len(left_hand_list)}, Right hand:{len(right_hand_list)}')
    
    return left_hand_list, right_hand_list

# Calculate the angle between two 3D points
def calculate_3D_angle(u:np.ndarray, v:np.ndarray) -> float:
    '''
    Calculate the angle between 2 points with (x,y,z) coordinates
    ang = acos( (x1*x2 + y1*y2 + z1*z2) / sqrt( (x1*x1 + y1*y1 + z1*z1)*(x2*x2+y2*y2+z2*z2) ) )
    Return: angle in radians
    '''
    # Calculate cross product
    dot_product = np.dot(u, v)
    # Calculate vector norm
    norm = np.linalg.norm(u) * np.linalg.norm(v)
    # Calculate angle in radians
    angle = np.arccos(dot_product / norm)
    if np.isnan(angle) or np.isinf(angle):
        angle=0
    return angle

# Obtain all angles ffrom a hand landmarks
def get_landmark_angles(landmark_df:pd.DataFrame) -> np.ndarray:
    '''
    Dataframe format:
    x	y	z
    0.183309	0.889030	9.577590e-09
    Return: list of shape 441
    '''
    landmark_angles = []
    # Multiply every node with each other, 21 connections * 21 = 441 angles
    for i in range(landmark_df.shape[0]):
        for j in range(landmark_df.shape[0]):
            # Calculate angle between X and Y coordinates
            _node_1 = landmark_df.iloc[i,[1,2]]
            _node_2 = landmark_df.iloc[j,[1,2]]
            landmark_angles.append(calculate_3D_angle(_node_1, _node_2))
    return landmark_angles

# Generate hand gesture array
def create_hand_gesture(frame_list:list, connections=441, hand_label='') -> np.ndarray:
    '''
    frame_list: list of pd.Dataframe containing each frame landmark coordinates
    connections(int): number of connected nodes
    Return: array of shape(frame_number, connections) to compute distance
    '''
    # Create empt array
    frame_size = len(frame_list)
    gesture_array = np.zeros([frame_size, connections])
    # Compute angles for each landmark
    for frame_index, landmark in tqdm(enumerate(frame_list), 
                                      desc=f'Calculating {hand_label} landmark angles',
                                      total=frame_size,
                                      colour='#00fafd'):
        gesture_array[frame_index] = get_landmark_angles(landmark)        
    return gesture_array

# Process results
def process_results(landmarks_results, verbose=False):
    left_hand_gesture=None
    right_hand_list=None
    # Process results
    left_hand_list, right_hand_list = get_hand_coordinates(landmarks_results, verbose)
    # Create gesture arrays
    if len(left_hand_list)>0:
        left_hand_gesture  = create_hand_gesture(left_hand_list, hand_label='left')
    if len(right_hand_list)>0:
        right_hand_gesture  = create_hand_gesture(right_hand_list, hand_label='right')
    
    return left_hand_gesture, right_hand_gesture

# Compare recorded sign with references
def make_prediction(hand_gesture:np.ndarray, verbose=False) -> str:
	predictions = {}
	for letter, reference in REFERENCE_SIGNS.items():
		dist, _ = fastdtw(hand_gesture, reference, dist=euclidean)
		if verbose:
			print(f'Distance from sign {letter}: {dist:.2f}')
		predictions[letter] = dist
	# Get the lowest distance
	predicted_sign = min(predictions, key=predictions.get)
	return predicted_sign

