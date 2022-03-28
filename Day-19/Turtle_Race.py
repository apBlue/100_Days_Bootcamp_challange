from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


tim = Turtle(shape="turtle",)
tim.color(colors[0])
tim.penup()
tim.goto(x=-230, y=-100)

jim = Turtle(shape="turtle")
jim.color(colors[1])
jim.penup()
jim.goto(x=-230, y=-60)

dim = Turtle(shape="turtle")
dim.color(colors[2])
dim.penup()
dim.goto(x=-230, y=-20)

kim = Turtle(shape="turtle")
kim.color(colors[3])
kim.penup()
kim.goto(x=-230, y=20)

him = Turtle(shape="turtle")
him.color(colors[4])
him.penup()
him.goto(x=-230, y=60)

lee = Turtle(shape="turtle")
lee.color(colors[5])
lee.penup()
lee.goto(x=-230, y=100)

screen.exitonclick()