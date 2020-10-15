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

from tensorflow import keras
from tensorflow.keras import Sequential,regularizers,Model
from tensorflow.keras.layers import Input,Dense, Dropout, LeakyReLU, concatenate 
from tensorflow.keras import optimizers
from tensorflow import set_random_seed
from tensorflow.keras.utils import plot_model
from numpy.random import seed

# np.seterr(divide='ignore', invalid='ignore')

# this part fixes random seeds to get the same result for each run - reproducibility
set_random_seed(400)
seed(400)
random.seed(400)

start_time = time.time()

# dataset = pd.read_csv("C:\\Users\\nurizdau\\Desktop\\[DATASET]\\results_for_training_final.csv", error_bad_lines=False, header=None)
# /workspace/014-AI_Welding_CNERC/neural_network/input_data
testset = pd.read_csv("/workspace/Welding_Defects_Handler/neural_network/input_data/11_results_final_testing_set_general.csv", error_bad_lines=False, header=None)
trainset = pd.read_csv("/workspace/Welding_Defects_Handler/neural_network/input_data/11_results_final_training_set_general.csv", error_bad_lines=False, header=None)

# print(dataset.describe(include="all"))
# line above prints out the data about dataset

# sns.heatmap(dataset.corr(), annot=True)
# plt.show()
# two lines above are used to plot the heatmap with correlations

# creating input features and target variables
# x = dataset.iloc[:, 0:13]  # input variables -- 11 inputs
# y = dataset.iloc[:, 13:17]  # target variables -- 4 outputs
x_test = testset.iloc[:, 0:11]  # input variables -- 11 inputs
x_test_1 = testset.iloc[:, 11:13] # -- 2 inputs

y_test = testset.iloc[:, 13:17]  # target variables -- 4 outputs

x_train = trainset.iloc[:, 0:11]  # input variables -- 11 inputs
x_train_1 = trainset.iloc[:, 11:13] # -- 2 inputs

y_train = trainset.iloc[:, 13:17]  # target variables -- 4 outputs

# standardizing the input feature -- imported StandardScaler for this purpose
sc = StandardScaler()
# x = sc.fit_transform(x)
x_test = sc.fit_transform(x_test)
x_test_1 = sc.fit_transform(x_test_1)
x_train = sc.fit_transform(x_train)
x_train_1 = sc.fit_transform(x_train_1)
# pd.DataFrame(x_test).to_csv("C:\\Users\\nurizdau\\Desktop\\transformed_set.csv")

# splitting the dataset into train and test -- train_test_split is imported for this purpose
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# print("train inputs are here: ", X_train)
# print("test inputs are here: ", X_test)
# print("train values are here: ", y_train)
# print("test values are here: ", y_test)

# Building the neural network
#---------------------------------------------------------------------------------------------
# Sub-network 1 - Layer1 (for all currents)
left_branch_input = Input(shape=(11,), name='Left_input')
left_branch_output_1 = Dense(100)(left_branch_input)
left_branch_output_2 = LeakyReLU(alpha=0.7)(left_branch_output_1)
left_branch_output_3 = Dropout(0.4)(left_branch_output_2)

# Sub-network 1 - Layer2
left_branch_output_4 = Dense(100)(left_branch_output_3)
left_branch_output_5 = LeakyReLU(alpha=0.7)(left_branch_output_4)
left_branch_output_6 = Dropout(0.4)(left_branch_output_5)

# Sub-network 1 - Layer3
left_branch_output_7 = Dense(100)(left_branch_output_6)
left_branch_output_8 = LeakyReLU(alpha=0.7)(left_branch_output_7)
left_branch_output_9 = Dropout(0.4)(left_branch_output_8)

# Sub-network 1 - Layer4
left_branch_output_10 = Dense(100)(left_branch_output_9)
left_branch_output_11 = LeakyReLU(alpha=0.7)(left_branch_output_10)
left_branch_output_12 = Dropout(0.4)(left_branch_output_11)

# Sub-network 1 - Layer5
left_branch_output_13 = Dense(100)(left_branch_output_12)
left_branch_output_14 = LeakyReLU(alpha=0.7)(left_branch_output_13)
left_branch_output_15 = Dropout(0.4)(left_branch_output_14)

# Sub-network 1 - Layer6
left_branch_output_16 = Dense(100)(left_branch_output_15)
left_branch_output_17 = LeakyReLU(alpha=0.7)(left_branch_output_16)
left_branch_output_18 = Dropout(0.4)(left_branch_output_17)

# Sub-network 1 - Layer7
left_branch_output_19 = Dense(100)(left_branch_output_18)
left_branch_output_20 = LeakyReLU(alpha=0.7)(left_branch_output_19)
left_branch_output_21 = Dropout(0.4)(left_branch_output_20)

# Sub-network 1 - Layer8
left_branch_output_22 = Dense(100)(left_branch_output_21)
left_branch_output_23 = LeakyReLU(alpha=0.7)(left_branch_output_22)
left_branch_output_24 = Dropout(0.4)(left_branch_output_23)

# Sub-network 1 - Layer9
left_branch_output_25 = Dense(100)(left_branch_output_24)
left_branch_output_26 = LeakyReLU(alpha=0.7)(left_branch_output_25)
left_branch_output_27 = Dropout(0.4)(left_branch_output_26)
#---------------------------------------------------------------------------------------------
# Sub-network 2 - Layer1 (for speed and gas flow)
right_branch_input = Input(shape=(2,), name='Right_input')
right_branch_output_1 = Dense(80,activation='tanh')(right_branch_input)
#right_branch_output_2 = Dropout(0.4)(right_branch_output_1)

# Sub-network 2 - Layer2
right_branch_output_2 = Dense(80,activation='tanh')(right_branch_output_1)
#right_branch_output_4 = Dropout(0.4)(right_branch_output_3)

# Sub-network 2 - Layer3
right_branch_output_3 = Dense(80,activation='tanh')(right_branch_output_2)

# Sub-network 2 - Layer4
right_branch_output_4 = Dense(80,activation='tanh')(right_branch_output_3)

#---------------------------------------------------------------------------------------------
# Combined network
concat = concatenate([left_branch_output_27, right_branch_output_4], name='Concatenate')

classifier_output = Dense(4, activation='sigmoid')(concat)
#---------------------------------------------------------------------------------------------
classifier = Model(inputs=[left_branch_input, right_branch_input], outputs=classifier_output,
                    name='classifier_output')


initial_learning_rate = 0.01
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate,
    decay_steps=200,
    decay_rate=0.96,
    staircase=True)


sgd = optimizers.SGD(learning_rate=lr_schedule, momentum=0.9)
#adam = optimizers.Adam(learning_rate=lr_schedule)
classifier.compile(optimizer=sgd, loss='binary_crossentropy', metrics=['accuracy'])

# Fitting the data to the training dataset
# batch_size is how many samples we use to update the gradient
# epochs are how many times we repeat the iterations
#history = classifier.fit(x_train, y_train, batch_size=289, validation_data=(x_test, y_test), epochs=18000)
history = classifier.fit([x_train,x_train_1], y_train, batch_size=64, validation_data=([x_test,x_test_1], y_test), epochs=1200)
print("History keys are following: ")
print(history.history.keys())

# plot history for the accuracy of training and validation set for each epoch
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['accuracy', 'validation accuracy'], loc='upper left')
plt.show()

# plot history for the loss of training and validation set for each epoch
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['loss', 'validation loss'], loc='upper left')
plt.show()


# evaluate the loss value and metrics values for the model
eval_model = classifier.evaluate([x_train,x_train_1], y_train)
print("Eval model is printed here: ", eval_model)


# here we predict the output for our test dataset
print("-----------------------------------------------")
print(x_test)

y_pred = classifier.predict([x_test,x_test_1])

print(y_pred)
print("-----------------------------------------------")

# pd.DataFrame(y_pred).to_csv("C:\\Users\\nurizdau\\Desktop\\predicted_probs.csv")

# classifies them into 2 classes
y_pred[:, 0] = (y_pred[:, 0] > 0.6)
y_pred[:, 1] = (y_pred[:, 1] > 0.5)
y_pred[:, 2] = (y_pred[:, 2] > 0.65)
y_pred[:, 3] = (y_pred[:, 3] > 0.6)
# y_pred[:, 4] = (y_pred[:, 4] > 0.5)

pd.DataFrame(y_pred).to_csv("/workspace/Welding_Defects_Handler/neural_network/output_data/predicted_results.csv")
pd.DataFrame(y_test.values).to_csv("/workspace/Welding_Defects_Handler/neural_network/output_data/testing_results.csv")

# check the accuracy on the dataset -- confusion_matrix is used for this purpose

# initially wanted to use this approach, but it did not work for 2-dim arrays
# cm = confusion_matrix(y_test.values.argmax(axis=1), y_pred.astype(int).argmax(axis=1))
# that's why firstly flattened results and then compared them
new_test_y = y_test.values.flatten()
new_pred_y = y_pred.astype(int).flatten()
cm = confusion_matrix(new_test_y, new_pred_y)
print(cm)

# from here we can easily calculate accuracy, sensitivity and specificity
print("accuracy for incompen is: ", ((cm[0][0]+cm[1][1])/np.sum(cm))*100)
print("sensitivity for incompen is: ", (cm[0][0]/np.sum(cm[0]))*100)
print("specificity for incompen is: ", (cm[1][1]/np.sum(cm[1]))*100)

# or we can calculate it like this, but we won't be able to filter it by defect
print("Model Accuracy is printed here: ", classifier.evaluate([x_test,x_test_1], y_test))

print("Time spent to execute this program is %s seconds" % (time.time() - start_time))

# print("The train set is: ", sc.inverse_transform(x_train))
# print("The train set is: ", sc.inverse_transform(x_test))

#saved trained model
#classifier.save('/workspace/Welding_Defects_Handler/neural_network/ANN_v3.h5')
print("Model saved and exported!")

"""
#Reproduce the results
classifier_new = keras.models.load_model('/workspace/Welding_Defects_Handler/neural_network/output_data/ANN_v3.h5')
print(x_test)

y_pred_new = classifier_new.predict([x_test,x_test_1])

print(y_pred_new)

y_pred_new[:, 0] = (y_pred_new[:, 0] > 0.6)
y_pred_new[:, 1] = (y_pred_new[:, 1] > 0.5)
y_pred_new[:, 2] = (y_pred_new[:, 2] > 0.65)
y_pred_new[:, 3] = (y_pred_new[:, 3] > 0.6)

print(y_pred_new)

print(classifier.summary())

plot_model(classifier, to_file='ANN_v3_Architecture.png', show_shapes=True, show_layer_names=True)
print("saved!")
"""
