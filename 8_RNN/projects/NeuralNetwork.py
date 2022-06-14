# Math operations and data manipulation
import numpy as np
import pandas as pd
# Data Visualization
import matplotlib.pyplot as plt
# Progress bar
from tqdm.auto import tqdm

class NeuralNetwork():
    
    def __init__(self, hl_size=16, epochs=3, alpha=0.01, random_state=None):
        self.hl_size = hl_size
        self.epochs = epochs
        self.alpha = alpha
        self.random_state = random_state
        self.score = 0
        self.best_loss = 99999
    
    # Preprocess data
    def preprocess(self, X, y):
        X /= X.max(axis=1).max()                  # Normalize train values
        y_enc = np.zeros((y.size, self.n_labels)) # One hot encode labels
        y_enc[np.arange(y.size), y] = 1
        return X, y_enc
    
    # Init weights/biases
    def init_wb(self, grid):
        np.random.seed(self.random_state)                      
        self.w1 = np.random.uniform(-0.5, 0.5, [grid[1], grid[0]])
        self.w2 = np.random.uniform(-0.5, 0.5, [grid[2], grid[1]])
        self.b1 = np.zeros([grid[1], 1])         
        self.b2 = np.zeros([grid[2], 1])
    
    # Fit model
    def fit(self, X, y):
        # Layer settings
        self.n_samples = X.shape[0]             # Number of samples
        self.n_labels = len(np.unique(y))       # Number of labels
        n_a1 = X.shape[1]                       # Input layer neurons
        n_a2 = self.hl_size                     # Hidden layer neurons
        n_a3 = self.n_labels                    # Output layer neurons
        print('Building neural network')
        print(f'Input layer = {n_a1}\nHidden layer = {n_a2}\nOutput layer = {n_a3}')
        # Preprocess data
        X, y = self.preprocess(X, y) 
        # Init weights/biases
        self.init_wb([n_a1, n_a2, n_a3])
        # Train NN
        self.train(X, y)
    
    # Train model
    def train(self, X, y):
        af1 = self.sigmoid
        af1_d = self.sigmoid_d
        af2 = self.softmax
        for epoch in range(self.epochs):     
            acc = 0      # Reset acc counter
            pbar = tqdm(          
                zip(X, y), 
                total=self.n_samples, 
                colour='#1696d2')    
            for sample, label in pbar:
                a1 = sample.reshape(-1,1)               # Reshape features/label to fit layer shape
                y_true = label.reshape(-1,1)    
                a2 = af1(self.w1 @ a1 + self.b1)        # Foward Input -> Hidden layer
                a3 = af2(self.w2 @ a2 + self.b2)        # Foward Hidden -> Output layer
                a2_d =  a3 - y_true                     # Backward Ouput -> Hidden layer                  
                self.w2 += -self.alpha * a2_d @ a2.T    # Update a2 weights/biases
                self.b2 += -self.alpha * a2_d
                a1_d   =  self.w2.T @ a2_d * af1_d(a2)  # Backward Hidden -> Input layer   
                self.w1 += -self.alpha * a1_d @ a1.T    # Update a1 weights/biases
                self.b1 += -self.alpha * a1_d
                # Calculate error
                error = self.cross_entropy(a3, y_true)
                if error < self.best_loss: self.best_loss = error
                # Calculate accuracy
                acc += int(np.argmax(a3) == np.argmax(y_true))
                current_score = acc/self.n_samples*100
                pbar.set_description(f'Epoch {epoch+1}, Acc={current_score:.2f}, Loss={error[0]:.4f}')
            pbar.close()
            if current_score > self.score:     # Update score
                self.score = current_score

    # Make predictions
    def predict(self, X_eval, image_shape=None):
        eval_samples = X_eval.shape[0]       # Number of samples
        X_eval /= X_eval.max(axis=1).max()   # Normalization
        y_pred = np.zeros([self.n_labels, 1])             
        for a1 in tqdm(X_eval, total=eval_samples, desc='Making predictions', colour='#fdbf11'):
            a1.shape += (1,)
            a2 = self.sigmoid(self.w1 @ a1 + self.b1)            
            a3 = self.softmax(self.w2 @ a2 + self.b2)
            y_pred  = np.append(y_pred, a3, axis=1)
        y_pred = y_pred.T[1:]
        
        # Plot sample predictions
        if image_shape:
            sample_pred = np.argmax(y_pred, axis=1)[:10]
            fig, ax = plt.subplots(1,10, figsize=(18,6))
            fig.suptitle('Sample predictions', size=18, x=0.19, y=0.725)
            for i in range(10): 
                ax[i].imshow(X_eval[i].reshape(image_shape[0], image_shape[1]))
                ax[i].set_xticks([]); ax[i].set_yticks([])
                ax[i].set_title(f'{sample_pred[i]}', size=18)
                ax[i].grid(False)

        return y_pred

    # Categorical Cross-Entropy for One Hot Encoded Labels
    @staticmethod
    def cross_entropy(y_pred, y_true):
        return -(np.log(y_pred[np.argmax(y_true)]))
    # Sigmoid function
    @staticmethod
    def sigmoid(x): 
        return 1 / (1 + np.exp(-x))
    # Derivative of sigmoid function
    @staticmethod
    def sigmoid_d(x): 
        return x * (1 - x)
    # Softmax
    @staticmethod
    def softmax(x):
        e_x = np.exp(x - np.max(x, keepdims=True))
        return e_x / np.sum(e_x, keepdims=True)

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
    