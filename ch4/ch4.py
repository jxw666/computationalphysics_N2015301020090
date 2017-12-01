import math
import matplotlib.pyplot as plt
MS=2*10**30
MJ=1.9*10**27*10
ME=6*10**24
a=(6*10**24+5.2*1.9*10**27)/(2*10**30+6*10**24+1.9*10**27)
b=((1-a)*2*math.pi*6*10**24+1.9*10**27*2*math.pi*(5.2-a)/math.sqrt(5.2))/(2*10**30*a)
c=(2*math.pi*ME+2*math.pi*MJ/math.sqrt(5.2))/(ME+MS+MJ)
JX=[5.2-a]
EX=[1-a]
SX=[0-a]
JY=[0]
EY=[0]
SY=[0]
COMX=[0]
COMY=[0]
vex=0
vey=2*math.pi
vjx=0
vjy=2*math.pi/math.sqrt(5.2)
vsx=0
vsy=0
t=0
dt=0.01
i=0
while t<=100:
    re_s=math.sqrt((EX[i]-SX[i])**2+(EY[i]-SY[i])**2)
    re_j=math.sqrt((EX[i]-JX[i])**2+(EY[i]-JY[i])**2)
    rs_j=math.sqrt((SX[i]-JX[i])**2+(SY[i]-JY[i])**2)
    vex_dt=vex-(4*math.pi**2*(EX[i]-SX[i])/re_s**3-4*math.pi**2*(MJ/MS)*(EX[i]-JX[i])/re_j**3)*dt
    vey_dt=vey-(4*math.pi**2*(EY[i]-SY[i])/re_s**3-4*math.pi**2*(MJ/MS)*(EY[i]-JY[i])/re_j**3)*dt
    vjx_dt=vjx-(4*math.pi**2*(JX[i]-SX[i])/rs_j**3-4*math.pi**2*(ME/MS)*(JX[i]-EX[i])/re_j**3)*dt                       
    vjy_dt=vjy-(4*math.pi**2*(JY[i]-SY[i])/rs_j**3-4*math.pi**2*(ME/MS)*(JY[i]-EY[i])/re_j**3)*dt                      
    vsx_dt=vsx-(4*math.pi**2*(ME/MS)*(SX[i]-EX[i])/re_s**3-4*math.pi**2*(MJ/MS)*(SX[i]-JX[i])/rs_j**3)*dt  
    vsy_dt=vsy-(4*math.pi**2*(ME/MS)*(SY[i]-EY[i])/re_s**3-4*math.pi**2*(MJ/MS)*(SY[i]-JY[i])/rs_j**3)*dt                                                                                            
    COMX.append(0)
    COMY.append(COMY[i]+c*dt)
    EX.append(EX[i]+vex_dt*dt)
    EY.append(EY[i]+vey_dt*dt-c*dt)
    JX.append(JX[i]+vjx_dt*dt)
    JY.append(JY[i]+vjy_dt*dt-c*dt)
    SX.append(SX[i]+vsx_dt*dt)
    SY.append(SY[i]+vsy_dt*dt-c*dt)    

    vex=vex_dt
    vey=vey_dt
    vsx=vsx_dt
    vsy=vsy_dt
    vjx=vjx_dt
    vjy=vjy_dt
    i=i+1
    t=t+dt
fig = plt.figure(figsize=(7, 7))   
plt.plot(EX,EY,linewidth='0.1',color='blue',label='Earth')
plt.plot(SX,SY,linewidth='1',color='red',label='Sun')
plt.plot(JX,JY,linewidth='1',color='black',label='Jupiter')
#plt.plot(COMX,COMY,color='yellow',linewidth='2')
#plt.grid()
plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.title('3-body simulation Earth&Jupiter&Sun')
plt.legend()
plt.show()