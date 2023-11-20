from task3 import task3

def task4():
    profile=task3()
    print("New Age is ", profile['age'])

    """
    F.
    Create a program which uses input with the following:
    1. Ask user for his phone number
    2. Print the words “phone number” and the phone number the user entered.
    """

    phone_number = int(input("Please Enter Your Phone Number: "))

    print("Your Phone Number is : ", phone_number)