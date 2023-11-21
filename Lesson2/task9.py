"""
K.
Create a program which will get a list of numbers and prints the sum of all items.

"""

list_of_numbers = []

while True:
    number = int(input("Please enter a Random Integer Number: "))
    if number == 999:
        break
    else:
        list_of_numbers.append(number)
print(list_of_numbers)

sum=0
for i in list_of_numbers:
    sum = sum+i

print(sum)



#The loop takes in Students name and populates a list and Quits when the user enters 'q'
list_of_students =[]
while True:
    student = input("Please Enter The Name of A Student: ")
    if student == 'q':
        break
    else:
        list_of_students.append(student)

print(list_of_students) #prints the list of students

list_of_students.pop() #removes the last student on the list

print(list_of_students)

#Removes Students whose name length is equal to that of a randomly inputted number
rand_num = int(input("Please input a random number: "))
for i in list_of_students:
    if len(i)==rand_num:
        x=list_of_students.index(i)
        list_of_students.pop(x)
list_of_students.pop(1)

print(list_of_students)