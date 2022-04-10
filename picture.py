import numpy as np
import matplotlib.pyplot as plt



plt.rcParams['font.family'] = "Times New Roman"

# 构造数据
labels = ['30000', '100000', '300000']
data_a = [0.792, 0.891, 0.924]
data_b = [0.784, 0.873, 0.907]
data_c = [0.787, 0.882, 0.915]

x = np.arange(len(labels))
width = .20

plt.rcParams['font.family'] = "Times New Roman"
# plots
fig, ax = plt.subplots(figsize=(5, 3), dpi=200)
bar_a = ax.bar(x - width / 2, data_a, width = 0.2, label='Precision', color='#130074', ec='black', lw=.5,zorder=200)
bar_b = ax.bar(x + width / 2, data_b, width = 0.2, label='Recall', color='#CB181B', ec='black', lw=.5,zorder=200)
bar_c = ax.bar(x+width*3/2, data_c,width,label='F1-score',color='#008B45',ec='black',lw=.5,zorder=200)

# 定制化设计
ax.tick_params(axis='x', direction='in', bottom=False)
ax.tick_params(axis='y', direction='out', labelsize=8, length=3)
ax.set_xticks(x + .1)
ax.set_xticklabels(labels, size=10)
ax.set_ylim(bottom=0.5, top=1)
ax.set_yticks(np.arange(0.5, 1.05, step=0.05))

for spine in ['top', 'right']:
    ax.spines[spine].set_color('none')

ax.legend(fontsize=7, frameon=False)

text_font = {'size': '14', 'weight': 'bold', 'color': 'black'}
# ax.text(.03, .93, "(a)", transform=ax.transAxes, fontdict=text_font, zorder=4)
ax.text(.49, -.08, '\nData set size', transform=ax.transAxes,
         ha='center', va='center', fontsize=10, color='black',  family='Times New Roman')
# bar_c = ax.bar(x+width*3/2, data_c,width,label='category_C',color='#008B45',ec='black',lw=.5,zorder=100)
plt.grid(axis="y",zorder=0,ls='--')

#定义函数来显示柱状上的数值
for rect in bar_a:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2.-0.098, 1.03*height-0.018, '%s' % float(height),fontsize=7)

#定义函数来显示柱状上的数值
for rect in bar_b:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2.-0.098, 1.03*height-0.018, '%s' % float(height),fontsize=7)


#定义函数来显示柱状上的数值
for rect in bar_c:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2.-0.098, 1.03*height-0.018, '%s' % float(height),fontsize=7)
# 添加图例



plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0)
plt.savefig(r'./pic.png',width=5,height=3,
            dpi=900,bbox_inches='tight')
plt.show()

