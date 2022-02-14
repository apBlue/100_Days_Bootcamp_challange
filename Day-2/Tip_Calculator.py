#Tip Calculator

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

Pay = (total_bill*(tip_percentage/100+1))/people

print("Each person should pay: ", round(Pay, 2))