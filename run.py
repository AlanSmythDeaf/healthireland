

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

    input("To return to the main menu, please press enter\n")
    main_menu()


def waist_hip():
    """
    Displays section call waist to hip ratio
    """
    print("Welcome to waist to hip ratio")

    gender_choice = input("Please chose your gender? (Type 'male' or 'female'): ")

    if gender_choice.lower() == 'male':
        m_waist = float(input("Please enter your waist: "))
        m_hip = float(input("Please enter your hip: "))
        male_waist_to_hip = m_waist / m_hip
    elif gender_choice.lower() == 'female':
        fm_waist = float(input("Please enter your waist: "))
        fm_hip = float(input("Please enter your hip: "))
        female_waist_to_hip = fm_waist / fm_hip
    else:
        print("Invalid choice. Please enter 'male' or 'female'.")
        return

    if gender_choice == "male":
        if male_waist_to_hip <= 0.91:
            print(f"Your waist-to-hip ratio is {male_waist_to_hip:.2f}, which means you are in the low-risk category.")
        elif 0.92 < male_waist_to_hip < 0.98:
            print(f"Your waist-to-hip ratio is {male_waist_to_hip:.2f}, which means you are in the medium-risk category.")
        else:
            print(f"Your waist-to-hip ratio is {male_waist_to_hip:.2f}, which means you are in the high-risk category.")

    if gender_choice =="female":
        if female_waist_to_hip <= 0.81:
            print(f"Your waist-to-hip ratio is {female_waist_to_hip:.2f}, which means you are in the low-risk category.")
        elif 0.82 < female_waist_to_hip < 0.89:
            print(f"Your waist-to-hip ratio is {female_waist_to_hip:.2f}, which means you are in the medium-risk category.")
        else:
            print(f"Your waist-to-hip ratio is {female_waist_to_hip:.2f}, which means you are in the high-risk category.")

    input("To return to the main menu, please press enter\n")
    main_menu()

def how_it_work():
    print("How this works \n")

    print("------------")
    print("Body Mass Index\n")
    print("Calculate your body mass index to find out")
    print("if you are a healthy weight area.")
    print("Not sure about your weight in kilogram or height in Meter,")
    print("you can use the the converter from your preference")
    print("https://www.unitconverters.net/length-converter.html")
    print("------------\n")

    print("------------")
    print("Heart.\n")
    print("Your target heart rate is a range of numbers that")
    print("reflect how fast your heart should be beating when you exercise.")
    print("------------\n")

    print("------------")
    print("Waist to Hip Ratio\n")
    print("compares your waist measurement to your hip measurement")
    print("Higher ratios can mean you have more fat around your waist.")
    print("Not sure about your waist or hip in centremeters, you can")
    print("use the the converter from your preference to cm")
    print("https://www.unitconverters.net/length-converter.html")
    print("------------\n")

    input("To return to the main menu, please press enter\n")
    main_menu()

def main():
    """
    Runs necessary functions at the start of the program.
    """
    main_menu()

main()