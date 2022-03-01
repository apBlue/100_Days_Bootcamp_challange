#Write your code below this line 👇






import math
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height, width, cover):
    calc=math.ceil((test_h*test_w)/coverage)
    print(f"You'll need {calc} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage)