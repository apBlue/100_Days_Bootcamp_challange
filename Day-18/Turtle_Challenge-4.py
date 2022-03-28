import turtle as t
import random
from turtle import Screen

import turtle as t
import random
t.speed("fastest")
tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)



"""
############My solution ################

t.colormode(255)
t.speed("fastest")



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color= (r, g, b)
    return color

def draw_circle(num_sides):
        t.circle(100)
        t.right(num_sides)

for shape_side_n in range(int(360/78)):
    t.color(random_color())
    draw_circle(int(360/78))


my_screen= Screen()
my_screen.exitonclick()
"""