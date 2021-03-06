import turtle as t
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