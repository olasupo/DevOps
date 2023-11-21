"""
Q.
Write a Python program to get the smallest number from a list.

"""

lst = [30,20,5,7,10,40,6,8,9]

smallest = 20

for i in lst:
    if i< smallest:
        smallest = i

print (f"The Smallest Number on the List is {smallest}")