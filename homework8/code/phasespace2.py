import math
import matplotlib.pyplot as plt
def billiard(x0,y0,vx0,vy0,r,a, RR,time):
    x=[x0]
    y=[y0]
    vx=vx0
    vy=vy0
    t=[0]
    dt=0.01
    T=0
    VX=[vx]
    while T<=time:
        x.append(x[-1]+vx*dt)
        y.append(y[-1]+vy*dt)
        VX.append(vx)
        t.append(t[-1]+dt)
        if y[-1]>=a and (x[-1]**2+(y[-1]-a)**2)>r**2 and  (x[-1]**2+(y[-1]-a)**2)>RR**2:
            d=math.sqrt(x[-1]**2+(y[-1]-a)**2)
            d1=2*r-d
            x.append(x[-1]*d1/d)
            y.append((y[-1]-a)*d1/d+a)
            VX.append(vx)
            cs=x[-1]/d
            ss=(y[-1]-a)/d
            vpt=vy*cs-vx*ss
            vpr=-(vy*ss+vx*cs)
            vx=vpr*cs-vpt*ss
            vy=vpr*ss+vpt*cs
        elif y[-1]<=-a and (x[-1]**2+(y[-1]+a)**2)>r**2 and  (x[-1]**2+(y[-1]-a)**2)>RR**2:
            d=math.sqrt(x[-1]**2+(y[-1]+a)**2)
            d1=2*r-d
            x.append(x[-1]*d1/d)
            y.append((y[-1]+a)*d1/d-a)
            VX.append(vx)
            cs=x[-1]/d
            ss=(y[-1]+a)/d
            vpt=vy*cs-vx*ss
            vpr=-(vy*ss+vx*cs)
            vx=vpr*cs-vpt*ss
            vy=vpr*ss+vpt*cs
        elif -a<y[-1]<a and x[-1]>r and  (x[-1]**2+(y[-1]-a)**2)>RR**2:
           x[-1]=2*r-x[-1]
           vx=-vx
           x.append(x[-1]*d1/d)
           y.append((y[-1]+a)*d1/d-a)
           VX.append(vx)
        elif -a<y[-1]<a and x[-1]<-r and  (x[-1]**2+(y[-1]-a)**2)>RR**2:
           x[-1]=-2*r-x[-1]
           vx=-vx 
           x.append(x[-1]*d1/d)
           y.append((y[-1]+a)*d1/d-a)
           VX.append(vx)
        elif (x[-1]**2+(y[-1]-a)**2)<=RR**2:
            d=math.sqrt(x[-1]**2+y[-1]**2)
            d1=2*RR-d
            x.append(x[-1]*d1/d)
            y.append(y[-1]*d1/d)
            t.append(t[-1]+dt)
            cs=x[-1]/d
            ss=y[-1]/d
            vpt=vy*cs-vx*ss
            vpr=-(vy*ss+vx*cs)
            vx=vpr*cs-vpt*ss
            vy=vpr*ss+vpt*cs
            VX.append(vx)
        T=t[-1]
    return x,y,VX


B=billiard(0.5,0.5,-0.4,-0.3,1,0,0.2,800)
aa=B[0]
bb=B[1]
cc=B[2]

V=[]
xx=[]
for i in range(len(B[1])-1):
    if abs(bb[i])<0.001:
        V.append(cc[i])
        xx.append(aa[i])
        
        
plt.plot(xx,V,'o', ms=2,color='black')

plt.xlabel('x')
plt.ylabel('vx')
plt.title('r=0.2 in center,phase-space')

    
        
        
            
            
