import turtle
def draw(t, a):
    if t == 1:
        turtle.forward(a)
        return
    draw(t-1, a/3)
    turtle.right(60)
    draw(t-1, a/3)
    turtle.left(120)
    draw(t-1, a/3)
    turtle.right(60)
    draw(t - 1, a / 3)

if __name__ == '__main__':
    turtle.mode('logo')
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.clear()
    turtle.up()
    turtle.goto(-130, -85)
    turtle.seth(90)
    turtle.down()
    for i in range(3):
        draw(4, 300)
        turtle.left(120)