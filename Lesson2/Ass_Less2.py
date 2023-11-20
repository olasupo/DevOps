import os
os.system('clear')

#A.
#1 Create two numeric variables named X and Y.
#2. Print the word “BIG” if the value of X is bigger than Y.
#3. Print the word “small” if the value of X is smaller than Y.
#B.
#1. Run a “for” loop 5 times.
#2. Print the iteration number every time.

print("****This Program Resolves Tasks A and B in Devops Course Assignment - Lesson 2***\n\n")
for i in range(5):
    print("-------This is Iteration " f"{i}" "-----------\n")
    try:
        x = int(input("Enter a value for X: "))
    except:
        print("Invalid value. Please try again")
    try:
        y = int(input("Enter a value for Y: "))
    except:
        print("Invalid value. Please try again")

    if (x > y):
        print(f"{x}" " is BIGGER than " f"{y}" "\n")
    else:
        print(f"{x}" " is SMALLER than " f"{y}" "\n")


print("****This Program Resolves Tasks C in Devops Course Assignment - Lesson 2***\n\n")

#C.
#1. Create a variable and initialize it with a number 1-4.
#2. Create 4 conditions (if-elif) which will check the variable value.
#3. Print a different season name for each number:
#For example:
#- 1 = summer
#- 2 = winter
#- 3 = fall
#- 4 = spring

lis_val = [3,1,2,4]

for i in lis_val:
    if (i == 4):
        print("Hurray, Its Spring")
    elif (i == 2):
         print("Wow!!!, Its Winter")
    elif (i == 1):
        print("Am Excited Its Summer")
    else:
        print("It must be Fall")


print("****This Program Resolves Tasks E in Devops Course Assignment - Lesson 2***\n\n")

#E.
#Write a program with variables holding the following:
#1. Your age.
#2. First letter of your last name.
#3. Current shekels-dollar currency.
#4. Did you flew abroad (true/false)
#5. Your apartment number.
#● Print all variables.
#● Add the currency(3) to your age(1), and check the result.

profile = {"age":39,"fl_of_lastName":"O","Shek_to_dollar":0.27,"Apartment_nos":118}

print (profile)
print ("\n\n")
print ("The below is my profile")



for i,j in profile.items():
    print(f"{i}" " is: " f"{j}")
    
