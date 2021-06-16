#@Author:pakchungy
#@Date:2021/5/27
#@Time:0:23
#@Project_name:finalproject

import time

import torch
import torch.nn as nn
from DNN import temperature_model_DNN as tm
import temperature_dataset as td
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np


def train(model, train_loader, criterion, optimizer, epoch):
    loss_list = []
    for i in range(epoch):
        epoch_start_time = time.time()
        print("epoch[{}/{}]".format(i, epoch))
        for index, (x, y) in enumerate(train_loader, 0):
            x = x.to(device)
            y = y.to(device)
            out = model(x).squeeze(-1)
            optimizer.zero_grad()
            # out = out.view(17, 64)
            loss = criterion(out, y)
            loss.backward()
            optimizer.step()
            loss_list.append(loss.item())
        print("  用时:{}min".format((time.time() - epoch_start_time) / 60))
    # 画出损失图像
    plt.figure(figsize=(10, 5))
    plt.plot(loss_list, "b")
    plt.title('loss')
    plt.savefig('Temperature_Train_loss_DNN_with_GPU.jpg', dpi=256)
    plt.close()


def test(model, test_loader):
    y_pred_list = []
    y_true_list = []
    for i, (x, y) in enumerate(test_loader, 0):
        x = x.to(device)
        y = y.to(device)
        # 计算预测值
        y_pred = model(x)
        y_pred = y_pred.detach().cpu().numpy().reshape(y_pred.shape[0])
        y = y.detach().cpu().numpy().reshape(y.shape[0])
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
    plt.savefig('pre_temperature_DNN_with_GPU.jpg', dpi=256)
    plt.close()


if __name__ == '__main__':
    start_time = time.time()

    train_loader = DataLoader(td.TemperatureDataset("../../meant_1901to2000.csv", mode="train", testset_ratio=0.1), batch_size=64, shuffle=True)
    test_loader = DataLoader(td.TemperatureDataset("../../meant_1901to2000.csv", mode="test", testset_ratio=0.1), batch_size=64, shuffle=False)

    device = torch.device('cuda:0')
    model = tm.TemperatureModel_DNN().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-6)
    criterion = nn.MSELoss()
    # criterion = nn.KLDivLoss()
    epoch = 100

    # 训练模型
    train(model, train_loader, criterion, optimizer, epoch)
    # 保存模型
    print("训练完成")
    torch.save(model, "temperature_model_DNN_with_GPU.pth")
    print("模型已保存")

    # 测试模型
    model = torch.load("temperature_model_DNN_with_GPU.pth")
    test(model, test_loader)
    print("总耗时:{}min".format((time.time() - start_time) / 60))
