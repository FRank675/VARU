import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 6])
y = np.array([0, 100])

plt.subplot(2, 2, 1)
plt.plot(x,y)
plt.title("plot 1")

#plot 2:
x = np.array([1, 2, 3, 4,5])
y = np.array([1, 4, 9, 16,5])

plt.subplot(2, 2, 2)
plt.plot(x,y,marker = 'o')
plt.title("plot 2")

#plot 3:
x = np.array([1, 2, 3, 4])
y = np.array([3, 5, 7, 9])

plt.subplot(2, 2, 3)
plt.pie(x,labels=y, # 设置饼图标签
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], )
plt.title("plot 3")

#plot 4:
x = np.array([1, 2, 3, 4])
y = np.array([4, 5, 6, 7])

plt.subplot(2, 2, 4)
plt.bar(x,y)
plt.title("plot 4")

plt.suptitle("RUNOOB subplot Test")
plt.show()