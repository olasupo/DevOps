import os
import time
from task1 import task1
from task2 import task2
from task4 import task4
from task5 import printHello,calculate


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
    x = int(input("Please enter the first value: "))
    y = int(input("Please enter the Second value: "))
    calculate(x,y)


if __name__ == "__main__":
    clearscrn()
    main()
