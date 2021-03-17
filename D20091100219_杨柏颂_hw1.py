# editor:Pakchung Y
# date:2021-02-25


import numpy as np #导入numpy
import numpy.matlib as ml
#################################
#课后作业1-3
#建立一个一维数组a初始化为[4,5,6]
a = np.array([4,5,6])

print("a的类型：", type(a)) #输出a的类型(type)
# print("a的类型：", a.dtype) #输出a的类型(a.dtype)？？？
print("a的各维度的大小：", a.shape)  #输出a的各维度的大小
print("a的第一个元素：", a[0]) #输出a的第一个元素(值为4)

##################################
#建立一个二维数组b，初始化为[[4,5,6],[1,2,3]]
b = np.array([[4,5,6],[1,2,3]])

print("b的各维度的大小：", np.shape(b)) #输出b的各维度的大小
print("b(0,0):", b[0,0]) #输出b(0,0)
print("b(0,1):", b[0,1]) #输出b(0,1)
print("b(1,1):", b[1,1]) #输出b(1,1)

##################################
#课后作业4-5
#新建矩阵
#建立一个全0矩阵a, 大小为3x3; 类型为整型（提示: dtype = int）
a = np.zeros((3,3), dtype=int, order='C')
print("矩阵a:\n", a)

#建立一个全1矩阵b,大小为4x5
b = np.ones((4,5), dtype=float, order='c')
print("矩阵b:\n", b)

#建立一个单位矩阵c ,大小为4x4
c = np.identity(4,dtype=float)
print("矩阵c:\n", c)

#生成一个随机数矩阵d,大小 为3x2
d = np.random.random((3,2))
print("矩阵d:\n", d)

#建立一个数组a,(值为[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] )
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("矩阵a:\n", a) #打印a
print("a[2,3]:\n", a[2,3],"\na[0,0]:\n",a[0,0]) #输出下标为(2,3),(0,0) 这两个数组元素的值

####################################
#课后作业6-7
#把上一题的a数组的0到1行2到3列,放到b里面
b = a[0:2, 2:4] #切片操作“要头不要尾”
print("矩阵b:\n", b) #输出b
print("b[0,0]:\n", b[0,0]) #输出b[0,0]

#把第上题中数组a的最后两行所有元素放到c中
c = a[1:3, :]
print("矩阵c:\n",c) #输出c
print("c[1,-1]:\n",c[1,-1]) #输出c中第一行的最后一个元素

#####################################
#课后作业8-10
#建立数组a,初始化a为[[1, 2], [3, 4], [5, 6]]，
#输出(0,0)(1,1)(2,0)这三个元素
a = np.array([[1,2],[3,4],[5,6]])
print(a[[0,1,2],[0,1,0]])

#建立矩阵a ,初始化为[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]，
#输出(0,0),(1,2),(2,0),(3,1)元素
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])

#####################################
#课后作业11-12
#执行x = np.array([1, 2])，然后输出x 的数据类型
x = np.array([1,2])
print(x.dtype)

#执行x = np.array([1.0, 2.0]),然后输出x的数据类类型
x = np.array([1.0,2.0])
print(x.dtype)

#######################################
#课后作业13-18
#已知
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print("x+y:\n",x+y)
print("np.add(x,y)\n",np.add(x,y))

print("x-y:\n",x-y)
print("np.subtract(x,y):\n",np.subtract(x,y))

print("x*y:\n",x*y)
print("np.multiply(x,y):\n",np.multiply(x,y))
print("np.dot(x,y):\n",np.dot(x,y))

print("x/y:\n",x/y)
print("np.divide(x,y):\n",np.divide(x,y))

print("np.sqrt(x):\n",np.sqrt(x))

print("x.dot(y):\n",x.dot(y))
print("np.dot(x,y):\n",np.dot(x,y))

#######################################
#课后作业19-20
#已知
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

print("np.sum(x):\n",np.sum(x))
print("np.sum(x, axis = 0):\n",np.sum(x, axis = 0))
print("np.sum(x, axis = 1):\n",np.sum(x, axis = 1))

print("np.mean(x):\n",np.mean(x))
print("np.mean(x, axis = 0):\n",np.mean(x, axis = 0))
print("np.mean(x, axis = 1):\n",np.mean(x, axis = 1))

#######################################
#课后作业21-23
#已知
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

print("转置:\n",x.T)

print("np.exp(x):\n",np.exp(x))

print("np.argmax(x):\n",np.argmax(x))
print("np.argmax(x, axis = 0):\n",np.argmax(x, axis = 0))
print("np.argmax(x, axis = 1):\n",np.argmax(x, axis = 1))

########################################
#课后作业24-25
###array的画图
#画图，y=x*x 其中x = np.arange(0, 100, 0.1)
x = np.arange(0, 100, 0.1)
y = x * x
from matplotlib import pyplot as plt #引入matplotlib库
plt.title("y = x * x")  #题目
plt.xlabel("x axis caption")    #x坐标轴名称
plt.ylabel("y axis caption")    #y坐标轴名称
plt.plot(x,y)
plt.show()

#画图. 画正弦函数和余弦函数，x = np.arange(0, 3 * np.pi, 0.1)
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)   #正弦
plt.title("sin wave form")  #题目
plt.plot(x, y)
plt.show()

x = np.arange(0, 3 * np.pi, 0.1)
y = np.cos(x)   #余弦
plt.title("cos wave form")  #题目
plt.plot(x, y)
plt.show()