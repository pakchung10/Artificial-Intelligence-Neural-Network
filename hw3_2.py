# editor:Pakchung Y
# date:2021-03-11

import random as rd

# 感知器
def my_perceptron(train_list, label_list, length):
    data = []
    label = label_list
    t = 0
    w_ = [0, 0, 0]
    for i in range(len(train_list)):
        data.append(train_list[i][0:3])
    while True:
        corret = 0
        for index in range(len(train_list)):
            # print(data[index][0])
            # print(data[index][1])
            print("\t")
            print("第{}次迭代".format(t))
            CheckPoint = w_[0] * data[(index+1)%3][0] + w_[1] * data[(index+1)%3][1] + w_[-1]
            print("测试值：", CheckPoint)
            print("实际值：", label[(index+1)%3])
            if CheckPoint * label[(index+1)%3] <= 0:
                print("为误分点")
                w_ = [w_[0] + data[(index+1)%3][0] * label[(index+1)%3],
                      w_[1] + data[(index+1)%3][1] * label[(index+1)%3], w_[2] + label[(index+1)%3]]
                print("更新权重w_", w_)
            else:
                print("不为误分点")
                print("保持权重w_", w_)
                corret += 1
            t += 1
        if corret >= len(data):
            break
    return w_


# 主函数
def main():
    train_set = [
        [3, 3, 1], [4, 3, 1], [1, 1, 1]
    ]
    label_set = [1, 1, -1]
    list_length = len(train_set)
    # for i in range(len(train_set)):
    #     train_set[i].append(label_set[i])
    print("训练集：", train_set)
    print(my_perceptron(train_set, label_set, list_length))


if __name__ == "__main__":
    main()