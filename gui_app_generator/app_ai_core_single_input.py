#This script loads trained ANN and starts parameters matching (single data input)
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import StandardScaler

# standardizing the input feature -- imported StandardScaler for this purpose
sc = StandardScaler()

#11 currents -> 1 speed -> 1 gas flow
input_vector = np.array([[176,180,179,176,173,171,173,174,173,172,165,6,3]])
# x = sc.fit_transform(x)
input_vector = sc.fit_transform(input_vector)

#The model is trained and output with neural_network/main.py
classifier = keras.models.load_model('./ANN.h5')

defects = classifier.predict(input_vector)

print("<<------------------- AI-Output ------------------->>")
print("Raw Output:")
print(defects)

#Thresholding
#0:
defects[:, 0] = (defects[:, 0] > 0.6)
defects[:, 1] = (defects[:, 1] > 0.5)
defects[:, 2] = (defects[:, 2] > 0.65)
defects[:, 3] = (defects[:, 3] > 0.6)

print("Binary Output:")
print(defects)



