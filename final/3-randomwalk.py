import random
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
def randpath(T):
    x=[0]
    y=[0]
    z=[0]
    t=[0]
    r2ave=[0]*T
    for i in range(T):
        ruler=random.randint(1,3)
        if ruler==1:
            c=random.random()
            t.append(i+1)
            if c<=0.5:
                x.append(x[-1]+1)        
            else:
                x.append(x[-1]-1)
            y.append(y[-1])
            z.append(z[-1])
        if ruler==2:
            c=random.random()
            t.append(i+1)
            if c<=0.5:
                y.append(y[-1]+1)
            else:
                y.append(y[-1]-1)
            x.append(x[-1])
            z.append(z[-1])
        if ruler==3:
            c=random.random()
            t.append(i+1)
            if c<=0.5:
                z.append(y[-1]+1)
            else:
                z.append(y[-1]-1)
            x.append(x[-1])
            y.append(z[-1])    
        r2ave[i]=r2ave[i]+(x[-1]**2+y[-1]**2+z[-1]**2)   
    return x,y,z,t,r2ave
x,y,z,t,r2ave=randpath(500)
x1,y1,z1,t1,r2ave1=randpath(500)
fig = plt.figure(figsize=(9,7))
ax1=fig.gca(projection='3d')
ax1.plot(x1,y1,z1,color='black')
ax1.plot(x,y,z,color='blue')
ax1.set_title('random walk in 3 dimension')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
#ax1.view_init(30,0)


#-----------
r2ave=[0]*100
for i in range(5000):
    x1,y1,z1,t1,r2ave1=randpath(100)
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

    