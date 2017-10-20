


> Written with [StackEdit](https://stackedit.io/).
# Chapter_two_section2.3&4
--------------------

贾雪巍 2015301020090
problem2.17 Kunckleball

--------------------------
## Throwing a Baseball
-----------------------------------

## Background
The basic equations of motion of for a baseball are the same as those of the cannon shell,with a few deflections, and we will again use the Euler method in our stimulations.Here are the changes we made on the model.
**1**.The force on a baseball due to air resistance is given by the same form as cannon shell's.But the drag coeffcient is a function of v,and is depent on the ball conditions.(P33.fig 2.6)At high speeds or when throwing a rough ball the flow become turbulent.We take 

<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{B_2}{m}=0.0039&plus;\frac{0.0058}{1&plus;exp[(v-v_d)/\Delta]}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{B_2}{m}=0.0039&plus;\frac{0.0058}{1&plus;exp[(v-v_d)/\Delta]}" title="\frac{B_2}{m}=0.0039+\frac{0.0058}{1+exp[(v-v_d)/\Delta]}" /></a>
<a href="http://www.codecogs.com/eqnedit.php?latex=v_d=35m/s,\Delta=5m/s" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_d=35m/s,\Delta=5m/s" title="v_d=35m/s,\Delta=5m/s" /></a>
**2**.The v in air resistance is the speed relative to the air. For a ball spinning about an axis perpendicular to the direction of travel,when add the drag force on different sides of the ball,there will be a net force perpendicular to the center of mass velocity called Magnus force.
<a href="http://www.codecogs.com/eqnedit.php?latex=F_M=S_0wv_x" target="_blank"><img src="http://latex.codecogs.com/gif.latex?F_M=S_0wv_x" title="F_M=S_0wv_x" /></a>
for baseball<a href="http://www.codecogs.com/eqnedit.php?wlatex=S_0/m\approx4.1\times10^{-4}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?S_0/m\approx4.1\times10^{-4}" title="S_0/m\approx4.1\times10^{-4}" /></a>.w is the angle velocity we assume w is a constant.
**3**.  Knuckleball.Baseball is not a total smooth ball.Since the drag force is greater for a smooth ball than for a rough ball,there will be an imbalance on the two sides of the ball,giving a net force in the direction of the rough side.If the ball rotates **slowly** as it moves so that the exposed stitches moves, the force changes direction.For simplicity we will assume that the ball spins about a vertical axis .The force is given approximately by the function

<a href="http://www.codecogs.com/eqnedit.php?latex=$$\frac{F_{lateral}}{mg}=0.5[sin(4\theta)-0.25sin(8\theta)&plus;0.08sin(12\theta)-0.025sin(16\theta)]$$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$$\frac{F_{lateral}}{mg}=0.5[sin(4\theta)-0.25sin(8\theta)&plus;0.08sin(12\theta)-0.025sin(16\theta)]$$" title="$$\frac{F_{lateral}}{mg}=0.5[sin(4\theta)-0.25sin(8\theta)+0.08sin(12\theta)-0.025sin(16\theta)]$$" /></a>


## [Code](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ch3.py)
--------------------

## Result&Analysis
---------------------
1.different center of mass velocity
(I choose this initial angular orientation and angular velocity because it looks ok，others go crazy......-_-#)
![FIG1](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ball1.png)
![fig2](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ball2.png)
 **When change center of mass velocity,the curve shape doesn't change.**
 **The largest velocity has the longest range.**

---------------------------
2.different w
![fig3](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ball3.png)
![fig4](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ball4.png)
**pi/5 has the longest range.
From the x-z figure,I can approximately see how a Knucleball moves.It's hard to say where it lands.**

----------------
3.different theta
I abandon the curves with x<0
![fig5](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ball5.png)
![fig6](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/ball6.png)
**1.8pihas the longest range.Still can't tell how this works.It is not consistent with my experience -_-#**
## Defect
The air resistance shouldn't have x<0(??),I think the forces in this model are wrong.
The actual the baseball motion may not have a horizontal velocity.Its spin may be more complicated.And the forces in this model are just approximations which can make our calculaton easier. 
## The way to catch a knuckleball is to wait until it stops rolling and pick it up.--Bob Uecker哈哈哈
