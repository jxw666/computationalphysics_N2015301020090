
import numpy as np
import matplotlib.pyplot as plt


def lorenz(r,sigma,b):
    x=[0]
    y=[1]
    z=[1]
    t=[0]
    i=0
    t_i=0
    dt=0.01
    while t_i<=50:
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
L=lorenz(25,10,8/3)




#fig=plt.figure()
#ax = fig.gca(projection='3d')
X=np.array(L[0])
Y=np.array(L[1])
Z=np.array(L[2])
T=np.array(L[3])


    
#ax.plot(X,Y,Z,color='black')
plt.subplot(121)
poin_z=[]
poin_x=[]
poin_y=[]
for i in range(len(X)-1):
    if X[i]*X[i+1]<=0:
       poin_z.append(Z[i])
       poin_y.append(Y[i])
       
plt.plot(np.array(poin_y),np.array(poin_z),'o')
plt.xlabel('y')
plt.ylabel('z')
plt.title('z versus y when x=0')   

plt.subplot(122)
p_z=[]
p_x=[]
p_y=[]
for i in range(len(X)-1):
    if Y[i]*Y[i+1]<=0:
       p_z.append(Z[i])
       p_x.append(X[i])       
plt.plot(np.array(p_x),np.array(p_z),'o')
plt.xlabel('x')
plt.ylabel('z')
plt.title('x versus z when y=0')   

#for angle in range(0, 360):
#ax.view_init(30, 0)
#plt.draw()
    #plt.pause(.001)
#plt.plot(L[0],L[2])
plt.show()
    