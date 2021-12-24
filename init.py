from turtle import *


def init():
    width, height = 1000, 600
    screen = Screen()
    title("Merry Christmas")
    bgcolor("black")
    speed("fastest")  # 定义速度
    setup(1200, 800, startx=None, starty=None)
    return width, height, screen
