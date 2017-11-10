import math
import matplotlib.pyplot as plt
def billiard(x0,y0,vx0,vy0,r,time):
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
        if (x[-1]**2+y[-1]**2)>r**2:
            d=math.sqrt(x[-1]**2+y[-1]**2)
            d1=2*r-d##这里借鉴了强雨的代码,对坐标进行修正
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
def circle(r1):
    x1=[]
    y1=[]
    theta=[]
    theta.append(0)
    tu=2*math.pi/10000
    for j in range(10000):
        x1.append(r1*math.cos(theta[-1]))
        y1.append(r1*math.sin(theta[-1]))
        theta.append(theta[-1]+tu)
    return x1,y1
fig = plt.figure(figsize=(7, 7))
B=billiard(0.5,0.5,-0.4,-0.3,1,500)
plt.plot(B[0],B[1],'k:')
a1,b1=circle(1.0)
plt.plot(a1,b1,color='black') 
plt.xlabel('x')
plt.ylabel('y')
plt.title('Circular stadium-trajectory')
 
    
        
        
            
            