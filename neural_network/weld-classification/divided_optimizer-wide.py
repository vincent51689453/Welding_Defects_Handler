import pandas as pd
import tensorflow as tf
import time
import random

from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from tensorflow.python.keras import optimizers

from tensorflow.python.keras.wrappers.scikit_learn import KerasClassifier
from tensorflow.keras.layers import Dense, Dropout  # imported to build input, hidden and output layers
from tensorflow import set_random_seed
from numpy.random import seed

# this part fixes random seeds to get the same result for each run - reproducibility

set_random_seed(400)
seed(400)
random.seed(400)

start_time = time.time()

trainset = pd.read_csv("C:\\Users\\nurizdau\\Desktop\\[DATASET]\\11_results_final_training_set_general.csv", error_bad_lines=False, header=None)


# creating input features and target variables
x_train = trainset.iloc[:, 0:13]  # input variables -- 13 inputs
y_train_incompen = trainset.iloc[:, 13]  # target variables -- 1 output
y_train_incomfus = trainset.iloc[:, 14]  # target variables -- 1 output
y_train_porosity = trainset.iloc[:, 15]  # target variables -- 1 output
y_train_underfill = trainset.iloc[:, 16]  # target variables -- 1 output

# standardizing the input feature -- imported StandardScaler for this purpose
sc = StandardScaler()
x_train = sc.fit_transform(x_train)


# Building the neural network
def createModel(learn_rate=0.01, momentum=0, initialization_mode='random_normal', activation='sigmoid',
                dropout_rate=0.0, neuron=100, loss='mean_squared_error', optimizer='SGD'):
    classifier = tf.keras.Sequential()
    classifier.add(Dense(90, activation='sigmoid', kernel_initializer='random_normal', input_dim=13))
    classifier.add(Dropout(0.0))
    classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))
    optimizer = optimizers.SGD(lr=0.9, momentum=0.0)
    classifier.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])

    return classifier


# create Model
model = KerasClassifier(build_fn=createModel, batch_size=32, epochs=400, verbose=0)

# define the grid search parameters
losses = ['binary_crossentropy', 'mean_squared_error', 'mean_absolute_error']
# neurons = [80, 90, 100, 110]
# dropout_rates = [0.0, 0.2, 0.4, 0.6, 0.8, 0.9]
# activations = ['softmax', 'relu', 'tanh', 'sigmoid', 'linear']
# init_mode = ['random_normal', 'zeros', 'ones']
# batch_size = [1, 8, 16, 32]
# epochs = [250, 300, 350, 400]
# learning_rate = [0.1, 0.3, 0.5, 0.7, 0.9]
# momentums = [0.0, 0.2, 0.4, 0.6, 0.9]
# optimizers = ['SGD', 'RMSprop', 'ADAM']
param_grid = dict(loss=losses)
# optimizer=optimizers
# batch_size=batch_size, epochs=epochs
# learn_rate=learning_rate, momentum=momentums
# initialization_mode=init_mode
# activation=activations, dropout_rate=dropout_rates, neuron=neurons
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3)

# first run for incomplete penetration
grid_result = grid.fit(x_train, y_train_incompen)

# summarize results
print("Best for incompen: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))

# second run for the porosity optimization
model = KerasClassifier(build_fn=createModel, batch_size=1, epochs=400, verbose=0)
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3)
grid_result = grid.fit(x_train, y_train_porosity)

# summarize results
print("Best for porosity: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']

for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))

print("Time spent to execute this program is %s seconds" % (time.time() - start_time))
