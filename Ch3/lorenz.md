


> Written with [StackEdit](https://stackedit.io/).
# Chapter_two_section3.6-The Lorenz Model
-------------
problem3.26&27

--------
##  Background
-------

E.N.Lorenz atmospheric scientist(not Lorentz!) studied the Navier-Stokes equations and the Rayleigh-Benard problem,which concerns a fluid in a container whose top and bottom surfaces are held at different temperatures.It had long been know that as the difference between these two temperature is increased, the fluid can undergo transitions from a stationary state to steady flow to chaotic flow.He considered a **greatly simplified** version of Navier-Stokes equationas as applied to this particular problem.He grossly oversimplified the problem as he reduced it to only three equations
 <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dx}{dt}=\sigma(y-x)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=\sigma(y-x)" title="\frac{dx}{dt}=\sigma(y-x)" /></a>,
 <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dy}{dt}=-xz&plus;rx-y" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=-xz&plus;rx-y" title="\frac{dy}{dt}=-xz+rx-y" /></a>,
 <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dz}{dt}=xy-bz" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dz}{dt}=xy-bz" title="\frac{dz}{dt}=xy-bz" /></a>.
 x,y,z are derived from the temperature density and velocity variables from Rayleigh-Benard problem,and the sigma, r,b are the measures of of temperature difference and other fluid parameters. In the following analysis,we'll take<a href="http://www.codecogs.com/eqnedit.php?latex=\sigma=10,b=8/3" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\sigma=10,b=8/3" title="\sigma=10,b=8/3" /></a>.From our text book we know the transition from steady convection to chaotic behavior takes place at<a href="http://www.codecogs.com/eqnedit.php?latex=r=470/19\approx24.74" target="_blank"><img src="http://latex.codecogs.com/gif.latex?r=470/19\approx24.74" title="r=470/19\approx24.74" /></a>.
 We again use Euler method to solve this problem.


-------
## [Code](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/Ch3/lorenz.py)
-----
## Results&Analysis
-------------
1.Phase-space
Construct a phase-space plot model for the Lorenz model.Imagine that x,y and z are coordinates in some abstract space.
r=2, steady
![r=2](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/Ch3/r%3D2.png)
![r=10](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/Ch3/r%3D10.png)
![r=15](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/Ch3/r%3D15.png)
![r=20](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/Ch3/r%3D20.png)
![r=30](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/Ch3/r%3D30.png)
![r=50](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/Ch3/r%3D50.png)
![r=100](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/Ch3/r%3D100.png)
When r is small,the system is steady.When r=20,the system is chaotic,not r=25.However,when r is greater,the chaos seems to disappear???

-----------
2.Poincatr sections
Consider the two-dimensional slices
x(0)=1,y(0)=z(0)=0
![1](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/Ch3/poin1.png)
x(0)=0,y(0)=z(0)=1
![2](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/Ch3/poin2.png)
Poincare sections are independent of the initial conditions.
