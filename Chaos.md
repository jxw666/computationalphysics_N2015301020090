﻿


> Written with [StackEdit](https://stackedit.io/).
# Chapter_three_section3.3
----------
贾雪巍2015301020090

## Chaos in the Driven Nonlinear Pendulum
-------
Problem 3.12

-----------
## Background
-----
![1](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/chaos1.png)
One example of a single pendulum is a particle of mass m connected by a massless string to a rigid surpport.We let <a href="http://www.codecogs.com/eqnedit.php?latex=\theta" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\theta" title="\theta" /></a>be the angle that the string makes with the vertical and assume that the string is always taut,as in figure.We also assume there are only two forces acting on the particle,gravity and the tension of the string.The force perpendicular to the string is given by <a href="http://www.codecogs.com/eqnedit.php?latex=F_{\theta}=-mgsin\theta" target="_blank"><img src="http://latex.codecogs.com/gif.latex?F_{\theta}=-mgsin\theta" title="F_{\theta}=-mgsin\theta" /></a>.Here we use the **Euler-Cromer method** to solve the problem.And we add some damping  to the model.Assume that damping force is  proportional to the velocity.Also, consider the addition of a driving force to the problem.A convenient choice is to assume that the driving force is sinusodial with time,with amplitude F_D and angular frequency <a href="http://www.codecogs.com/eqnedit.php?latex=\Omega_D" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\Omega_D" title="\Omega_D" /></a>.These lead to the equation of motion <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{d^2\theta&space;}{dt^2}=-\frac{g}{l}sin\theta-q\frac{d\theta}{dt}&plus;F_Dsin(\Omega_Dt)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{d^2\theta&space;}{dt^2}=-\frac{g}{l}sin\theta-q\frac{d\theta}{dt}&plus;F_Dsin(\Omega_Dt)" title="\frac{d^2\theta }{dt^2}=-\frac{g}{l}sin\theta-q\frac{d\theta}{dt}+F_Dsin(\Omega_Dt)" /></a>
l is the length of the string.Rewrite it as two first-order diiferential equation<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dw&space;}{dt}=-\frac{g}{l}sin\theta-q\frac{d\theta}{dt}&plus;F_Dsin(\Omega_Dt)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dw&space;}{dt}=-\frac{g}{l}sin\theta-q\frac{d\theta}{dt}&plus;F_Dsin(\Omega_Dt)" title="\frac{dw }{dt}=-\frac{g}{l}sin\theta-q\frac{d\theta}{dt}+F_Dsin(\Omega_Dt)" /></a>,<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{d\theta&space;}{dt}=w" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{d\theta&space;}{dt}=w" title="\frac{d\theta }{dt}=w" /></a>.
## [Code](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/chaos.py)
---------------------
## Results&Analysis
---------------
1.theta as function of time
q=0.5,l=g=9.8,theta(0)=0.2,w(0)=0,w_D=2/3
(parameters in the text book)
![2](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/chaos2.png)
The vertical jumps in theater due to resetting of the angle to keep it in the range -pi to pi and thus correspond to the pendulum swinging "over the top".

----------
Without resetting the angle,F_D=1.2
![3](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/chaos3.png)
We see that pendulum does not settle into any sort of repeating steady behavior .
**At high drive the motion is chaotic!**
From the text book we know that in chaotic condition two pendulum with slightly different initial parameters their difference increased rapidly and irregularly .The diverge exponentially fast.
 
----
2.phase-space plot
Our text book said it is possible to make certain accurate predictions in chaotic conditions by ploting w as function of theta(phase-space).Let's have a try ;-)
![4](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/chaos4.png)
the pendulum settles into a regular orbit

-----
T=100s
![5](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/chaos5.png)
T=1000s
![6](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/chaos6.png)

(I think there are many horizontal lines because of resetting angles from -pi to pi)

3.Poincare section
Then we plot w versus theta only at times that w_D=2npi,where n is an integer.

for F_D=0.5,T=100s or T=10000s(same)
![](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/FD%3D0.5.png)
for F_D=1.2
![](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/1000s.png)

----------------
 maximum of the drive force,F_D=1.2
 ![](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/pi:2.png)

-------------
 pi/4 out-of-phase
 initial theta=0.2
 ![](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/pi:4.png)
 initial theta=2
 ![](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/pi:4%202.png)
 initial theta=20
 ![](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/pi:4%2020.png)
 
 ----------
It's not sensitive to the initial value.
"special attractor"?
The behavior in the chaotic regime is not completely random,but can be describe by a strange attractor in phase space.
## Attractor in wikipedia
In the mathematical field of dynamical systems, an attractor is a set of numerical values toward which a system tends to evolve, for a wide variety of starting conditions of the system. System values that get close enough to the attractor values remain close even if slightly disturbed.

An attractor is called strange if it has a fractal structure. This is often the case when the dynamics on it are chaotic, but strange nonchaotic attractors also exist. If a strange attractor is chaotic, exhibiting sensitive dependence on initial conditions, then any two arbitrarily close alternative initial points on the attractor, after any of various numbers of iterations, will lead to points that are arbitrarily far apart (subject to the confines of the attractor), and after any of various other numbers of iterations will lead to points that are arbitrarily close together. Thus a dynamic system with a chaotic attractor is locally unstable yet globally stable: once some sequences have entered the attractor, nearby points diverge from one another but never depart from the attractor.
 
