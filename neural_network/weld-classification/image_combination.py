import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
import time
import random
import cv2

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import optimizers
from tensorflow import set_random_seed
from numpy.random import seed

set_random_seed(400)
seed(400)
random.seed(400)

start_time = time.time()

input_values = pd.read_csv("C:\\Users\\nurizdau\\Desktop\\[DATASET]\\results_for_training_final.csv", error_bad_lines=False, header=None)
input_values = input_values.values

final_dataset = []

for i in range(1, 363):
    img_one = cv2.imread("C:\\Users\\nurizdau\\Desktop\\[DATASET]\\Cut Video Files\\Snapshots\\%d-global-snapshot-%d.png" % (i, 7), 0)
    # img_two = cv2.imread("C:\\Users\\nurizdau\\Desktop\\[DATASET]\\Cut Video Files\\Snapshots\\%d-global-snapshot-%d.png" % (i, 9), 0)

    dim = (1280, 1024)
    img_one = cv2.resize(img_one, dim)
    # img_two = cv2.resize(img_two, dim)

    img_one = img_one.flatten()
    # img_two = img_two.flatten()

    # images = np.concatenate([img_one, img_two])
    # input_row_final = np.concatenate([images, input_values[i-1]])
    # final_dataset.append(input_row_final)
    final_dataset.append(img_one)


final_dataset = np.array(final_dataset)

x = final_dataset[:, 0:1310720]
y = input_values[:, 13:17]

sc = StandardScaler()
x = sc.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

classifier = tf.keras.Sequential()
classifier.add(Dense(150, activation='sigmoid', kernel_initializer='random_normal', input_dim=1310720))
classifier.add(Dropout(0.3))
classifier.add(Dense(150, activation='sigmoid', kernel_initializer='random_normal'))
classifier.add(Dropout(0.3))
classifier.add(Dense(150, activation='sigmoid', kernel_initializer='random_normal'))
classifier.add(Dropout(0.3))
classifier.add(Dense(4, activation='sigmoid', kernel_initializer='random_normal'))

sgd = optimizers.SGD(learning_rate=0.01, momentum=0.0)
classifier.compile(optimizer='SGD', loss='binary_crossentropy', metrics=['accuracy'])

history = classifier.fit(x_train, y_train, batch_size=1, validation_data=(x_test, y_test), epochs=100)
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

eval_model = classifier.evaluate(x_train, y_train)
print("Eval model is printed here: ", eval_model)

y_pred = classifier.predict(x_test)
pd.DataFrame(y_pred).to_csv("C:\\Users\\nurizdau\\Desktop\\predicted_image_probs.csv")

y_pred[:, 0] = (y_pred[:, 0] > 0.8)
y_pred[:, 1] = (y_pred[:, 1] > 0.8)
y_pred[:, 2] = (y_pred[:, 2] > 0.8)
y_pred[:, 3] = (y_pred[:, 3] > 0.8)

new_test_y = y_test.flatten()
new_pred_y = y_pred.astype(int).flatten()
cm = confusion_matrix(new_test_y, new_pred_y)
print(cm)

# from here we can easily calculate accuracy, sensitivity and specificity
print("accuracy is: ", ((cm[0][0]+cm[1][1])/np.sum(cm))*100)
print("sensitivity is: ", (cm[0][0]/np.sum(cm[0]))*100)
print("specificity is: ", (cm[1][1]/np.sum(cm[1]))*100)

print("Model Accuracy is printed here: ", classifier.evaluate(x_test, y_test))

print("Time spent to execute this program is %s seconds" % (time.time() - start_time))
