def task1():
    # A.
    # 1 Create two numeric variables named X and Y.
    # 2. Print the word “BIG” if the value of X is bigger than Y.
    # 3. Print the word “small” if the value of X is smaller than Y.
    # B.
    # 1. Run a “for” loop 5 times.
    # 2. Print the iteration number every time.

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