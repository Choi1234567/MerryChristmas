from turtle import *
import random

from init import init


def draw_snow(width, height, screen):
    screen.delay(0)
    t = Turtle(visible=False, shape='circle')
    t.pencolor("white")
    t.fillcolor("white")
    t.penup()
    t.setheading(-90)
    t.goto(random.randint(-width // 2, width // 2), height / 2)
    stars = []
    for i in range(200):
        star = t.clone()
        s = random.random() / 3
        star.shapesize(s, s)
        star.speed(int(s * 10))
        star.setx(random.randint(-width // 2, width // 2))
        star.sety(height / 2 + random.randint(1, height))
        star.showturtle()
        stars.append(star)
    while True:
        for star in stars:
            star.sety(star.ycor() - 8 * star.speed())
            if star.ycor() < -height / 2:
                star.hideturtle()
                star.setx(random.randint(-width // 2, width // 2))
                star.sety(height / 2 + random.randint(1, height))
                star.showturtle()


if __name__ == '__main__':
    width, height, screen = init()
    draw_snow(width, height, screen)
