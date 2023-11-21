"""
O.
Write a program with the following:
1. Function that gets a number from the user (using input).
2. Function that receive the number from the first method, and computes the sum of the
digits the integer (e.g. 25 = 7, 2+5=7)
"""
def inputvalue():
    x = int(input("Please enter an integer value: "))
    y = int(input("Please enter a second integer value: "))
    return x, y
def compute_sum():
    a,b = inputvalue()
    sump = a + b
    print(f"The Sum of {a} and {b} is {sump}")

if __name__ == "__main__":
    compute_sum()
