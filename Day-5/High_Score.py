# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
score=0
for i in range(len(student_scores)):
    if score < student_scores[i]:
        score=student_scores[i]
    else:
        pass
print("The highest score in the class is: ", score)

##################################################################
"""
video solution:
for i in student_scores:
    if score <i:
        score=i
print("The highest score in the class is: ", score)
"""