import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def lorenz(r,sigma,b,TIME):
    x=[1]
    y=[0]
    z=[0]
    t=[0]
    i=0
    t_i=0
    dt=0.01
    while t_i<=TIME:
        x_i=x[i]
        y_i=y[i]
        z_i=z[i]
        t_i=t[i]
        x_dt=x_i+sigma*(y_i-x_i)*dt
        y_dt=y_i-(x_i*z_i-r*x_i+y_i)*dt
        z_dt=z_i+(x_i*y_i-b*z_i)*dt
        T=t_i+dt
        x.append(x_dt)
        y.append(y_dt)
        z.append(z_dt)
        t.append(T)
        i=i+1
    return x,y,z,t
L1=lorenz(100,10,8/3,50)
L2=lorenz(100,10,8/3,50)
fig = plt.figure(figsize=(15, 4))
#ax = fig.gca(projection='3d')
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')

ax3 = fig.add_subplot(133, projection='3d')
#ax.view_init(90, 0)
#ax.set_xlabel("X label")
#ax.set_ylabel("Y label")
#ax.set_zlabel("Z label")
X1=np.array(L1[0])
Y1=np.array(L1[1])
Z1=np.array(L1[2])
#T=np.array(L1[3])
X2=np.array(L2[0])
Y2=np.array(L2[1])
Z2=np.array(L2[2])
ax1.plot(X1,Y1,Z1,color='black')
ax1.set_title('r=100')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.view_init(30,0)
ax2.plot(X2,Y2,Z2,color='black')
ax2.set_title('r=100')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel("z")
ax1.view_init(30,180)

ax3.plot(X2,Y2,Z2,color='black')
ax3.set_title('r=100')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel("z")
ax3.view_init(90,0)
plt.show()
    