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
y_train = trainset.iloc[:, 13:17]  # target variables -- 4 outputs

# standardizing the input feature -- imported StandardScaler for this purpose
sc = StandardScaler()
x_train = sc.fit_transform(x_train)


# Building the neural network
def createModel(learn_rate=0.01, momentum=0, initialization_mode='random_normal', activation='sigmoid',
                dropout_rate=0.0, neuron=50, loss='mean_squared_error'):
    classifier = tf.keras.Sequential()
    classifier.add(Dense(40, activation='sigmoid', kernel_initializer='random_normal', input_dim=13))
    classifier.add(Dropout(0.0))
    classifier.add(Dense(40, activation='sigmoid', kernel_initializer='random_normal'))
    classifier.add(Dropout(0.0))
    classifier.add(Dense(4, activation='sigmoid', kernel_initializer='random_normal'))
    optimizer = optimizers.SGD(lr=0.7, momentum=0.9)
    classifier.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])

    return classifier


# create Model
model = KerasClassifier(build_fn=createModel, batch_size=1, epochs=1600, verbose=0)

# define the grid search parameters
losses = ['binary_crossentropy', 'mean_squared_error', 'mean_absolute_error']
# neurons = [30, 40, 45, 50, 55, 60]
# dropout_rates = [0.0, 0.2, 0.4, 0.6, 0.9]
# activations = ['softmax', 'relu', 'tanh', 'sigmoid', 'linear']
# init_mode = ['random_normal', 'zeros', 'ones']
# batch_size = [1, 8, 16, 32]
# epochs = [1000, 1200, 1400, 1600]
# learning_rate = [0.1, 0.3, 0.5, 0.7, 0.9]
# momentums = [0.0, 0.2, 0.4, 0.6, 0.9]
param_grid = dict(loss=losses)
# batch_size=batch_size, epochs=epochs
# learn_rate=learning_rate, momentum=momentums
# initialization_mode=init_mode
# activation=activations, dropout_rate=dropout_rates, neuron=neurons
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=5)
grid_result = grid.fit(x_train, y_train)

# summarize results
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']

for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))

print("Time spent to execute this program is %s seconds" % (time.time() - start_time))
