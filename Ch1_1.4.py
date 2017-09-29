
import matplotlib.pyplot as plt
time=[0]
T=10000
a=10#初始A粒子数
b=0#初始B粒子数
A=[a]#the number of nucleus A
B=[b]#the number of nucleus B
Analytic_A=[a]
Analytic_B=[b]
dt=0.1
tA=1000#time constant for A
tB=1#time constant for B
e=2.718281828459
i=0
while i<=int(T/dt-1):
#for i in range(int(T/dt)-1):
    num_of_a_at_dt=A[i]-dt*A[i]/tA
    A.append(num_of_a_at_dt)
    num_of_b_at_dt=B[i]+dt*(A[i]/tA-B[i]/tB)
    B.append(num_of_b_at_dt)
    time.append(dt*(i+1))
    Analytic_A.append(a*2.718281828459**(-dt*(i+1)/tA))
    Analytic_B.append(b+a*tB/(tA-tB)*(2.718281828459**(-dt*(i+1)/tA)-2.718**(-dt*(i+1)/tB)))
    i=i+1
plt.xlabel('Time(s)')
plt.ylabel('Number of particles')
plt.title('Radioactive Decay of 2 nucleus')
line1,= plt.plot(time,A,color='blue',linewidth='3.0',label='A')
line2,= plt.plot(time,B,color='pink',linewidth='3.0',label='B')
line3,= plt.plot(time,Analytic_A,color='yellow',linestyle='-.',label='analytic_A')
line4,= plt.plot(time,Analytic_B,color='red',linestyle='-.',label='analytic_B')
plt.legend()
plt.show()