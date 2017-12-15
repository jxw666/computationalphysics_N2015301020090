# Waves: The ideal Case

2015301020090

Problem 6.2

## Backgroud

The equation of wave motion is 
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial^{2}y}{\partial&space;t^2}=c^2\frac{\partial^{2}y}{\partial&space;x^2}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial^{2}y}{\partial&space;t^2}=c^2\frac{\partial^{2}y}{\partial&space;x^2}" title="\frac{\partial^{2}y}{\partial t^2}=c^2\frac{\partial^{2}y}{\partial x^2}" /></a>

c is the speed with which a wave moves on the string.We use a finitie difference form.Let the displacement of the string is a function of i and n.i and n are correspond to the spatial and time coordinates.We get
<a href="http://www.codecogs.com/eqnedit.php?latex=y(i.n&plus;1)=2[1-r^2]y(i,n)-y(i,n-1)&plus;r^2[y(i&plus;1,n)&plus;y(i-1,n)]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?y(i.n&plus;1)=2[1-r^2]y(i,n)-y(i,n-1)&plus;r^2[y(i&plus;1,n)&plus;y(i-1,n)]" title="y(i.n+1)=2[1-r^2]y(i,n)-y(i,n-1)+r^2[y(i+1,n)+y(i-1,n)]" /></a>

r=c*delta-xt/delta-x.

We set the initial displacement of the string as<a href="http://www.codecogs.com/eqnedit.php?latex=y_0(x)=exp[-k(x-x_0)^2]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?y_0(x)=exp[-k(x-x_0)^2]" title="y_0(x)=exp[-k(x-x_0)^2]" /></a>

,a "Gaussian pluck",where x0=0.3 and x runs from 0 to 1.And the string is held fixed y0(x) prior to t=0.

The problem we are dealing with involves two step sizes.We should let r=1.Because when r=1 the higher order terms are largely cancelled out.A smaller step is actually less accurate.With our numerical schem the disurbance is propagate one spacial step for each time step.We can't have a disturbance that moves faster.

##	[Code](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ch6/ch6.py)

## Results&Analysis

1.r=1

![1](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ch6/1.png)

2.r<1

![2](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ch6/2.png)

To see it clearly,here's a BIGGER picture:![33](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ch6/33.png)

We can see that after the reflection from a fixed end there's small blip.Our textbook says it is because the numerical error when r<1

3.r>1

![44](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ch6/44.png)

a smaller r:

![4](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ch6/4.png)





