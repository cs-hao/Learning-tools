import matplotlib.pyplot as plt   # 导入绘图模块
import numpy as np
font = {'family' : 'Times New Roman',
'weight' : 'light',
'size'   : 12,
}
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_xlabel("FLOPs (G)",fontdict=font)
ax.set_ylabel("AP",fontdict=font)
# ax.set_ylim(32, 34.5)
# ax.set_yticks([32,32.5,33,33.5,34,34.5])
ax.set_xlim([1,3.5])
ax.set_xticks([0,0.5, 1, 1.5, 2.0, 2.5, 3.0, 3.5])
# ax.tick_params(axis='x',width=0,colors='black',labelsize=8)
# ax.tick_params(axis='y',width=0,colors='black',labelsize=8)
ax.tick_params(bottom=True,left=True,colors='black',labelsize=8,direction='in') # 不显示刻度尺

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
 [0.53196569, 0.4624008,  0.86573696],
 # [0.39634342, 0.81036955, 0.84365579],
 [0.62736658, 0.10176231, 0.6875806 ],
 [0.24182245, 0.98788236, 0.26682556],
 # [0.12897025, 0.92566105, 0.75532276]]
 [1,0,0]]
# print(color)
# color = ['#00FFFF','black','black','black','black','black','black','black','black','red']
# size = np.random.randint(0,1000,1000) # 设置每一个点的大小随机生成
size=100
flops = [0.2, 0.3, 1.1, 1.1, 3.0, 3.0, 2.6, 2.6]
ap = [64.8, 67.2, 64.5, 65.9, 68.3, 69.3, 68.4, 71.7]
txt = ['Lite-HRNet-18','Lite-HRNet-30','LPN50','ODKD-LPN50','4-stage Hourglass','ODKD-4-stage Hourglass','HRNet-W16','ODKD-HRNet-W16']

loc_params = [0.2+0.1, 0.3+0.1, 1.1+0.1, 1.1+0.1, 2.8+0.1, 2.55+0.1, 2.0+0.1, 1.8+0.1]
loc_ap = [64.7, 67.1, 64.4, 65.8, 68.0, 69.5, 68.3, 71.6]
loc_color = ['black','black','black','black','black','black','black','black','black','black','red']
for i in range(len(txt)):
	if i == 0 or i == 1:
		plt.plot(flops[i], ap[i],"o",color=color[0], markersize=10)
	elif i % 2 == 0:
		plt.plot(flops[i], ap[i],"o",color=color[i], markersize=10)
	else:
		plt.plot(flops[i], ap[i],"*",color='red', markersize=10)
# plt.scatter(params, psnr, color = color, s=size, marker='8')
# font2 = {"fontsize":12,"family":"Times New Roman", "style":"normal", "weight":"normal"}
for i in range(len(txt)):
	plt.text(loc_params[i], loc_ap[i], txt[i], color = loc_color[0], fontsize=8, family =  'Times New Roman')

# plt.grid(linestyle='--')#显示网格线

plt.savefig('flops.png',dpi=1000,bbox_inches = 'tight')
plt.show()
