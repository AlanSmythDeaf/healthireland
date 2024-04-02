

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
    """
    Calculates BMI based on user input for weight and height.
    """
    print("Welcome to the BMI Index")

    # Input height in meters between 1.00 to 2.44
    while True:
        try:
            height = float(input("Please enter your height in meters: "))
            if 1.00 <= height <= 2.44:
                break
            else:
                print(f"Please enter your height in meters between 1.00 and 2.44.")
        except ValueError:
            print("Input error, please enter a valid number for height.")

    # Input weight in kilograms between 35 to 199
    while True:
        try:
            weight = int(input("Please enter your weight in kilograms: "))
            if 35 <= weight < 199:
                break
            else:
                print(f"Please enter your weight in kg between 35 and 199.")
        except ValueError:
            print("Input error, please enter a valid number for weight.")

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine BMI category user are in
    if bmi <= 18.5:
        print(f"Your BMI is {bmi:.2f}, which means you are underweight.\n")
    elif 18.5 < bmi < 25:
        print(f"Your BMI is {bmi:.2f}, which means you are normal.\n")
    elif 25 <= bmi < 30:
        print(f"Your BMI is {bmi:.2f}, which means you are overweight.\n")
    else:
        print(f"Your BMI is {bmi:.2f}, which means you are obese.\n")
 
    input("Press enter to return to the main menu\n")
    main_menu()

def heart_ratio():
    """
    Displays section called Heart Ratio
    """    
    print("Welcome to Heart Ratio\n")
     # Input age in numbers between 0 - 100
    while True:
        try:
            user_input_heart = int(input("Please enter your age: "))
            min_value = 0
            max_value = 100
            if min_value <= user_input_heart <= max_value:
                heart_result = 206.9 - (0.67 * user_input_heart)
                print(f"Your maximum heart rate result is {heart_result} beats per minute.\n")
                break
            else:
                print(f"Please enter your age between {min_value} and {max_value}.\n")
        except ValueError:
            print("Invalid input, please enter a number.\n")

    input("Press enter to return to the main menu\n")
    main_menu()


def waist_hip():
    """
    Displays section call waist to hip ratio
    """
    print("Welcome to waist to hip ratio")

    input("Press enter to return to menu\n")
    main_menu()

def how_it_work():
    print("How this works")

    print("BMI Index.\n")
    print("Calculate your body mass index to find out if you are a healthy weight for your height.")
    print("Not sure about your height in Meter, you can use the link below from Meters to Feet")
    print("https://www.unitconverters.net/length/feet-to-meters.htm\n")

    print("Heart.\n")
    print("Your target heart rate is a range of numbers that reflect how fast your heart should be beating when you exercise.")

    input("Press enter to return to menu\n")


    main_menu()

def main():
    """
    Runs necessary functions at the start of the program.
    """
    main_menu()

main()