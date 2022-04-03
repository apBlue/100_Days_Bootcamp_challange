from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_positions = [(0,0), (-20,0), (-40,0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)


# tim =Turtle()
# tim.color("white")
# tim.shape("square")
#
# tim.goto(x=0, y=0)
#
# jim =Turtle()
# jim.color("white")
# jim.shape("square")
# jim.goto(x=-20, y=0)
#
# him =Turtle()
# him .color("white")
# him .shape("square")
# him .goto(x=-40, y=0)
#

screen.exitonclick()
