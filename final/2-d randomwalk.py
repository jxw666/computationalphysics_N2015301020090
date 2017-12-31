import random
import numpy as np
import matplotlib.pyplot as plt
import math
def randpath(T):
    x=[0]
    y=[0]
    t=[0]
    r2ave=[0]*T
    for i in range(T):
        ruler=random.randint(1,2)
        if ruler==1:
            c=random.random()
            t.append(i+1)
            if c<=0.5:
                x.append(x[-1]+1)        
            else:
                x.append(x[-1]-1)
            y.append(y[-1])
        if ruler==2:
            c=random.random()
            t.append(i+1)
            if c<=0.5:
                y.append(y[-1]+1)
            else:
                y.append(y[-1]-1)
            x.append(x[-1])
        r2ave[i]=r2ave[i]+(x[-1]**2+y[-1]**2)   
    return x,y,t,r2ave
x,y,t,r2ave=randpath(100)
x1,y1,t1,r2ave1=randpath(100)
plt.plot(x,y,color='black')
plt.plot(x1,y1,color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('random walk in 2 dimension')
#-----------
r2ave=[0]*100
for i in range(5000):
    x1,y1,t1,r2ave1=randpath(100)
    for j in range(len(x1)-1):
        r2ave[j]=r2ave[j]+r2ave1[j]/5000
plt.figure(figsize=(10,5))
plt.grid()
t0=[]
for i in range(100):
    t0.append(i+1)
plt.plot(t0,r2ave,'o',ms=3)
plt.xlabel('time(step number)')
plt.ylabel('<r2>')
plt.title('random walk in one dimension')
#plt.text(10,80,'<x2> versus time')
k,b=np.polyfit(t0,r2ave,1)#多项式拟合
ideal=[]
for i in range(100):
    ideal.append(k*(i+1)+b)
plt.plot(t0,ideal,color='red')
print(k,b)

    
