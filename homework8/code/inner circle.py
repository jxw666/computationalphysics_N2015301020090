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
    while T<=time:
        x.append(x[-1]+vx*dt)
        y.append(y[-1]+vy*dt)
        t.append(t[-1]+dt)
        if y[-1]>=a and (x[-1]**2+(y[-1]-a)**2)>r**2 and  (x[-1]**2+(y[-1]-a)**2)>RR**2:
            d=math.sqrt(x[-1]**2+(y[-1]-a)**2)
            d1=2*r-d
            x.append(x[-1]*d1/d)
            y.append((y[-1]-a)*d1/d+a)
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
            cs=x[-1]/d
            ss=(y[-1]+a)/d
            vpt=vy*cs-vx*ss
            vpr=-(vy*ss+vx*cs)
            vx=vpr*cs-vpt*ss
            vy=vpr*ss+vpt*cs
        elif -a<y[-1]<a and x[-1]>r and  (x[-1]**2+(y[-1]-a)**2)>RR**2:
           x[-1]=2*r-x[-1]
           vx=-vx
        elif -a<y[-1]<a and x[-1]<-r and  (x[-1]**2+(y[-1]-a)**2)>RR**2:
           x[-1]=-2*r-x[-1]
           vx=-vx 
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

        T=t[-1]
    return x,y
def circle(r1,l1):
    x1=[]
    y1=[]
    theta=[]
    theta.append(0)
    tu=math.pi/10000
    for j in range(10000):
        x1.append(r1*math.cos(theta[-1]))
        y1.append(r1*math.sin(theta[-1])+l1)
        theta.append(theta[-1]+tu)
    theta1=[]
    theta1.append(math.pi) 
    for k in range(10000):
        x1.append(r1*math.cos(theta1[-1]))
        y1.append(r1*math.sin(theta1[-1])-l1)
        theta1.append(theta1[-1]+tu)
    return x1,y1
fig = plt.figure(figsize=(7, 7))
B=billiard(0.5,0.5,-0.4,-0.3,1,0,0.2,800)
plt.plot(B[0],B[1],'k:')
a1,b1=circle(1,0.01)
plt.plot(a1,b1,color='black')
plt.xlabel('x')
plt.ylabel('y')
plt.title('r=0.2 wall in the center')

            
    
        
        
            
            