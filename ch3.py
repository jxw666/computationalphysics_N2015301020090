import matplotlib.pyplot as plt
import math
g=9.8
def Trajectory(v,w,theta):
    velocity_x=[v]
    velocity_y=[0]
    velocity_z=[0]
    dt=0.01
    x=[0]
    y=[10]
    z=[0]   
    i=0
    y_dt=1
    while  y_dt>0  :
        theta=theta+w*dt
        F_lateral=0.5*g*(math.sin(4*theta)-0.25*math.sin(8*theta)+0.08*math.sin(12*theta)-0.025*math.sin(16*theta))
        vxi=velocity_x[i]
        vyi=velocity_y[i]
        vzi=velocity_z[i] 
        v=math.sqrt(vxi**2+vyi**2+vzi**2)
        B=0.0039+0.0058/(1+math.exp((v-35)/5))
        vx_dt=vxi-B*v*vxi*dt+F_lateral*math.sin(theta)
        vy_dt=vyi-B*v*vyi*dt-g*dt
        vz_dt=vzi-B*v*vzi*dt+F_lateral*math.cos(theta)-4.1*10**(-4)*vxi*w
        x_dt=x[i]+vxi*dt
        y_dt=y[i]+vyi*dt
        z_dt=z[i]+vzi*dt
        if y_dt<0:
            r=-y[-1]/y_dt
            x_dt=(x[-1]+r*x_dt)/(r+1)
            y_dt=0
        range=x_dt
        x.append(x_dt)
        y.append(y_dt)
        z.append(z_dt)
        velocity_x.append(vx_dt)
        velocity_y.append(vy_dt)
        velocity_z.append(vz_dt)
        i=i+1
    return x,y,z,range





plt.xlabel('x/m')
plt.ylabel('y/m')
for i in range(11):
    t=Trajectory(5*i,math.pi/3,math.pi/2)
    plt.plot(t[0],t[1],label=5*i)
#plt.xlim(0,180)
plt.title('x-y,v=50m/s,w=pi/3')
plt.legend()
plt.show()