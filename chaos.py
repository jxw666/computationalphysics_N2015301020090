import matplotlib.pyplot as plt
import math
g=9.8
def chaos(theta,l,q,F_D,w_D):
    w=[0]
    Theta=[theta]
    dt=0.01
    i=0
    t=[0]
    T=0
    while T<=100:
        t_i=t[i]
        w_i=w[i]
        theta_i=Theta[i]
        w_dt=w_i-((g/l)*math.sin(theta_i)+q*w_i-F_D*math.sin(w_D*t_i))*dt
        theta_dt=theta_i+w_dt*dt
        while theta_dt>math.pi:
             theta_dt=theta_dt-2*(math.pi)
        while theta_dt<(-math.pi):
             theta_dt=theta_dt+2*(math.pi)
        T=t_i+dt
        w.append(w_dt)
        Theta.append(theta_dt)
        t.append(T)
        i=i+1
    return Theta,t,w
CH=chaos(0.2,9.8,0.5,1.2,2/3)

#CHo=chaos(0.2,9.8,0.5,0,2/3)
CH2=chaos(0.3,9.8,0.5,0.5,2/3)
plt.xlabel('theta/radians')
plt.ylabel('w/radians/s')
plt.title('w versus theta')

line1=plt.plot(CH[0],CH[2],label='F_D=1.2',color='black')
#line2=plt.plot(CHo[1],CHo[0],label='F_D=0',color='red')
#line3=plt.plot(CH2[0],CH2[2],label='F_D=0.5',color='black')
plt.legend()
plt.show()
            
            
        