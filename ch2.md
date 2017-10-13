


> Written with [StackEdit](https://stackedit.io/).
# Chapter_two_section2.2
problem2.7&8

贾雪巍 2015301020090

----------


## The Trajectory of a Cannon Shell
------------------------------------
Consider a projectile such as a shell shot by a cannon.If we ignore air resistance,the equation of motions can be obtained from Newton's second law.
<a href="http://www.codecogs.com/eqnedit.php?latex=$$&space;\frac{d^2x}{dt^2}=0$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$&space;\frac{d^2x}{dt^2}=0$$" title="$$ \frac{d^2x}{dt^2}=0$$" /></a>
<a href="http://www.codecogs.com/eqnedit.php?latex=$$\frac{d^2y}{dt^2}=-g$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$\frac{d^2y}{dt^2}=-g$$" title="$$\frac{d^2y}{dt^2}=-g$$" /></a>
x and y are horizontal and vertical coordinates of the projectile.
These are second-order differential equations.If we recasting the equations in the following way.
<a href="http://www.codecogs.com/eqnedit.php?latex=$$\frac{dx}{dt}=v_x$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$\frac{dx}{dt}=v_x$$" title="$$\frac{dx}{dt}=v_x$$" /></a>
<a href="http://www.codecogs.com/eqnedit.php?latex=$$\frac{dv_x}{dt}=0$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$\frac{dv_x}{dt}=0$$" title="$$\frac{dv_x}{dt}=0$$" /></a>
<a href="http://www.codecogs.com/eqnedit.php?latex=$$\frac{dy}{dt}=v_y$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$\frac{dy}{dt}=v_y$$" title="$$\frac{dy}{dt}=v_y$$" /></a>
<a href="http://www.codecogs.com/eqnedit.php?latex=$$\frac{dv_y}{dt}=-g$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$\frac{dv_y}{dt}=-g$$" title="$$\frac{dv_y}{dt}=-g$$" /></a>
We can use Euler method to solve the problem.Then we add air resistance, air density,temperature,gravitational acceleration etc to the model to approach the realistic motion of the cannon and find out how much these factors affect the model.

1.We will assume that the magnitude of the drag force on cannon shell is give by 
<a href="http://www.codecogs.com/eqnedit.php?latex=$$F_{drag}=-B_2v^2$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$F_{drag}=-B_2v^2$$" title="$$F_{drag}=-B_2v^2$$" /></a>
where<a href="http://www.codecogs.com/eqnedit.php?latex=$v=\sqrt{&space;v_x^2&plus;v_y^2}$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$v=\sqrt{&space;v_x^2&plus;v_y^2}$" title="$v=\sqrt{ v_x^2+v_y^2}$" /></a>is the speed of the shell.
<a href="http://www.codecogs.com/eqnedit.php?latex=$$F_{drag,x}=-B_2vv_x$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$F_{drag,x}=-B_2vv_x$$" title="$$F_{drag,x}=-B_2vv_x$$" /></a>
<a href="http://www.codecogs.com/eqnedit.php?latex=$$F_{drag,y}=-B_2vv_y$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$F_{drag,y}=-B_2vv_y$$" title="$$F_{drag,y}=-B_2vv_y$$" /></a>
2.Air resistance is propotional to the density of the air,so the drag force at high altitude will be less.Treat the atmosphere as an adiabatic ideal gas which leads to that the density depends on altitude according to
<a href="http://www.codecogs.com/eqnedit.php?latex=$$\rho=\rho_0(1-\frac{ay}{T_0})^\alpha$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$\rho=\rho_0(1-\frac{ay}{T_0})^\alpha$$" title="$$\rho=\rho_0(1-\frac{ay}{T_0})^\alpha$$" /></a>
We replace <a href="http://www.codecogs.com/eqnedit.php?latex=$B_2$with$B_2\rho/\rho_0$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$B_2$with$B_2\rho/\rho_0$" title="$B_2$with$B_2\rho/\rho_0$" /></a>.
$a\approx6.5\times{10^-}^3$K/m,$T_0$is the sea level temperature,$\alpha\approx2.5$for air

3.Further incorporate the effects off the variation of the ground temperature by replacing<a href="http://www.codecogs.com/eqnedit.php?latex=$B_2$by$B_2^{ref}(T_0/T_{ref})^\alpha$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$B_2$by$B_2^{ref}(T_0/T_{ref})^\alpha$" title="$B_2$by$B_2^{ref}(T_0/T_{ref})^\alpha$" /></a>
<a href="http://www.codecogs.com/eqnedit.php?latex=$T_{ref}=300K$,$B_2^{ref}/m=4\times10^{-5}m^{-1}$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$T_{ref}=300K$,$B_2^{ref}/m=4\times10^{-5}m^{-1}$" title="$T_{ref}=300K$,$B_2^{ref}/m=4\times10^{-5}m^{-1}$" /></a>

4.Gravity decreases with altitude as one rises above the Earth's surface because greater altitude means greater distance from the Earth's centre.
<a href="http://www.codecogs.com/eqnedit.php?latex=$$g_h=g_0(\frac{r_e}{r_e&plus;h})^2$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$g_h=g_0(\frac{r_e}{r_e&plus;h})^2$$" title="$$g_h=g_0(\frac{r_e}{r_e+h})^2$$" /></a>
Where

gh is the gravitational acceleration at height h above sea level.
re is the Earth's mean radius.
g0 is the standard gravitational acceleration.
The formula treats the Earth as a perfect sphere with a radially symmetric distribution of mass; a more accurate mathematical treatment is discussed below(from wikipedia).
## [Code](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ch2.py)
--------------------
## Results and Analysis
----------

**1.Use the adiabatic model of air density**
 - when we ignore the air resistance. 
![Fig2](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/2-2.png)
 - when we consider the air resistance and air density.
 ![Fig1](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/2-1.png)
When we consider  air resistance,the trajectories change a lot.
The altitude the cannon can reach fall. 
Compare these two pic,we can see cannon's range reduce a lot .
> - ignore air resistance
![FIG](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/2-1range.png)
 45.0 50049.491150831855
> - cosider air densitr
![fig4](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/2-2range.png)
43.199999999999996 24523.790443161008
( numbers under the plot are the maximum range and the launch angle to achieve it.)
---------------------

The maximum range reduce from 50049.49 to 24523.79(about51.0%)
The launch angle to achieve it also become smaller(from 45.0 to 43.2)


----------


**2.Incorporate the effects of the temperature**
> - 253K
 ![Fig5](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/253.png)
> - 303K
![FIg6](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/303.png)
Assume that the temperature in winter is 253K and the summer temperature is 303K.
The altitude the cannon can reach fall in summer .
Compare these two pic,we can see cannon's range reduce .
> - 253K
 ![FIG7](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/253range.png)
 > - 303K
 ![fig8](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/303range.png)
( numbers under the plot are the maximum range and the launch angle to achieve it.)
-----------------------

The maximum range reduce from30320.25to 24194.66 in summer.(about20.2%).However,both range in winter and summer fall a lot compared with 300K.
The launch angle to achieve it in winter is 43.2 which is closed to reference temperature.The angle in summer is 45.0 which is closed to the ideal condition.


**3.Incorporate the effects of g**
> - g
![Fig9](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/g.png)
> - gh
![fig10](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/gh.png)
> - g
![fig11](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/g%20range.png)
> - gh
![fig12](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/gh%20range.png).
---------------------------------

It seems that g has very little effect on the trajectory.




