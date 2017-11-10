# Chapter_three_chaos_section3.7

Problem 3.31*

## Background

Here we consider the problem of a ball moving without friction on a horizontal table.Imagine there are walls at the edges of table that reflect the ball perfectly and there is no frictional force between the ball and the table.We will ignore any complications associated with the momentum of the ball.

Between the collisions the motion of the ball is very simple.The key part of the program is the treatment of collisons.The way our textbook recommends can save some work for my computer,but I just took a smaller step at the beginning and then corrected the coordinate by the way I learned from a former student.

In this section,we take the **table shape** as stadium shape.Imagine a circular table of radius r=1.Cut the table along the x axis and pull the two semicircular halves apart along y axis, a distance 2alpha*r.Then fill in with straight segments.

Problem 3.31 consider a circular interior wall located in the table.



## [Codes]()

## Results&Analysis

1.alpha=0&alpha=0.01

---



Trajectory

![1]()

 The corrosponding phase-space plot(y=0)

![2]()



2.with a circular interior wall located in the center

---

Trajectory&phase-space plot

![3]()

![4]()

3.with a circular interior wall located slightly off-center

![5]()

![6]()

----

 When the parameters above are equal to some other value,the plots go crazy!I think the way to solve it is to figure out a better way to deal with the collision.









