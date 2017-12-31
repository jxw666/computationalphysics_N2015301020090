Different levels of Koch curve can be obtained by this code
```import turtle as t
def koch(level, size):
    if level == 0:
        t.forward(size)
        return
    else:
        for angle in [60, -120, 60, 0]:
           koch(level-1, size/3)
           t.left(angle)

t.hideturtle()
t.up()
t.setx(-t.window_width()/2)
t.down()
t.speed(0)

koch(5,t.window_width())

t.exitonclick() 
```

set level= 1,2,3,4,5
![1](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/final/屏幕快照%202017-12-31%2016.54.53.png)
![2](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/final/屏幕快照%202017-12-31%2016.55.12.png)
![3](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/final/屏幕快照%202017-12-31%2016.55.29.png)
![4](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/final/屏幕快照%202017-12-31%2016.56.19.png)
![5](https://github.com/jxw666/computationalphysics_N2015301020090/blob/master/final/屏幕快照%202017-12-31%2016.57.24.png)
