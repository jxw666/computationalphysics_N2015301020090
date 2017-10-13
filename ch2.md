


> Written with [StackEdit](https://stackedit.io/).
# Chapter_two_section2.2


----------


## The Trajectory of a Cannon Shell
------------------------------------
Consider a projectile such as a shell shot by a cannon.If we ignore air resistance,the equation of motions can be obtained from Newton's second law.
$$ \frac{d^2x}{dt^2}=0$$
$$\frac{d^2y}{dt^2}=-g$$
x and y are horizontal and vertical coordinates of the projectile.
These are second-order differential equations.If we recasting the equations in the following way.
$$\frac{dx}{dt}=v_x$$
$$\frac{dv_x}{dt}=0$$
$$\frac{dy}{dt}=v_y$$
$$\frac{dv_y}{dt}=-g$$
We can use Euler method to solve the problem.Then we add air resistance, air density,temperature,gravitational acceleration etc to the model to approach the realistic motion of the cannon and find out how much these factors affect the model.

1.We will assume that the magnitude of the drag force on cannon shell is give by 
$$F_{drag}=-B_2v^2$$
where$v=\sqrt{ v_x^2+v_y^2}$is the speed of the shell.
$$F_{drag,x}=-B_2vv_x$$
$$F_{drag,y}=-B_2vv_y$$
2.Air resistance is propotional to the density of the air,so the drag force at high altitude will be less.Treat the atmosphere as an adiabatic ideal gas which leads to that the density depends on altitude according to
$$\rho=\rho_0(1-\frac{ay}{T_0})^\alpha$$
We replace $B_2$with$B_2\rho/\rho_0$.
$a\approx6.5\times{10^-}^3$K/m,$T_0$is the sea level temperature,$\alpha\approx2.5$for air

3.Further incorporate the effects off the variation of the ground temperature by replacing$B_2$by$B_2^{ref}(T_0/T_{ref})^\alpha$
$T_{ref}=300K$,$B_2^{ref}/m=4\times10^{-5}m^{-1}$

4.Gravity decreases with altitude as one rises above the Earth's surface because greater altitude means greater distance from the Earth's centre.
$$g_h=g_0(\frac{r_e}{r_e+h})^2$$

Where

$g_h$ is the gravitational acceleration at height h above sea level.
$r_e$ is the Earth's mean radius.
$g_0$ is the standard gravitational acceleration.
The formula treats the Earth as a perfect sphere with a radially symmetric distribution of mass; a more accurate mathematical treatment is discussed below(from wikipedia).
##[Code]()
--------------------
##Results and Analysis
----------

###1.Use the adiabatic model of air density
![Fig1]()
 - when we ignore the air resistance. 
 - when we consider the air resistance and air density.

When we consider  air resistance,the trajectories change a lot.

> -  The altitude the cannon can reach fall. 
> -   Compare these two pic,we can see cannon's range reduce a lot .
 ![FIG]()
( numbers under the plot are the maximum range and the launch angle to achieve it.)
> - The maximum range reduce from 50049.49 to 24523.79(about51.0%)
> - The launch angle to achieve it also become smaller(from 45.0 to 43.2)


----------


###2.Incorporate the effects of the temperature
 ![Fig2]()
Assume that the temperature in winter is 253K and the summer temperature is 303K.
> -  The altitude the cannon can reach fall in summer .
> -   Compare these two pic,we can see cannon's range reduce .
 ![FIG]()
( numbers under the plot are the maximum range and the launch angle to achieve it.)
> - The maximum range reduce from30320.25to 24194.66 in summer.(about20.2%).However,both range in winter and summer fall a lot compared with 300K.
> - The launch angle to achieve it in winter is 43.2 which is closed to reference temperature.The angle in summer is 45.0 which is closed to the ideal condition.


###3.Incorporate the effects of g
![Fig3]()
It seems that g has very little effect on the trajectory.


