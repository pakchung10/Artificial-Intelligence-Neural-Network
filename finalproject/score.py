#@Author:pakchungy
#@Date:2021/5/27
#@Time:0:23
#@Project_name:finalproject

from sklearn.metrics import mean_squared_error, explained_variance_score
import numpy as np

def mse(true_data_set,predicted_data_set):
    mse = mean_squared_error(true_data_set, predicted_data_set)
    print('Mean Squared Error : {}'.format(mse))

def rmse(true_data_set, predicted_data_set):
    rmse = np.sqrt(mean_squared_error(true_data_set, predicted_data_set))
    print('Root Mean Squared Error : {}'.format(rmse))

def evs(true_data_set, predicted_data_set):
    evs = explained_variance_score(true_data_set, predicted_data_set)
    print('Explained Variance Score: {}'.format(evs))


