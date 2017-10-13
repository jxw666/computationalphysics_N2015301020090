import matplotlib.pyplot as plt
import math
import numpy as np
g=9.8
def Trajectory(velocity,angle,Temp):
    velocity_x=[velocity*math.cos(angle)]
    velocity_y=[velocity*math.sin(angle)]
    dt=0.1
    x=[0]
    y=[0]
    i=0
    y_dt=1
    while  y_dt>0:  
        vxi=velocity_x[i]
        vyi=velocity_y[i]
        v=math.sqrt(vxi**2+vyi**2)
        B=(Temp/300)**2.5*(1-6.5*10**(-3)*y[i]/Temp)**2.5*4*10**(-5)
        vx_dt=vxi-B*v*vxi*dt
        vy_dt=vyi-B*v*vyi*dt-g*dt#g*(6371/(6371+y[i]/1000))**2考虑g的影响时
        x_dt=x[i]+vxi*dt
        y_dt=y[i]+vyi*dt
        if y_dt<0:
            r=-y[-1]/y_dt
            x_dt=(x[-1]+r*x_dt)/(r+1)
            y_dt=0
        range=x_dt
        x.append(x_dt)
        y.append(y_dt)
        velocity_x.append(vx_dt)
        velocity_y.append(vy_dt)
        i=i+1
    return x,y,range

alpha=[]
Range=[]
plt.xlabel('x/m')
plt.ylabel('y/m')
plt.title('The trajectory of a cannon shell')
for i in range(10):
    angle=i*math.pi/20
    t=Trajectory(700,angle,300)
    plt.plot(t[0],t[1])
    #alpha.append(angle)
    #Range.append(t[2]) #to get the maximum range
plt.xlim(0,30000)
#plt.plot(np.array(alpha),np.array(Range),'o')
plt.show()
#R=max(Range)
#l=Range.index(R)
#A=alpha[l]/math.pi*180
#print(A,R)
