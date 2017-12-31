import random
#import numpy as np
import matplotlib.pyplot as plt
def randpath(n,time):#n number
    initial=[]
    x=[]
    bb=[]
    for i in range(1,2*n):
        x.append(-n+i)
        bb.append(0)
        if i==n:
           initial.append(n)
        else:
           initial.append(0)
    for j in range(n):
        X=[]
        X.append(0) 
        for k in range(time):   
            c=random.random()
            if c<=0.5:
               X.append(X[-1]+1)
            if c>0.5:
               X.append(X[-1]-1)
        ct=x.index(X[-1])#一个walker最后停止的坐标
        bb[ct]=bb[ct]+1#+1
    if time==0:
       return x,initial
    else:
       return x,bb
plt.figure(figsize=(12,7))
ax1=plt.subplot(811)
ax2=plt.subplot(812)
ax3=plt.subplot(813)
ax4=plt.subplot(814)
ax5=plt.subplot(815)
ax6=plt.subplot(816)
ax7=plt.subplot(817)
ax8=plt.subplot(818)
ax1.set_title('Diffusion in one dimension')
plt.sca(ax1)
a,b=randpath(1000,0)
plt.plot(a,b)
plt.sca(ax2)
a,b=randpath(1000,10)
plt.plot(a,b)
plt.sca(ax3)
a,b=randpath(1000,100)
plt.plot(a,b)
plt.sca(ax4)
a,b=randpath(1000,500)
plt.plot(a,b)
plt.sca(ax5)
a,b=randpath(1000,1000)
plt.plot(a,b)
plt.sca(ax6)
a,b=randpath(1000,2000)
plt.plot(a,b)
plt.sca(ax7)
a,b=randpath(1000,4000)
plt.plot(a,b)
plt.sca(ax8)
a,b=randpath(1000,8000)
plt.plot(a,b)

plt.show()         
        