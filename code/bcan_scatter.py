import matplotlib.pyplot as plt   # 导入绘图模块
import numpy as np
font = {'family' : 'Times New Roman',
'weight' : 'light',
'size'   : 12,
}
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_xlabel("Number of Parameters(k)",fontdict=font)
ax.set_ylabel("PSNR(dB)",fontdict=font)
# ax.set_ylim(32, 34.5)
# ax.set_yticks([32,32.5,33,33.5,34,34.5])
ax.set_xlim([-1000,45000])
ax.set_xticks([0,5000,10000,15000,20000,25000,30000,35000,40000,45000])
# ax.tick_params(axis='x',width=0,colors='black',labelsize=8)
# ax.tick_params(axis='y',width=0,colors='black',labelsize=8)
ax.tick_params(bottom=False,left=False,colors='black',labelsize=8) # 不显示刻度尺

labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
[label.set_fontsize(10) for label in labels]

ax.spines['left'].set_color('gray')
ax.spines['right'].set_color('gray')
ax.spines['top'].set_color('gray')
ax.spines['bottom'].set_color('gray')

# color = np.random.random(33).reshape((11,3))  # 设置每一个点的颜色随机生成
color = [[0.37787616,0.75083482,0.43136594],
 [0.72003379, 0.27885057, 0.58196171],
 [0.97396498, 0.55454179, 0.30583052],
 [0.61723963, 0.77635772, 0.73766149],
 [0.05117207, 0.80795008, 0.72134145],
 [0.01763648, 0.45818955, 0.25539535],
 [0.39634342, 0.81036955, 0.84365579],
 [0.62736658, 0.10176231, 0.6875806 ],
 [0.24182245, 0.98788236, 0.26682556],
 [0.53196569, 0.4624008,  0.86573696],
 # [0.12897025, 0.92566105, 0.75532276]]
 [1,0,0]]
# print(color)
# color = ['#00FFFF','black','black','black','black','black','black','black','black','red']
# size = np.random.randint(0,1000,1000) # 设置每一个点的大小随机生成
size=100
params = [57, 12, 665, 1774, 677, 1592,43000,5956,22100,5930,6103]
psnr = [32.45,32.76,33.03,33.06,33.28,33.52,33.92,33.85,34.01,33.74,33.98]
txt = ['SRCNN','FSRCNN','VDSR','DRCN','MemNet','CARN','EDSR','DBPN','RDN','MSRN','Ours']

loc_params = [1000+57, 1000+12, 665-500, 1000+1774, 1000+677, 1000+1592, 43000-1000,1000+5956,22100-1000,1000+5930,1000+6103]
loc_psnr = [32.45,32.76,33.03-0.15,33.06,33.28,33.52,33.92-0.15,33.85,34.01-0.15,33.74,33.98]
loc_color = ['black','black','black','black','black','black','black','black','black','black','red']
for i in range(len(txt)):
	plt.plot(params[i], psnr[i],"o",color=color[i], markersize=10)

for i in range(len(txt)):
	plt.text(loc_params[i], loc_psnr[i], txt[i], family='Times New Roman', color = loc_color[i],fontsize=12)
plt.grid(linestyle='--')#显示网格线
plt.savefig('scatterdiagramx2.pdf')
plt.show()