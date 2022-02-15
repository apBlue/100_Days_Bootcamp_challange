# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_caps_name1= name1.lower()
small_caps_name2= name2.lower()

T1 =small_caps_name1.count('t')
R1 =small_caps_name1.count('r')
U1 =small_caps_name1.count('u')
E1 =small_caps_name1.count('e')

L1 =small_caps_name1.count('l')
O1 =small_caps_name1.count('o')
V1 =small_caps_name1.count('v')
E3 =small_caps_name1.count('e')

T2 =small_caps_name2.count('t')
R2 =small_caps_name2.count('r')
U2 =small_caps_name2.count('u')
E2 =small_caps_name2.count('e')

L2 =small_caps_name2.count('l')
O2 =small_caps_name2.count('o')
V2 =small_caps_name2.count('v')
E4 =small_caps_name2.count('e')

Total1= T1 + T2 + R1 + R2 + U1 + U2 + E1 + E2
Total2= L1 + L2 + O1 + O2 + V1 + V2 + E3 + E4
Total = str(Total1)+str(Total2)

if int(Total) <=10 or int(Total) >= 90:
    print(f"Your score is {Total}, you go together like coke and mentos.")
elif int(Total) >=40 and int(Total) <= 50:
    print(f"Your score is {Total}, you are alright together.")
else:
    print(f"Your score is {Total}.")

######################################################################
#the strings were added in the solution which i didnt think of and made the solution shorter
#combined_string= name1+name2


