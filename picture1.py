import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = "Times New Roman"

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('VARU', 'HELAD', 'SVM', 'IF', 'RBM', 'SAE', 'GMM')
xP = (0,0.2,0.4,0.6,0.8,1)
y_pos = np.arange(len(people))
performance = (0.983,0.932,0.781,0.986,1.000,0.988,0.776)
performance2 = (0.968,0.956,0.436,0.963,0.513,0.954,0.683)
performance3 = (0.975,0.944,0.560,0.974,0.678,0.970,0.726)

error = np.random.rand(len(people))


total_width, n = 0.6, 2
width = total_width / n
y_pos=y_pos - (total_width - width) / 2

b=ax.barh(y_pos, performance, align='center',
        color='#130074', ecolor='black',height=0.3,label='Precision')
#添加数据标签

for rect in b:
    w=rect.get_width()
    ax.text(w,rect.get_y()+rect.get_height()/2,'%s'%w,ha='left',va='center',fontsize=14)

b=ax.barh(y_pos+width, performance2, align='center',
        color='#CB181B', ecolor='black',height=0.3,label='Recall')
#添加数据标签
for rect in b:
    w=rect.get_width()
    ax.text(w,rect.get_y()+rect.get_height()/2,'%s'%w,ha='left',va='center',fontsize=14)

b=ax.barh(y_pos+width+width, performance3, align='center',
        color='#008B45', ecolor='black',height=0.3,label='F1-score')
#添加数据标签
for rect in b:
    w=rect.get_width()
    ax.text(w,rect.get_y()+rect.get_height()/2,'%s'%w,ha='left',va='center',fontsize=14)
ax.set_yticks(y_pos+width/2.0)
ax.set_yticklabels(people,size=18)
ax.invert_yaxis()  # labels read top-to-bottom

ax.set_xticklabels(xP,size=18)

ax.set_xlabel('Performance',fontsize=20)
ax.legend(fontsize=17, frameon=False)

# ax.set_title('How fast do you want to go today?')
plt.legend(loc= "4", prop={'size': 13})
plt.show()
print(y_pos+3)