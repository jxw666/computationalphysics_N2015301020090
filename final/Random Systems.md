# Random Systems

Name:贾雪巍  

Student number:201530120090

##Random Walks&Diffusion

1.Random walk is a model describes a process in which a walker moves one step a time,according to certain rules.The simplest situation involves a walker that is able to take steps of length unity along a line.The walker begins at the origin.Each step can be towards right or left with equal probability.We can stimulate the displacement of the walker after N steps(time).Use the Monte Carlo sampling.First generate a random number between 0 and 1 and determine the direction of the step.We can also calculate the mean displacement and the average of square of the displacement and the 2 or 3 dimensional cases.

2.Random walks are equivalent to diffusion.Consider the density of particles(walkers).The density is propotional to the probablity per unit volume P(x,y,z,t).We'll see the density and P obey the same equation.On a simple cubic lattice,the total probablity to arrive at (i,j,k) is P(i,j,k,n)=1/6[P(i+1,j,k,n-1)+P(i,j,k,t)+P(i-1,j,k,n-1)+P(i,j+1,k,n-1)+P(i,j-1,k,n-1)+P(i,j,k-1,n-1)].Rearranging and taking the continuum limit, it suggests that

<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;P(x,y,z,t)}{\partial&space;t}=D&space;\nabla^2P(x,y,z,t)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;P(x,y,z,t)}{\partial&space;t}=D&space;\nabla^2P(x,y,z,t)" title="\frac{\partial P(x,y,z,t)}{\partial t}=D \nabla^2P(x,y,z,t)" /></a>

If we know the initial distribution we'll get the solution at future times.

3. Recall that the statistical definition of entropy is 

   <a href="http://www.codecogs.com/eqnedit.php?latex=S=-\sum_{i}P_ilnP_i" target="_blank"><img src="http://latex.codecogs.com/gif.latex?S=-\sum_{i}P_ilnP_i" title="S=-\sum_{i}P_ilnP_i" /></a>

   Divide the system into a square grid.State i correspond to the particles in the cell i at any particular time and Pi is the probability of finding the particle in this cell at particular time.

   ## [Codes]()

   ## Results&Anylasis

   1.One dimensional random walk

   ![1](/Users/apple/Desktop/计算物理final/1.png)

Here I draw two walker's displacements versus time

The following figures are get from the average of 5000 walkers.

![2](/Users/apple/Desktop/计算物理final/2.png)

We can see that the mean displacement is close to zero as expected.Because it's equal likely to go left and right.

![3](/Users/apple/Desktop/计算物理final/4.png)

We see that the averages of the square of the displacement is well described by a straight line.The RED line is the stimulation of the dots.Y=0.989960976898X+0.315882666666.

For a free particle x=vt.So a random walker escapes from the origin more slowly(square root of t).

N steps one dimensional random walk is a **Binomial distribution.** From the math we have learned we can easily know that

<a href="http://www.codecogs.com/eqnedit.php?latex=\sigma_n^2=\overline{(\Delta&space;n)^2}=Npq" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\sigma_n^2=\overline{(\Delta&space;n)^2}=Npq" title="\sigma_n^2=\overline{(\Delta n)^2}=Npq" /></a>

Our textbook,to explain this result,suggests that we can write the position xn as a sum of n separate i th step,then write the square displacement.Finally we reach that the slope of the curve is 1.

Use the same method the average of x^4 is

<a href="http://www.codecogs.com/eqnedit.php?latex=<x^4>=3n^2-2n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?<x^4>=3n^2-2n" title="<x^4>=3n^2-2n" /></a>

here's the result I got

![4](/Users/apple/Desktop/计算物理final/4.png)



​			
​		The RED line is y=2.94218790678x^2 -6.59728183121x+ 63.7786218824 .I think <x4> can be very large (we can see from the figure).So the difference between the ideal one and the result I got is acceptable.

2.one dimensional but random length

![5](/Users/apple/Desktop/计算物理final/5.png)

![6](/Users/apple/Desktop/计算物理final/6.png)

The mean average is also close to zero.

![7](/Users/apple/Desktop/计算物理final/7.png)

The RED line is y=0.346211421082x -0.0849232487711

![8](/Users/apple/Desktop/计算物理final/8.png)

The RED line is y=2.94218790678x^2 -6.59728183121x+ 63.7786218824

3.two&three dimensions

![9](/Users/apple/Desktop/计算物理final/9.png)

![10](/Users/apple/Desktop/计算物理final/10.png)

The stimulation result is y=1.01732169697x+0.22355830303

![11](/Users/apple/Desktop/计算物理final/11.png)



![12](/Users/apple/Desktop/计算物理final/12.png)

The stimulation result is y=1.62234589019 x-0.981333454546

4.From the **central limit theorem** we know for large number particles their distributions should approximate to a Gaussian distribution.You can also verify that a Gaussian distribution obeys the diffusion equation.

Set all particle at the center at the beginning, then let them do random walk in one dimension .For 1000 walkers after 10,100,500,2000,4000,8000 time steps we get

![13](/Users/apple/Desktop/计算物理final/13.png)

We can see how the particles diffuse in this way without knowing the details of particles' motion.

5.Consider two dimension random walk problem. First we set a number of particle in the center area which is shaped as a square. Then let them do random walk to up,down,left and right in four directions. The only limit is once they are reach the edge of the area they can not pass it. Then we observe the whole random particle picture in different time.

![14](/Users/apple/Desktop/计算物理final/14.png)

Then calculate the entropy we get

![entropy](/Users/apple/Desktop/计算物理final/entropy.png)

During the process th entropy increase and seemingly is going to approach a constant value.This illustrates how a closed system approaches equilibrium.

## Acknowledgement

1.Qiangyu,a former student of our computational course.I refered part of his codes,especially about the diffusion problem.

2.Wikipedia,Random walk

3.Computational Physics, Nicholas J. Giordano & Hisao Nakanishi 