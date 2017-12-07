# Electric Potentials 

Problem 5.3

## Bacground

The reigons of space that do not contain any electric charges,the potential obeys Laplace's equation(PDE).We'll use the **relaxation method** to solve the equation numerically.After the approximaton we get the value of the potential at any point is the average of potential at all of the neighbor points(assume that the step sizes along every axis are equal).If we know the value at boundaries ,we make an initial guess for the solution.Then calculate an improved guess by the relation we get.Then repeat the procedure.This iterative process continues until satisfy some conditions.This approach is called the relaxation method.The algorithm ,our textbook says, is known as the Jacobi method.

Problem5.3consider the potential between two parallel capacitor plates.And based on the symmetry ,we just need to calculate the result in one quadrant of the x-y plane.

![1](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/CH5/1.png)

## [Code](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/CH5/ch5.py)

## Results&Analysis

![2](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/CH5/2.png)

![2'](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/CH5/2.png)

![3](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/CH5/3.png)

![4](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/CH5/4.png)
## Acknowlegement

I want to thank Junyi Shangguan.Her method to set the potential is awesome!





