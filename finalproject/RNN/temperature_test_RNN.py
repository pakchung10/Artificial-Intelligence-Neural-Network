#@Author:pakchungy
#@Date:2021/5/27
#@Time:0:23
#@Project_name:finalproject

import time

import torch
import torch.nn as nn
from RNN import temperature_model_RNN as tm
import temperature_dataset as td
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np


def test(model, test_loader):
    y_pred_list = []
    y_true_list = []
    for i, (x, y) in enumerate(test_loader, 0):
        # 计算预测值
        y_pred = model(x)
        y_pred = y_pred.detach().numpy().reshape(y_pred.shape[0])
        y = y.detach().numpy().reshape(y.shape[0])
        if i == 0:
            y_pred_list = y_pred
            y_true_list = y
        else:
            y_pred_list = np.concatenate((y_pred_list, y_pred))
            y_true_list = np.concatenate((y_true_list, y))
    # 画图
    plt.figure(figsize=(10, 5))
    plt.plot(y_true_list, 'r+', label='real data')
    plt.plot(y_pred_list, 'b*', label='pred data')
    plt.legend()
    plt.savefig('pre_temperature_RNN.jpg', dpi=256)
    plt.close()


if __name__ == '__main__':
    start_time = time.time()
    model = tm.TemperatureModel_RNN()
    # 加载数据
    test_loader = DataLoader(td.TemperatureDataset("../meant_1901to2000.csv", mode="test", testset_ratio=0.1),
                             batch_size=64, shuffle=False)

    # 加载模型

    # model = torch.load("CPU/temperature_model_RNN.pth")
    model = torch.load("GPU/3/temperature_model_RNN_with_GPU.pth", map_location=torch.device('cpu'))
    # 测试
    test(model, test_loader)
    print("总耗时:{}min".format((time.time() - start_time) / 60))
