import math
import matplotlib.pyplot as plt
import numpy as np
def billiard(x0,y0,vx0,vy0,r,a,time):
    x=[x0]
    y=[y0]
    vx=vx0
    vy=vy0
    VX=[vx]
    t=[0]
    dt=0.01
    T=0
    while T<=time:
        x.append(x[-1]+vx*dt)
        y.append(y[-1]+vy*dt)
        t.append(t[-1]+dt)
        VX.append(vx)
        if y[-1]>=a and (x[-1]**2+(y[-1]-a)**2)>r**2:
            d=math.sqrt(x[-1]**2+(y[-1]-a)**2)
            d2=math.sqrt(vx**2+vy**2)
            d1=2*r-d
            
            x.append(x[-1]*d1/d)
            y.append((y[-1]-a)*d1/d+a)
            cs=x[-1]/d
            ss=(y[-1]-a)/d
            vpt=vy*cs-vx*ss
            vpr=-(vy*ss+vx*cs)
            vx=vpr*cs-vpt*ss
            vy=vpr*ss+vpt*cs
            VX.append(vx)
        elif y[-1]<=-a and (x[-1]**2+(y[-1]+a)**2)>r**2:
            d=math.sqrt(x[-1]**2+(y[-1]+a)**2)
            d1=2*r-d
            x.append(x[-1]*d1/d)
            y.append((y[-1]+a)*d1/d-a)
            cs=x[-1]/d
            ss=(y[-1]+a)/d
            vpt=vy*cs-vx*ss
            vpr=-(vy*ss+vx*cs)
            vx=vpr*cs-vpt*ss
            vy=vpr*ss+vpt*cs
            VX.append(vx)
        elif -a<y[-1]<a and x[-1]>r:
           x[-1]=2*r-x[-1]
           x.append(x[-1])
           y.append(y[-1])
           vx=-vx
           VX.append(vx)
        elif -a<y[-1]<a and x[-1]<-r:
           x[-1]=-2*r-x[-1]
           vx=-vx  
           x.append(x[-1])
           y.append(y[-1])
           VX.append(vx)
        T=t[-1]
    return x,y,VX

fig = plt.figure(figsize=(11, 11))

B=billiard(0.5,0.5,-0.4,-0.3,1,0,800)
a=B[0]
b=B[1]
c=B[2]
V=[]
xx=[]
A=billiard(0.5,0.5,-0.4,-0.3,1,0.01,800)
aa=A[0]
bb=A[1]
cc=A[2]
VV=[]
xxx=[]
C=billiard(0.5,0.5,-0.4,-0.3,1,0.1,800)
aaa=C[0]
bbb=C[1]
ccc=C[2]
VVV=[]
xxxx=[]
D=billiard(0.5,0.5,-0.4,-0.3,1,1,800)
aaaa=C[0]
bbbb=C[1]
cccc=C[2]
VVVV=[]
xxxxx=[]
plt.subplot(2,2,1)
plt.xlim(-1,1)

for i in range(len(B[1])-1):
    if abs(b[i])<0.001:
        V.append(c[i])
        xx.append(a[i])
plt.plot(xx,V,'o', ms=2,color='black')
plt.xlabel('x')
plt.ylabel('vx')
plt.title('alpha=0')
plt.subplot(2,2,2)
plt.xlim(-1,1)

for i in range(len(A[1])-1):
    if abs(bb[i])<0.001:
        VV.append(cc[i])
        xxx.append(aa[i])
plt.plot(xxx,VV,'o', ms=2,color='black')
plt.xlabel('x')
plt.ylabel('vx')
plt.title('alpha=0.01')
plt.subplot(2,2,3)
plt.xlim(-1,1)

for i in range(len(C[1])-1):
    if abs(bbb[i])<0.001:
        VVV.append(ccc[i])
        xxxx.append(aaa[i])
plt.plot(xxxx,VVV,'o', ms=2,color='black')
plt.xlabel('x')
plt.ylabel('vx')
plt.title('alpha=0.1')
plt.subplot(2,2,4)
plt.xlim(-1,1)

for i in range(len(D[1])-1):
    if abs(bbbb[i])<0.001:
        VVVV.append(cccc[i])
        xxxxx.append(aaaa[i])
plt.plot(xxxx,VVV,'o', ms=2,color='black')
plt.xlabel('x')
plt.ylabel('vx')
plt.title('alpha=1')

