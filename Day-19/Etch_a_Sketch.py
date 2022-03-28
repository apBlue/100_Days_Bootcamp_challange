from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backwords():
    tim.backward(10)

def turn_clockwise():
    tim.right(10)

def turn_anticlockwise():
    tim.left(10)

def clear_board():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwords)
screen.onkey(key="a", fun=turn_anticlockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_board)
screen.exitonclick()
