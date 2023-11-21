import os
import time
from task1 import task1
from task2 import task2
from task4 import task4
from task5 import printHello, calculate
from task6 import print_name_args, print_halfof
from task7 import add_num, concat_strings

def clearscrn():
    if os.environ.get('TERM'):
        os.system('clear' if os.name == 'posix' else 'cls')
    else:
        print("TERM environment variable is not set.")
    time.sleep(5)


def main():
    print("Program Start")
    time.sleep(5)
    task1()
    clearscrn()
    task2()
    clearscrn()
    task4()
    clearscrn()
    printHello()
    time.sleep(5)
    int1 = int(input("Please enter the first value: "))
    int2 = int(input("Please enter the Second value: "))
    calculate(int1,int2)
    str1 = input ("Please input your first name: ")
    str2 = input("Please input your Last name: ")
    print_name_args(str1)
    print_halfof(int1)
    add_result = add_num(int1, int2)
    print(f"Sum of {int1} and {int2} is : {add_result}")
    str_result = concat_strings(str2,str1)
    print(f"Your Full name is {str_result}")


if __name__ == "__main__":
    clearscrn()
    main()
