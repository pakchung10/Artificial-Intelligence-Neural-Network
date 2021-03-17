# editor:Pakchung Y
# date:2021-03-11

import pandas as pd
import numpy as np

# 主函数
def main():
    T_list = [200, 50, 20, 5]  # 迭代次数
    num = 80
    file_path = "D://PycharmProjects//lesson_neuralnetwork//data_x1x2x3y.csv"
    print("文件路径：" + file_path)
    list_x = []
    list_y = []
    data_set = pd.read_csv(file_path, delimiter=',',
                           dtype={'x1': np.int64, 'x2': np.int64, 'x3': np.int64, 'y': np.int64})

    # data_set类型<class 'pandas.core.frame.DataFrame'>，（100, 4）
    data_set_array = np.array(data_set)
    data_set_list = data_set_array.tolist()
    # print(data_set_list) #data_set的列表形式
    list_x_array = []
    for i in range(len(data_set_list)):
        list_x.append(data_set_list[i][0:3])
        list_y.append(data_set_list[i][-1])
    for j in range(len(list_x)):
        list_x[j].append(1)
        list_x_array.append(np.array(list_x[j], dtype=np.int64).reshape(4, 1))
        # print(list_x_array[:num])
        # print(list_y[:num])
        # print(T_list)
    # data_set = np.loadtxt("D:/PycharmProjects/lesson_neuralnetwork/data_x1x2x3y.csv", dtype=np.int64, delimiter=',',
    #                       skiprows=1)
    #
    # list_x_array = []
    # list_y = []
    # for data in data_set:
    #     list_x_array.append(np.r_[data[0:3], [1]].reshape(4, 1))
    #     list_y.append(data[3])

    for T in T_list:
        my_perceptron(list_x_array[:num], list_y[:num], T)
        w_ = my_perceptron(list_x_array[:num], list_y[:num], T)
        # print(w_)
        print("准确率:", count_accuracy(w_, list_x_array[-num:], list_y[-num:]))

# 感知器
def my_perceptron(x_list, y_list, T):
    # x<--x1,x2,x3,y<-y,T迭代次数
    w_ = np.array([0, 0, 0, 0]).reshape(4, 1)
    # 权重向量(w1,w2,w3,w0)初始化为零,w1，w2,w3为权重，w0为偏置b
    t = 0
    while t < T:
        for x, y in zip(x_list, y_list):
            # if np.dot(w_.T,x*y) <= 0:
            # print(np.dot(w_.T, x)[0][0], y, np.dot(w_.T, x)[0][0] * y)
            # print(type(x[0][0]))
            if np.dot(w_.T, x)[0][0] * y <= 0:
                # if np.dot(w_.T,np.dot(x,y)) <= 0:
                w_ += x * y
            t += 1
            if t >= T:
                break
        if t >= T:
            break
    # print(w_)
    return w_

# 计算正确率
def count_accuracy(w, x_list, y_list):
    correct = 0
    for x, y in zip(x_list, y_list):
        # 结果同号，说明预测正确
        # print(np.dot(w.T, x)[0][0], y, np.dot(w.T, x)[0][0] * y)
        if np.dot(w.T, x)[0] * y > 0:
            correct += 1
    return correct / len(x_list)

if __name__ == "__main__":
    main()
