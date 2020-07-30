#This script loads trained ANN and starts parameters matching (single data input)
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import scale


#11 currents -> 1 speed -> 1 gas flow
input_vector = np.array([273,283,281,279,279,277,276,275,273,277,278,10,6])
input_vector = scale(input_vector)
input_vector_ai = np.array([input_vector])


#The model is trained and output with neural_network/main.py
classifier = keras.models.load_model('./ANN_200.h5')


defects = classifier.predict(input_vector_ai)

print("<<------------------- AI-Output ------------------->>")
print("Raw Output:")
print(defects)

#Thresholding
#0: Incomplete penetration
defects[:, 0] = (defects[:, 0] > 0.6)
#1: Incomplete fusion
defects[:, 1] = (defects[:, 1] > 0.5)
#2: Porosity
defects[:, 2] = (defects[:, 2] > 0.65)
#3: Underfill
defects[:, 3] = (defects[:, 3] > 0.6)

print("Binary Output:")
print(defects)




