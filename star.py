import random
import turtle
from turtle import *
from init import init


def star(r, x, y, size):
    seth(r)
    pensize(2)
    pencolor("yellow")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    fillcolor("yellow")
    for i in range(5):
        left(72)
        fd(size)
        right(144)
        fd(size)
    end_fill()


def draw_star():
    star(random.randint(0, 180), 340, -150, 10)
    star(random.randint(0, 180), 50, -150, 10)

    star(random.randint(0, 180), 80, -70, 10)
    star(random.randint(0, 180), 320, -70, 10)

    star(random.randint(0, 180), 110, -10, 10)
    star(random.randint(0, 180), 290, -10, 10)

    star(random.randint(0, 180), 260, 50, 10)
    star(random.randint(0, 180), 140, 50, 10)

    star(random.randint(0, 180), 220, 110, 10)
    star(random.randint(0, 180), 180, 110, 10)

    star(0, 195, 180, 20)
    penup()


if __name__ == '__main__':
    init()
    draw_star()
    turtle.done()
