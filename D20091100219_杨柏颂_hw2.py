# editor:Pakchung Y
# date:2021-02-25

import numpy as np
from matplotlib import pyplot as plt

times = 100  # 迭代次数
alpha = 0.2  # 步长
# list_x = []
# list_y = []
#原函数
def f(x):
    y = np.sqrt((5 + 4*np.cos(x)) / 4) + np.sqrt((5 - 4*np.cos(x)) / 4)
    return y

#求导函数
def fd(x):
    y = 0.5 * np.sin(x) * (pow(((5 - 4 * np.cos(x)) / 4), -0.5) - pow((5 + 4 * np.cos(x)) / 4, -0.5))
    return y

#梯度下降算法
def gradient_decs(n, m): #参数n为迭代执行次数
    x1 = m #初始化x
    list_x.append(x1)
    y1 = f(x1)
    list_y.append(y1)
    for i in  range(n):
        fd_x1 = fd(x1)
        x1 = x1 - alpha * fd_x1
        list_x.append(x1)
        y2 = f(x1)
        list_y.append(y2)
    return list_x, list_y

for i in range(1,5):
    list_x = []
    list_y = []
    gradient_decs(100, i)
    # fig = plt.figure()
    # ax = fig.add_subplot(2, 2, i)
    ax = plt.subplot(2, 2, i)
    ax.set_title("x0={}".format(i))
    plt.plot(range(101) , list_x, color="red", label = "x")
    plt.plot(range(101) , list_y, color="blue", label = "y")
    # plt.plot(list_x , list_y, color="black")
    # plt.plot(np.arange(-5,5,0.001) , f(np.arange(-5,5,0.001)), color="pink")
    plt.legend()
plt.suptitle("学习率alpha={},迭代次数t={}".format(alpha,times), fontproperties="KaiTi", fontsize=20)
plt.show()
plt.plot(np.arange(-5, 5, 0.001), f(np.arange(-5, 5, 0.001)))
plt.show()