# defines all the methods to classify the text and return results

#importing
# imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB,MultinomialNB
import keras
from keras import Sequential
from keras import *
from keras.layers import *
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from tensorflow.keras.models import load_model



def build_model():
	# building network
# after multiple attempts to prevent overfitting, this was the most apt model created
	model = Sequential()
	model.add(Dense(32, input_dim=100, activation="relu",kernel_regularizer=keras.regularizers.l2(0.001)))
	model.add(Dropout(0.5))
	model.add(Dense(32, activation="relu", kernel_regularizer=keras.regularizers.l2(0.001)))
	model.add(Dropout(0.5))
	model.add(Dense(64, activation="relu",kernel_regularizer=keras.regularizers.l2(0.001)))
	model.add(Dropout(0.5))
	model.add(Dense(1, activation="sigmoid"))
	model.compile(optimizer="adam", loss=keras.losses.binary_crossentropy, metrics=['acc'])

	return model

def load(model):
	try:
		model.load_weights("saved_weights/model1.weights")

		return True
	except:
		return False

"""
	get_results()
	return the analysis using the model
"""

def get_results(model, vectorized_input):
	model = load_model("model.h5")

	try: # check if shape is correct.
		predictions = model.predict(vectorized_input).round()
	except:
		print ("Error!")
	pos=0
	neg=0


	for i in predictions:
		if i[0] == 1:
			pos+=1
		else:
			neg+=1
	analysis = ""
	if pos >= neg:
		analysis = "GOOD!"
	else:
		analysis = "BAD!"

	return {"pos":pos, "neg":neg, "analysis":analysis}
