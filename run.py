

def main_menu():
    """
    Displays the main menu options for the user
    to select in order to navigate the application.
    """
    print("---------------------------")
    print("Welcome to Health Ireland")
    print("---------------------------")
    print("Please select an option below.\n")

    print("(1) Body Mass Index BMI.")
    print("(2) Heart Rate.")
    print("(3) Waist to Hip Ratio ")
    print("(4) How it works.")

    while True:
        main_menu_ans = input("\n")
        if main_menu_ans not in ("1", "2", "3", "4",):
            print("Invalid input.")
            print("Please choose an option between 1 and 4.")
        else:
            break

    if main_menu_ans == ("1"):
        bmi()
    elif main_menu_ans == ("2"):
        heart_ratio()
    elif main_menu_ans == ("3"):
        waist_hip()
    elif main_menu_ans == ("4"):
        how_it_work()
    

def bmi():
    print("Welcome to BMI")

    input("Press enter to return to menu\n")
    main_menu()

def heart_ratio():
    print("Welcome to BMI")

    input("Press enter to return to menu\n")
    main_menu()

def waist_hip():
    print("Welcome to waist to hip ratio")

    input("Press enter to return to menu\n")
    main_menu()

def how_it_work():
    print("How this works")

    print("explain how this works.\n")

    input("Press enter to return to menu\n")
    main_menu()


main_menu()