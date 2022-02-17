# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
count=0
items=0
for i in student_heights:
    count=count+i
    items+=1
avg =count/items
print(round(avg))

#Write your code below this row 👇

