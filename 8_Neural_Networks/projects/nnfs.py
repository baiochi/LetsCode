__version__ = '0.0.1'

# Math operations and data manipulation
import numpy as np
import pandas as pd
# Data Visualization
import matplotlib.pyplot as plt
# Progress bar
from tqdm.auto import tqdm

# Sigmoid function
sigmoid   = lambda x : 1 / (1 + np.exp(-x))
# Derivative of sigmoid function
sigmoid_d = lambda x : x * (1 - x)
# Softmax
def softmax(x):
    e_x = np.exp(x - np.max(x, keepdims=True))
    return e_x / np.sum(e_x, keepdims=True)

# Preprocess data
def preprocess(X, y, X_eval, n_labels):
    X /= X.max(axis=1).max()                # Normalize train values
    X_eval /= X_eval.max(axis=1).max()      # Normalize eval values
    y_enc = np.zeros((y.size, n_labels))    # One hot encode labels
    y_enc[np.arange(y.size), y] = 1
    return X, y_enc, X_eval

# Init weights/biases
def init_wb(grid, random_state):
    np.random.seed(random_state)                      
    w1 = np.random.uniform(-0.5, 0.5, [grid[1], grid[0]])
    w2 = np.random.uniform(-0.5, 0.5, [grid[2], grid[1]])
    b1 = np.zeros([grid[1], 1])         
    b2 = np.zeros([grid[2], 1])
    return w1, w2, b1, b2

# Fit model
def fit(X, y, w1, b1, w2, b2, af1, af2, af1_d, epochs, alpha):
    for epoch in range(epochs):     
        acc = 0                # Init/reset accuracy score
        pbar = tqdm(          
            zip(X, y), 
            total=n_samples, 
            colour='#1696d2')    
        for sample, label in pbar:
            a1 = sample.reshape(-1,1)          # Reshape features/label to fit layer shape
            y_true = label.reshape(-1,1)    
            a2 = af1(w1 @ a1 + b1)             # Foward Input -> Hidden layer
            a3 = af2(w2 @ a2 + b2)             # Foward Hidden -> Output layer
            a2_d =  a3 - y_true                # Backward Ouput -> Hidden layer                  
            w2 += -alpha * a2_d @ a2.T         # Update a2 weights/biases
            b2 += -alpha * a2_d
            a1_d   =  w2.T @ a2_d * af1_d(a2) # Backward Hidden -> Input layer   
            w1 += -alpha * a1_d @ a1.T         # Update a1 weights/biases
            b1 += -alpha * a1_d
            # Update accuracy score
            acc += int(np.argmax(a3) == np.argmax(y_true))
            pbar.set_description(f'Epoch {epoch+1}, Acc: {acc/n_samples*100:.2f}')
        pbar.close()
    return w1, w2, b1, b2

# Make predictions
def predict(X_eval, w1, b1, w2, b2, af1, af2, image_shape=None):
    eval_samples = X_eval.shape[0]
    y_pred = np.zeros([10,1])             
    for a1 in tqdm(X_eval, total=eval_samples, desc='Making predictions', colour='#fdbf11'):
        a1.shape += (1,)
        a2 = af1(w1 @ a1 + b1)            
        a3 = af2(w2 @ a2 + b2)
        y_pred  = np.append(y_pred, a3, axis=1)
    y_pred = y_pred.T[1:]
    
    if image_shape:
        # Plot sample predictions
        sample_pred = np.argmax(y_pred, axis=1)[:10]
        fig, ax = plt.subplots(1,10, figsize=(18,6))
        fig.suptitle('Sample predictions', size=18, x=0.19, y=0.725)
        for i in range(10): 
            ax[i].imshow(X_eval[i].reshape(image_shape[0], image_shape[1]))
            ax[i].set_xticks([]); ax[i].set_yticks([])
            ax[i].set_title(f'{sample_pred[i]}', size=18)
            ax[i].grid(False)
            
    return y_pred
# Main function
def neural_network(X:np.ndarray, y:np.ndarray, X_eval:np.ndarray, hl_size=16, 
                   af1=sigmoid, af2=softmax, af1_d=sigmoid_d, 
                   epochs=3, alpha=0.01, random_state=None):
    '''
    X : train data  
    y : label data  
    X_eval : evaluation data  
    hl_size int : number of neurons in the hidden layer  
    af1 : hidden layer activation function 
    af2 : output layer activation function 
    af1_d : derivative of af1
    epochs : number of iterations to train the network
    alpha : learning rate
    random_state : seed to control reproducibility
    '''
    # Layer settings
    n_samples = X.shape[0]                  # Number of samples
    n_labels = len(np.unique(y))            # Number of labels
    n_a1 = X.shape[1]                       # Input layer neurons
    n_a2 = hl_size                          # Hidden layer neurons
    n_a3 = n_labels                         # Output layer neurons
    
    print('Building neural network')
    print(f'Input layer = {n_a1}\nHidden layer = {n_a2}\nOutput layer = {n_a3}')
    
    # Preprocess data
    X, y, X_eval = preprocess(X, y, X_eval, n_labels) 
    # Init weights/biases
    w1, w2, b1, b2 = init_wb([n_a1, n_a2, n_a3], random_state)   
    # Train NN
    w1, w2, b1, b2 = fit(X, y, w1, b1, w2, b2, af1, af2, af1_d, epochs, alpha)
    # Make predictions
    predict(X_eval, w1, b1, w2, b2, af1, af2)


if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
