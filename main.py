from turtle import *

from init import init
from santa import santa_claus
from snow import draw_snow
from star import draw_star
from tree import draw_tree
from write import merry_christmas

width, height, screen = init()
draw_tree()
draw_star()
santa_claus()
merry_christmas()
draw_snow(width, height, screen)

hideturtle()
done()
