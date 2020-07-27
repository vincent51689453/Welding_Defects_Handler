import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import time
import random

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
# from sklearn.metrics import confusion_matrix

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow import set_random_seed
from numpy.random import seed

# this part fixes random seeds to get the same result for each run - reproducibility
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.layers import Dropout

set_random_seed(400)
seed(400)
random.seed(400)

start_time = time.time()

# dataset = pd.read_csv("C:\\Users\\nurizdau\\Desktop\\[DATASET]\\results_for_training_final.csv", header=None)
testset = pd.read_csv("C:\\Users\\nurizdau\\Desktop\\[DATASET]\\11_results_final_testing_set_general.csv", error_bad_lines=False, header=None)
trainset = pd.read_csv("C:\\Users\\nurizdau\\Desktop\\[DATASET]\\11_results_final_training_set_general.csv", error_bad_lines=False, header=None)

x_test = testset.iloc[:, 0:13]  # input variables -- 13 inputs
# y_test = testset.iloc[:, 13:17]  # target variables -- 1 outputs
x_train = trainset.iloc[:, 0:13]  # input variables -- 13 inputs
# y_train = trainset.iloc[:, 13:17]  # target variables -- 1 outputs

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

def predictIncompletePenetration(x_train, y_train, x_test, y_test):
    # x = sc.fit_transform(x)
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    classifier = Sequential()
    classifier.add(Dense(100, activation='sigmoid', kernel_initializer='random_normal', input_dim=13))
    classifier.add(Dropout(0.0))
    classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))
    optimizer = optimizers.SGD(lr=0.01, momentum=0.4)
    classifier.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['accuracy'])

    history = classifier.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=1, epochs=400)

    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title("IncomPen's accuracy graph")
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['accuracy', 'validation accuracy'], loc='upper left')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title("IncomPen's loss graph")
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['loss', 'validation loss'], loc='upper left')
    plt.show()

    y_pred = classifier.predict(x_test)

    pd.DataFrame(y_pred).to_csv("C:\\Users\\nurizdau\\Desktop\\predicted_probs_incompen.csv")

    y_pred[:] = (y_pred[:] > 0.7)

    # pd.DataFrame(y_pred).to_csv("C:\\Users\\nurizdau\\Desktop\\predicted_results_incompen.csv")

    eval_model = classifier.evaluate(x_test, y_test)
    resultString = "Accuracy (incomplete penetration) is printed here: " + str(eval_model[1])

    new_test_y = y_test.values.flatten()
    new_pred_y = y_pred.astype(int).flatten()
    cm = confusion_matrix(new_test_y, new_pred_y)
    print(cm)
    print("accuracy of Incomplete Penetration is: ", ((cm[0][0] + cm[1][1]) / np.sum(cm)) * 100)
    print("sensitivity of Incomplete Penetration is: ", (cm[0][0] / np.sum(cm[0])) * 100)
    print("specificity of Incomplete Penetration is: ", (cm[1][1] / np.sum(cm[1])) * 100)

    return resultString


def predictIncompleteFusion(x_train, y_train, x_test, y_test):

    classifier = Sequential()
    classifier.add(Dense(45, activation='sigmoid', kernel_initializer='random_normal', input_dim=13))
    classifier.add(Dropout(0.6))
    classifier.add(Dense(45, activation='sigmoid', kernel_initializer='random_normal'))
    classifier.add(Dropout(0.6))
    classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))
    optimizer=optimizers.SGD(lr=0.9, momentum=0.4)
    classifier.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

    history = classifier.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=1, epochs=250)

    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title("IncomFus' accuracy graph")
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['accuracy', 'validation accuracy'], loc='upper left')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title("IncomFus' loss graph")
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['loss', 'validation loss'], loc='upper left')
    plt.show()

    y_pred = classifier.predict(x_test)

    pd.DataFrame(y_pred).to_csv("C:\\Users\\nurizdau\\Desktop\\predicted_probs_incomfus.csv")

    y_pred[:] = (y_pred[:] > 0.5)

    # pd.DataFrame(y_pred).to_csv("C:\\Users\\nurizdau\\Desktop\\predicted_results_incomfus.csv")

    eval_model = classifier.evaluate(x_test, y_test)
    resultString = "Accuracy (incomplete fusion) is printed here: " + str(eval_model[1])

    new_test_y = y_test.values.flatten()
    new_pred_y = y_pred.astype(int).flatten()
    cm = confusion_matrix(new_test_y, new_pred_y)
    print(cm)
    print("accuracy of Incomplete Fusion is: ", ((cm[0][0] + cm[1][1]) / np.sum(cm)) * 100)
    print("sensitivity of Incomplete Fusion is: ", (cm[0][0] / np.sum(cm[0])) * 100)
    print("specificity of Incomplete Fusion is: ", (cm[1][1] / np.sum(cm[1])) * 100)

    return resultString


def predictPorosity(x_train, y_train, x_test, y_test):

    classifier = Sequential()
    classifier.add(Dense(90, activation='sigmoid', kernel_initializer='random_normal', input_dim=13))
    classifier.add(Dropout(0.0))
    classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))
    optimizer=optimizers.SGD(lr=0.9, momentum=0.0)
    classifier.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['accuracy'])

    history = classifier.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=1, epochs=400)

    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title("Porosity's accuracy graph")
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['accuracy', 'validation accuracy'], loc='upper left')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title("Porosity's loss graph")
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['loss', 'validation loss'], loc='upper left')
    plt.show()
    y_pred = classifier.predict(x_test)

    pd.DataFrame(y_pred).to_csv("C:\\Users\\nurizdau\\Desktop\\predicted_probs_porosity.csv")

    y_pred[:] = (y_pred[:] > 0.9)

    # pd.DataFrame(y_pred).to_csv("C:\\Users\\nurizdau\\Desktop\\predicted_results_porosity.csv")

    eval_model = classifier.evaluate(x_test, y_test)
    resultString = "Accuracy (porosity) is printed here: " + str(eval_model[1])

    new_test_y = y_test.values.flatten()
    new_pred_y = y_pred.astype(int).flatten()
    cm = confusion_matrix(new_test_y, new_pred_y)
    print(cm)
    print("accuracy of Porosity is: ", ((cm[0][0] + cm[1][1]) / np.sum(cm)) * 100)
    print("sensitivity of Porosity is: ", (cm[0][0] / np.sum(cm[0])) * 100)
    print("specificity of Porosity is: ", (cm[1][1] / np.sum(cm[1])) * 100)

    return resultString


def predictNotEnoughFiller(x_train, y_train, x_test, y_test):

    classifier = Sequential()
    classifier.add(Dense(55, activation='softmax', kernel_initializer='random_normal', input_dim=13))
    classifier.add(Dropout(0.2))
    classifier.add(Dense(55, activation='softmax', kernel_initializer='random_normal'))
    classifier.add(Dropout(0.2))
    classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))
    optimizer=optimizers.SGD(lr=0.1, momentum=0.9)
    classifier.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['accuracy'])

    history = classifier.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=1, epochs=250)

    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title("Underfill's accuracy graph")
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['accuracy', 'validation accuracy'], loc='upper left')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title("Underfill's loss graph")
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['loss', 'validation loss'], loc='upper left')
    plt.show()
    y_pred = classifier.predict(x_test)

    pd.DataFrame(y_pred).to_csv("C:\\Users\\nurizdau\\Desktop\\predicted_probs_underfill.csv")

    y_pred[:] = (y_pred[:] > 0.7)

    # pd.DataFrame(y_pred).to_csv("C:\\Users\\nurizdau\\Desktop\\predicted_results_underfill.csv")

    eval_model = classifier.evaluate(x_test, y_test)
    resultString = "Accuracy (underfill) is printed here: " + str(eval_model[1])

    new_test_y = y_test.values.flatten()
    new_pred_y = y_pred.astype(int).flatten()
    cm = confusion_matrix(new_test_y, new_pred_y)
    print(cm)
    print("accuracy of Underfill is: ", ((cm[0][0] + cm[1][1]) / np.sum(cm)) * 100)
    print("sensitivity of Underfill is: ", (cm[0][0] / np.sum(cm[0])) * 100)
    print("specificity of Underfill is: ", (cm[1][1] / np.sum(cm[1])) * 100)

    return resultString


outputString = predictIncompletePenetration(x_train, trainset.iloc[:, 13], x_test, testset.iloc[:, 13]) + "\n" + \
               predictIncompleteFusion(x_train, trainset.iloc[:, 14], x_test, testset.iloc[:, 14]) + "\n" + \
               predictPorosity(x_train, trainset.iloc[:, 15], x_test, testset.iloc[:, 15]) + "\n" + \
               predictNotEnoughFiller(x_train, trainset.iloc[:, 16], x_test, testset.iloc[:, 16])

print(outputString)
print("Time spent to execute this program is %s seconds" % (time.time() - start_time))
