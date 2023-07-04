from turtle import *
from colorsys import *
bgcolor('black')
tracer(2)
pensize(3)
hideturtle()
h=0
def draw(angle, n):
    circle(n, 130)
    left(angle)
    circle(n, 180)
for i in range (100):
    c=hsv_to_rgb(h,1,1)
    h+=0.005
    pencolor(c)
    draw(90, i)
done()