import gradient_descent as GD
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  

str_formula = "y = ax + b"
data_name = "data.txt"

ab, support_3D = GD.GD(data_name, str_formula)
a = ab[0]
b = ab[1]

pformula = "y = " + str(round(a, 5)) +"x + " + str(round(b, 5))

data = GD.get_data('data.txt')
print(data)
print(pformula)
x_train = []
y_train = []

for i in data:
    x_train.append(i[0])
    y_train.append(i[1])



find_y = []
for x in x_train:
    find_y.append(a*x+b)

figg, ax1 = plt.subplots()
# Plot the data points
ax1.scatter(x_train, y_train, marker='x', c='r', label='Raw data')
# Set the title
ax1.set_title("Graph 1")
# Set the y-axis label
ax1.set_ylabel('y')
# Set the x-axis label
ax1.set_xlabel('x')

ax1.plot(x_train, find_y, c='b',label='Trendline')

ax1.legend()

fig = plt.figure()
ax2 = fig.add_subplot(projection='3d')

print("3D data:")
print(support_3D)

ax2.scatter(support_3D[:, 0], support_3D[:, 1], support_3D[:, 2])
 
 
# 添加坐标轴(顺序是Z, Y, X)
ax2.set_title("Graph 2")
ax2.set_xlabel('a', fontdict={'size': 12, 'color': 'black'})
ax2.set_ylabel('b', fontdict={'size': 12, 'color': 'black'})
ax2.set_zlabel('cost', fontdict={'size': 12, 'color': 'black'})
plt.show()
