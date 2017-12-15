import math
import numpy as np
import matplotlib.pyplot as plt
delta_x=0.01
c=300
delta_t=3.5*10**(-5)#delta_x/c#2*10**(-5)#3.33*10**(-5)delta_x/c
r=c*delta_t/delta_x
x=np.linspace(0,1,int(1/delta_x)+1)
k0,x0=1000,0.3
y_initial=[]
for i in range(1+int(1/delta_x)):
    y_initial.append(math.exp(-k0*(i*delta_x-x0)**2))
y1=y_initial
y2=y_initial
for i in range(11):
    y3=[0]
    for j in range(1,len(y2)-1):
        y3.append((2*(1-r**2)*y2[j]-y1[j]+r**2*(y2[j-1]+y2[j+1])))
    y3.append(0)
    y1=y2
    y2=y3


n_step=11
n_plot=11
plt.figure(figsize=(10,10))
plt.subplot(n_plot,1,1)
plt.plot(x,y_initial,color='blue')
plt.title('Waves On A String With Fixed Ends')
for i in range(n_plot-1):
    plt.subplot(n_plot,1,i+2)
    plt.plot(x,y1,color='blue')
    #plt.xlabel('x')
    #plt.figure(figsize=(7, 7))
    for i in range(11):
        y3=[0]
        for j in range(1,len(y2)-1):
            y3.append((2*(1-r**2)*y2[j]-y1[j]+r**2*(y2[j-1]+y2[j+1])))
        y3.append(0)
        y1=y2
        y2=y3

    

plt.show()
