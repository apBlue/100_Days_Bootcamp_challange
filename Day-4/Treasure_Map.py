# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# horizontal = int(position[0])
# vertical = int(position[1])
# map[vertical - 1][horizontal - 1] = "X"
numbers=list(position)
lets_change1=int(numbers[0])-1
lets_change2=int(numbers[1])-1
map[lets_change1][lets_change2]="X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")