#@Author:pakchungy
#@Date:2021/5/27
#@Time:0:23
#@Project_name:finalproject

import torch
import torch.nn as nn


class TemperatureModel_RNN(nn.Module):
    def __init__(self):
        super(TemperatureModel_RNN, self).__init__()
        self.rnn1 = nn.RNN(input_size=60, hidden_size=1500, num_layers=1, dropout=0.5, batch_first=False)
        self.rnn2 = nn.RNN(input_size=1500, hidden_size=3000, num_layers=1, dropout=0.5, batch_first=False)
        self.rnn3 = nn.RNN(input_size=3000, hidden_size=20, num_layers=1, dropout=0.5,batch_first=False)

        #lr = 1e-6
        self.linear = nn.Sequential(
            nn.Linear(20, 1),
        )
        # self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        output = self.rnn1(x)

        output = self.rnn2(output[0])
        output = self.rnn3(output[0])
        # output = self.sigmoid(output[0])
        # output = self.rnn1(output[0])
        # output = self.sigmoid(output[0])
        output = self.linear(output[0])
        return output
