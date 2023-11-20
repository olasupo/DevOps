def task2():
    print("****This Program Resolves Tasks C in Devops Course Assignment - Lesson 2***\n\n")

    # C.
    # 1. Create a variable and initialize it with a number 1-4.
    # 2. Create 4 conditions (if-elif) which will check the variable value.
    # 3. Print a different season name for each number:
    # For example:
    # - 1 = summer
    # - 2 = winter
    # - 3 = fall
    # - 4 = spring

    lis_val = [3, 1, 2, 4]

    for i in lis_val:
        if (i == 4):
            print("Hurray, Its Spring")
        elif (i == 2):
            print("Wow!!!, Its Winter")
        elif (i == 1):
            print("Am Excited Its Summer")
        else:
            print("It must be Fall")