# Final-Project-of-AI-and-NN

人工智能与神经网络的期末项目留档

- 根目录目录存放数据，temperature_dataset.py是数据导入相关脚本
- DNN、RNN目录分别存放对应模型脚本
- CPU、GPU目录分别存放对应的训练脚本和训练出来的产物(损失图像、预测数值图像、模型文件等)

# 目前效果最好的模型

## DNN

- 多个全连接层叠加，越多效果越好，但训练时间倍增，目前建议最高10层，有GPU可以酌情加深
- 损失函数MESloss
- 优化器为torch.optim.Adam
- lr=1e-8
- epoch=400

## RNN

- 输入60，隐藏层输出20，隐藏层数3层，dropout=0.3
- 最后使用全连接层回归
- 损失函数MESloss
- 优化器为torch.optim.Adam
- lr=1e-8
- epoch=1000

## 目前的问题

- RNN效果不佳，需要继续探索更优的模型结构
- 无论是RNN还是DNN，激活函数都只能起副作用，原因暂时不明
- 学习率需要很小，但不能太小，过大的学习率会导致梯度爆炸，过小的学习率导致跳不出鞍点，目前试出最优学习率为1e-8