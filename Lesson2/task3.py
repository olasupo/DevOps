def task3():

    print("****This Program Resolves Tasks E in Devops Course Assignment - Lesson 2***\n\n")

    # E.
    # Write a program with variables holding the following:
    # 1. Your age.
    # 2. First letter of your last name.
    # 3. Current shekels-dollar currency.
    # 4. Did you flew abroad (true/false)
    # 5. Your apartment number.
    # ● Print all variables.
    # ● Add the currency(3) to your age(1), and check the result.

    profile = {"age": 39, "fl_of_lastName": "O", "Shek_to_dollar": 0.27, "Apartment_nos": 118}

    print(profile)
    print("\n\n")
    print("The below is my profile")

    for i, j in profile.items():
        print(f"{i}" " is: " f"{j}")

    vCurr = profile["Shek_to_dollar"]
    profile["age"] = profile["age"] + vCurr
    return profile