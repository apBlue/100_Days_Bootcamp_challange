#sit where you can try out the code at: (https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)


#Hurdle_1

def robot():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()


for i in range(6):
    robot()

#Hurdle_2

def robot():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

while not at_goal():
    robot()

#Hurdle_3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def for_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        for_wall()
    else:
        move()

#Hurdle_4


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def robot():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def for_wall():
    turn_left()
    move()
    turn_right()
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        for_wall()
    else:
        move()


#Final Project

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()



#need to tackle the infinite loop problem
