# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = int(weight)/float(height)**2
if round(BMI) <18.5:
    print(f"Your BMI is {round(BMI)}, you are underweight.")
elif round(BMI) >18.5 and round(BMI) <25:
    print(f"Your BMI is {round(BMI)}, you have a normal weight.")
elif round(BMI) >25  and round(BMI) <30:
    print(f"Your BMI is {round(BMI)}, you are slightly overweight.")
elif round(BMI) >30  and round(BMI) <35:
    print(f"Your BMI is {round(BMI)}, you are obese.")
else:
    print(f"Your BMI is {round(BMI)}, you are clinically obese.")