from turtle import *

from init import init


def santa_claus():
    goto(-200, 0)
    penup()
    color('#CDAF95', '#CDAF95')
    pendown()
    begin_fill()
    circle(-50)
    end_fill()
    # 第二个圆
    penup()
    goto(-200, -50)
    color('red', 'red')
    pendown()
    begin_fill()
    circle(-60)
    end_fill()
    # 围巾部分
    # 第一部分
    penup()
    goto(-200, -80)
    pendown()
    color('grey', 'red')
    begin_fill()
    forward(48)
    circle(8, 180)
    forward(96)
    circle(8, 180)
    forward(48)
    end_fill()
    # 第二部分
    penup()
    goto(-248, -80)
    pendown()
    begin_fill()
    setheading(-90)
    forward(10)
    circle(-30, 30)
    circle(10, 60)
    circle(-50, 20)
    setheading(0)
    forward(20)
    setheading(90)
    circle(50, 20)
    circle(-10, 60)
    circle(30, 30)
    setheading(90)
    forward(10)
    end_fill()
    # 帽子部分
    # 帽子底部
    penup()
    goto(-25 * 1.73 - 200, -25)
    color('grey', 'white')
    setheading(30)
    pendown()
    begin_fill()
    forward(50)
    circle(5, 180)
    forward(50)
    circle(5, 180)
    end_fill()
    # 帽子中间
    penup()
    circle(5, -180)
    pendown()
    color('red', 'red')
    begin_fill()
    setheading(90)
    forward(50)
    right(120)
    forward(50)
    end_fill()
    # 帽子顶部
    penup()
    forward(-50)
    left(30)
    color('white', 'white')
    pendown()
    begin_fill()
    circle(5)
    end_fill()
    # 面部
    # 两个大眼睛
    penup()
    goto(-220, -35)
    pencolor('black')
    pendown()
    dot(10)
    penup()
    goto(-180, -35)
    pencolor('black')
    pendown()
    dot(10)
    # 鼻子
    penup()
    goto(-205, -45)
    color('grey', 'yellow')
    pendown()
    begin_fill()
    forward(10)
    circle(3, 180)
    forward(10)
    circle(3, 180)
    end_fill()
    # 嘴巴
    penup()
    goto(-210, -50)
    pencolor('red')
    pensize(3)
    setheading(-90)
    pendown()
    circle(10, 180)
    # 身体部分
    # 扣子
    penup()
    goto(-200, -100)
    pencolor('black')
    dot(10)
    penup()
    goto(-200, -120)
    pencolor('black')
    dot(10)
    penup()
    goto(-200, -140)
    pencolor('black')
    dot(10)
    # 两只手臂，左手
    penup()
    goto(-260, -100)
    pencolor('brown')
    pensize(5)
    setheading(120)
    pendown()
    forward(50)
    pencolor('white')
    forward(-10)
    right(60)
    forward(10)
    # 两只手臂，右手
    penup()
    goto(-140, -100)
    pencolor('brown')
    pensize(5)
    setheading(60)
    pendown()
    forward(50)
    pencolor('white')
    forward(-10)
    right(-60)
    forward(10)
    hideturtle()

    # 左脚
    penup()
    goto(-220, -165)
    pencolor('brown')
    pensize(10)
    setheading(270)
    pendown()
    forward(80)
    pencolor('white')
    forward(-10)
    right(60)
    forward(10)
    # 右脚
    penup()
    goto(-180, -165)
    pencolor('brown')
    pensize(10)
    setheading(-90)
    pendown()
    forward(80)
    pencolor('white')
    forward(-10)
    right(-60)
    forward(10)
    hideturtle()


if __name__ == '__main__':
    init()
    santa_claus()
    done()
