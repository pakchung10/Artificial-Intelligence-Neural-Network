#@Author:pakchungy
#@Date:2021/5/27
#@Time:0:23
#@Project_name:finalproject

import time

import torch
import torch.nn as nn
from RNN import temperature_model_RNN as tm_RNN
import temperature_dataset as td
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np

from score import *

def test(model, test_loader, criterion):
    y_pred_list = []
    y_true_list = []
    loss = 0
    for i, (x, y) in enumerate(test_loader, 0):
        # 计算预测值
        y_pred = model(x)
        loss += criterion(y_pred, y)
        y_pred = y_pred.detach().numpy().reshape(y_pred.shape[0])
        y = y.detach().numpy().reshape(y.shape[0])
        if i == 0:
            y_pred_list = y_pred
            y_true_list = y
        else:
            y_pred_list = np.concatenate((y_pred_list, y_pred))
            y_true_list = np.concatenate((y_true_list, y))

    loss /= i
    # 画图
    plt.figure(figsize=(10, 5))
    plt.plot(y_true_list, 'r+', label='real data')
    plt.plot(y_pred_list, 'b*', label='pred data')
    plt.title('loss={}'.format(loss))
    plt.legend()
    plt.savefig('pre_temperature_RNN_3_test.jpg', dpi=256)
    plt.close()

    print(len(y_true_list))
    print(len(y_pred_list))

    mse(y_true_list, y_pred_list)
    rmse(y_true_list, y_pred_list)
    evs(y_true_list, y_pred_list)

if __name__ == '__main__':
    start_time = time.time()
    model = tm_RNN.TemperatureModel_RNN()
    # 加载数据
    test_loader = DataLoader(td.TemperatureDataset("C:\\Users\\ziting\\Desktop\\yanzheng\\E_weather\\weather\\meant_1901to2000.csv", mode="test", testset_ratio=1),
                             batch_size=64, shuffle=False)
    criterion = nn.MSELoss()
    # 加载模型

    # model = torch.load("CPU/temperature_model_RNN.pth")
    model = torch.load("RNN/GPU/3/temperature_model_RNN_with_GPU.pth", map_location=torch.device('cpu'))
    # 测试
    test(model, test_loader, criterion)
    print("总耗时:{}min".format((time.time() - start_time) / 60))
