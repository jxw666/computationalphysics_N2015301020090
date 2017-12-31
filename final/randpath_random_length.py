import random
import numpy as np
import matplotlib.pyplot as plt
def randpath(T):
    x=[0]
    t=[0]
    x2ave=[0]*T
    for i in range(T):
        t.append(i+1)
        x.append(x[-1]+random.uniform(-1,1))
        x2ave[i]=x2ave[i]+x[-1]**2
    return x,t,x2ave
x,t,x2ave=randpath(100)
x1,t1,x2ave1=randpath(100)
fig = plt.figure(figsize=(10, 5))
plt.plot(t,x,'o',ms=4,color='red')
plt.plot(t1,x1,'o',ms=4,color='blue')
plt.xlabel('time(step number)')
plt.ylabel('X')
plt.title('random walk in one dimension')


#----------
average=[0]*101
for i in range(5000):
    x1,t1,x2ave1=randpath(100)
    for j in range(len(x1)):
        average[j]=average[j]+x1[j]/5000
plt.figure(figsize=(10,5))
plt.ylim(-0.2,0.2)
plt.grid()
plt.plot(t1,average)
plt.xlabel('time(step number)')
plt.ylabel('<x>')
plt.title('random walk in one dimension')
#plt.text(0,0.15,'<x> versus time')
#-----------\
x2ave=[0]*100
for i in range(5000):
    x1,t1,x2ave1=randpath(100)
    for j in range(len(x1)-1):
        x2ave[j]=x2ave[j]+x2ave1[j]/5000
plt.figure(figsize=(10,5))
plt.grid()
t0=[]
for i in range(100):
    t0.append(i+1)
plt.plot(t0,x2ave,'o',ms=3)
plt.xlabel('time(step number)')
plt.ylabel('<x2>')
plt.title('random walk in one dimension')
#plt.text(10,80,'<x2> versus time')
k,b=np.polyfit(t0,x2ave,1)#多项式拟合
ideal=[]
for i in range(100):
    ideal.append(k*(i+1)+b)
plt.plot(t0,ideal,color='red')
print(k,b)
#------
x4ave=[0]*100
for i in range(5000):
    x1,t1,x2ave1=randpath(100)
    for j in range(len(x1)-1):
        x4ave[j]=x4ave[j]+x1[j+1]**4/5000

plt.figure(figsize=(10,5))
plt.grid()
plt.plot(t0,x4ave,'o',ms=3)
plt.xlabel('time(step number)')
plt.ylabel('<x4>')
plt.title('random walk in one dimension')
a,b,c=np.polyfit(t0,x4ave,2)
ideal4=[]
for i in range(100):
    ideal4.append(a*i**2+b*i+c)
plt.plot(t0,ideal4,color='red')
#plt.text(20,20000,'<x4>versus time')
print(a,b,c)


    
    


    



