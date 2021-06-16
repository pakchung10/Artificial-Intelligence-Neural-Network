#@Author:pakchungy
#@Date:2021/5/27
#@Time:0:23
#@Project_name:finalproject

import torch.nn as nn
import torch

class TemperatureModel_DNN(nn.Module):
    def __init__(self):
        super(TemperatureModel_DNN, self).__init__()
        self.linear = nn.Sequential(
            nn.Linear(60, 100),
            nn.Linear(100, 200),
            nn.Linear(200, 500),
            nn.Linear(500, 1000),
            nn.Linear(1000, 400),
            nn.Linear(400, 200),
            nn.Linear(200, 80),
            nn.Linear(80, 40),
            nn.Linear(40, 20),
            nn.Linear(20, 1),
        )
        #lr=1e-6
        self.sigmoid = nn.Sigmoid()
    def forward(self, x):
        x = self.linear(x)
        x = self.sigmoid(x)
        return x