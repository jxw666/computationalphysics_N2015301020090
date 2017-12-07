import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
#1.initialize-V
delta=0.1
V_old=[[0.]*(int(1+1/delta))for i in range(int(1+1/delta))]
for i in range(1+int(round(0.3/delta))):#int(0.3/0.1)=2
    V_old[int(round(0.3/delta))][i]=-1#借鉴上官俊怡学姐的代码，设置初值
deltaV=100
#2.update-V
while deltaV >=len(V_old)**2*10**(-5):
    V_new=[[0.]*len(V_old)for i in range(len(V_old))]
    for i in range(1,len(V_old)-1):
        for j in range(1,len(V_old)-1):
            V_new[i][j]=(V_old[i-1][j]+V_old[i+1][j]+V_old[i][j-1]+V_old[i][j+1])/4
    for j in range(1,len(V_old)-1):
        V_new[0][j]=(V_old[0][j-1]+V_old[0][j+1])/4
    for k in range(1,len(V_old)-1):
        V_new[k][0]=(V_old[k-1][0]+V_old[k+1][0]+2*V_old[k][1])/4
    V_new[0][0]=V_old[0][1]/2
    for l in range(1+int(round(0.3/delta))):
        V_new[int(round(0.3/delta))][l]=-1.
    b=[]
    for i in range(len(V_old)):
        a=[abs(V_old[i][j]-V_new[i][j]) for j in range(len(V_old))]
        b.append(max(a))
    deltaV=max(b)
    V_old=V_new
N=len(V_old)#这里也借鉴了上官俊怡的代码
V1=np.transpose(V_old)#1st Quadrant
V3=[[0.]*(N-1) for i in range(N)]#3rd quadrant
for i in range(N):
    for j in range(N-1):
        V3[i][j]=-V1[N-1-i][N-1-j]
#add the 4th qudrant to V3 using extend
for i in range(N):
    V3[i].extend(V1[N-1-i])
#add the 1st&2nd qudrant using +
V_whole=V3
for i in range(N-1):
    V_whole=V_whole+[V3[N-2-i]]
del V1,V3 
      
x=np.linspace(-1,1,len(V_whole))
X,Y= np.meshgrid(x,x)
fig = plt.figure()


#ax = Axes3D(fig)
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('Electric Potential/V')
#ax.set_title('Electric Potential Distribution Near Two Metal Plates') 
#surf=ax.plot_surface(X,Y,V_whole, rstride=1, cstride=1, cmap=cm.viridis)
#fig.colorbar(surf, shrink=0.5, aspect=5)
#wframe = ax.plot_wireframe(X, Y, V_whole, rstride=2, cstride=2)
#CS = plt.contour(X, Y, V_whole, 15, linewidths=0.5, colors='k')
#CS = plt.contourf(X, Y, V_whole, 15)
plt.xlabel('x')
plt.ylabel('y')
#plt.title('Electric Potential Distribution Near Two Metal Plates')
#plt.colorbar()  # draw colorbar
EY,EX=np.gradient(V_whole)
EX,EY=-EX,-EY
plt.quiver(X,Y, EX, EY)
plt.title('Electric field near two metal plates')
plt.show()
