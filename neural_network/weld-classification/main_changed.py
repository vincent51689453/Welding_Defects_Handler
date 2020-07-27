import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
import time
import random

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from tensorflow.keras import Sequential  # there are two types of model in Keras: Sequential and Model
from tensorflow.keras.layers import Dense, Dropout  # imported to build input, hidden and output layers
from tensorflow.keras import optimizers
from tensorflow import set_random_seed
from numpy.random import seed

# np.seterr(divide='ignore', invalid='ignore')

# this part fixes random seeds to get the same result for each run - reproducibility
set_random_seed(400)
seed(400)
random.seed(400)

start_time = time.time()

# dataset = pd.read_csv("C:\\Users\\nurizdau\\Desktop\\[DATASET]\\results_for_training_final.csv", error_bad_lines=False, header=None)
testset = pd.read_csv("C:\\Users\\nurizdau\\Desktop\\[DATASET]\\11_results_final_testing_set_general.csv", error_bad_lines=False, header=None)
trainset = pd.read_csv("C:\\Users\\nurizdau\\Desktop\\[DATASET]\\11_results_final_testing_set_general.csv", error_bad_lines=False, header=None)

# print(dataset.describe(include="all"))
# line above prints out the data about dataset

# sns.heatmap(dataset.corr(), annot=True)
# plt.show()
# two lines above are used to plot the heatmap with correlations

# creating input features and target variables
# x = dataset.iloc[:, 0:13]  # input variables -- 13 inputs
# y = dataset.iloc[:, 13:17]  # target variables -- 4 outputs
x_test = testset.iloc[:, 0:13]  # input variables -- 13 inputs
y_test = testset.iloc[:, 13:17]  # target variables -- 4 outputs
x_train = trainset.iloc[:, 0:13]  # input variables -- 13 inputs
y_train = trainset.iloc[:, 13:17]  # target variables -- 4 outputs

# standardizing the input feature -- imported StandardScaler for this purpose
sc = StandardScaler()
# x = sc.fit_transform(x)
x_test = sc.fit_transform(x_test)
x_train = sc.fit_transform(x_train)

# pd.DataFrame(x_test).to_csv("C:\\Users\\nurizdau\\Desktop\\transformed_set.csv")

# splitting the dataset into train and test -- train_test_split is imported for this purpose
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# print("train inputs are here: ", X_train)
# print("test inputs are here: ", X_test)
# print("train values are here: ", y_train)
# print("test values are here: ", y_test)

# Building the neural network
classifier = tf.keras.Sequential()

classifier.add(Dense(20, activation='sigmoid', kernel_initializer='random_normal', input_dim=13))
classifier.add(Dropout(0.0))
classifier.add(Dense(20, activation='sigmoid', kernel_initializer='random_normal'))
classifier.add(Dropout(0.0))
classifier.add(Dense(20, activation='sigmoid', kernel_initializer='random_normal'))
classifier.add(Dropout(0.0))

classifier.add(Dense(4, activation='sigmoid', kernel_initializer='random_normal'))

sgd = optimizers.SGD(learning_rate=0.01, momentum=0.0)
classifier.compile(optimizer='SGD', loss='mean_squared_error', metrics=['accuracy'])

history = classifier.fit(x_train, y_train, batch_size=1, validation_data=(x_test, y_test), epochs=4000)
eval_model = classifier.evaluate(x_train, y_train)

y_pred = classifier.predict(x_test)
y_pred[:, 0] = (y_pred[:, 0] > 0.8)
y_pred[:, 1] = (y_pred[:, 1] > 0.8)
y_pred[:, 2] = (y_pred[:, 2] > 0.8)
y_pred[:, 3] = (y_pred[:, 3] > 0.8)


new_test_y = y_test.values.flatten()
new_pred_y = y_pred.astype(int).flatten()
cm = confusion_matrix(new_test_y, new_pred_y)
print(cm)

# from here we can easily calculate accuracy, sensitivity and specificity
print("accuracy is: ", ((cm[0][0]+cm[1][1])/np.sum(cm))*100)
print("sensitivity is: ", (cm[0][0]/np.sum(cm[0]))*100)
print("specificity is: ", (cm[1][1]/np.sum(cm[1]))*100)

# or we can calculate it like this, but we won't be able to filter it by defect
print("Model Accuracy is printed here: ", classifier.evaluate(x_test, y_test))

print("Time spent to execute this program is %s seconds" % (time.time() - start_time))

# print("The train set is: ", sc.inverse_transform(x_train))
# print("The train set is: ", sc.inverse_transform(x_test))
