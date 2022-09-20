
import os
import numpy as np
import pandas as pd
import flask
import pickle
from flask import Flask, render_template, request
from sklearn import svm, datasets

app = Flask(__name__)

@app.route('/')
def index():
	return flask.render_template('index.html')

def ValuePredictor(predict_list: list):
	
	predict_list = np.array(predict_list).reshape(1, 4)
	with open('iris_model.pickle', 'rb') as file:
		loaded_model = pickle.load(file)
		predictor = loaded_model.predict()
		print(f'Model loaded.')

	return predictor[0]

def pickle_model(path: str):

	iris = datasets.load_iris()
	X = iris.data
	y = iris.target
	model = svm.SVC(kernel='poly', degree=3, C=1.0).fit(X, y)

	with open(path + 'iris_model.pickle', 'wb') as file:
		pickle.dump(model, file, protocol=pickle.HIGHEST_PROTOCOL)
		print(f'Model saved in: {path}')

@app.route('/predict', methods=['POST'])
def result():
	
	if request.method=='POST':
		predict_list = request.form.to_dict().values()
		predict_list = list(predict_list)
		predict_list = list(map(float, predict_list))

		result = ValuePredictor(predict_list)
		pred = str(result)

		# TODO: write cleaner code
		if pred == '0':
			pred='versicolor'
		elif pred == '1':
			pred = 'virginica'
		elif pred == '2':
			pred = 'setosa'
	
	return render_template('predict.html', )
	
if __name__ == '__main__':
	
	pickle_model('')
	app.run(host='0.0.0.0', debug=True)
