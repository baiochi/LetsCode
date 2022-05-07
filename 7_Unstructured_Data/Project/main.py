# Supress warnings
from typing import Tuple
import warnings; warnings.filterwarnings('ignore')

# Image processing
import cv2
import mediapipe as mp

# Image visualizations
import matplotlib.pyplot as plt

# OS functions
import os
import time

# Custom functions
from functions import process_results, make_prediction, FONT_ARGS, LETTER_ARGS

# Define recording lenght
FRAME_SIZE = 20

# Create Mediapipe Hands model
hands = mp.solutions.hands.Hands(model_complexity=0, 
								min_detection_confidence=0.5, 
								min_tracking_confidence=0.9)
# Settings
frame_list = []		# store recorded frames
results_list = []	# store hands processing results
recording = False

# Start webcam
cam = cv2.VideoCapture(0)
while cam.isOpened():

	# Read frame
	_, image = cam.read()

	# Improve performance = False
	image.flags.writeable = False

	# Start "recording"
	if recording:
		# Recording flag
		cv2.putText(cv2.flip(image, 1), 'Recording...', (30, 50), **FONT_ARGS)

		# Append frame converted to RGB
		if len(frame_list) < FRAME_SIZE:
			frame_list.append(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
		# Stop record and predict sign
		else:
			# Process results with mediapipe Hands
			results_list = [hands.process(frame) for frame in frame_list]
			left_hand_gesture, _ = process_results(results_list, True)
			predicted_sign = make_prediction(left_hand_gesture)

			# Draw Sign in image
			cv2.putText(cv2.flip(image, 1), predicted_sign, (30, 50), **FONT_ARGS)
			print(f'Predicted Sign: {predicted_sign}')
			print('Recording stopped.')
			# time.sleep(0)
			recording = False

	# Show image
	cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
	# Key control
	pressed_key = cv2.waitKey(1) & 0xFF
	# Start recording
	if pressed_key == ord('r'):
		recording = True
	# Close webcam
	elif pressed_key == ord('q'):
		recording = False
		break

# Release video capture
cam.release()
# Memory dump
cv2.destroyAllWindows()
# fix window not closing bug on macOS 10.15
cv2.waitKey(1)