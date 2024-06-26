import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def main_menu():
    """
    Displays the main menu options for the user
    to select in order to navigate the application.
    """
    clear_tml()
    print("-------------------------")
    print(f"{Style.BRIGHT}Welcome to Health Ireland")
    print("-------------------------\n")
    print("Please select an option below and press enter.\n")

    print("(1) Body Mass Index BMI")
    print("(2) Heart Rate")
    print("(3) Waist to Hip Ratio")
    print("(4) How it works")

    while True:
        main_menu_ans = input("\n")
        if main_menu_ans not in ("1", "2", "3", "4",):
            print(f"{Fore.RED}Invalid input.")
            print("Please choose a number between 1 to 4.")
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
    clear_tml()
    print("------------------------")
    print(f"{Style.BRIGHT}Welcome to the BMI Index")
    print("------------------------ \n")

    # Input height in meters between 1.00 to 2.44
    while True:
        try:
            height = float(input("Please enter your height in meters: "))
            if 1.00 <= height <= 2.44:
                break
            else:
                print(f"{Fore.RED}Please enter your height in meters between "
                      "1.00 and 2.44.")
        except ValueError:
            print(f"{Fore.RED}Input error, please enter a valid number for "
                  f"height.")

    # Input weight in kilograms between 35 to 199
    while True:
        try:
            weight = float(input("Please enter your weight in kilograms: "))
            if 35 <= weight < 199:
                break
            else:
                print(f"{Fore.RED}Please enter your weight in kg between "
                      "35 and 199.")
        except ValueError:
            print(f"{Fore.RED}Input error, please enter a valid number "
                  f"for weight.")

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine which user are in BMI area
    if bmi <= 18.5:
        print(f"\nYour BMI is {bmi:.2f} - which means you are underweight.")
    elif 18.5 < bmi < 25:
        print(f"\nYour BMI is {bmi:.2f} - which means you are healthy.")
    elif 25 <= bmi < 30:
        print(f"\nYour BMI is {bmi:.2f} - which means you are overweight.")
    else:
        print(f"\nYour BMI is {bmi:.2f} - which means you are obese.")

    print(f"{Back.BLUE}0 -Underweight- 18.5 {Back.GREEN} 18.6 -Healthy- 24 "
          f"{Back.YELLOW} 25 -Overweight- 30 {Back.RED} 30.1 -obese- 302 \n")

    input("To return to the main menu, please press enter\n")
    main_menu()


def heart_ratio():
    """
    Displays section called Heart Ratio
    """
    clear_tml()
    print("----------------------")
    print(f"{Style.BRIGHT}Welcome to Heart Ratio")
    print("----------------------\n")

    # Input age in numbers between 0 - 100
    while True:
        try:
            user_input_heart = int(input("Please enter your age: "))
            min_value = 1
            max_value = 100
            if min_value <= user_input_heart <= max_value:
                heart_result = 206.9 - (0.67 * user_input_heart)
                print(f"\nYour maximum heart rate result is {heart_result} "
                      f"beats per minute.\n")
                break
            else:
                print(f"{Fore.RED}Please enter your age between {min_value} "
                      f"and {max_value}.\n")
        except ValueError:
            print(f"{Fore.RED}Invalid input, please enter a number.\n")

    input("To return to the main menu, please press enter\n")
    main_menu()


def waist_hip():
    """
    Displays section call waist to hip ratio
    """
    clear_tml()
    print("-----------------------------")
    print(f"{Style.BRIGHT}Welcome to waist to hip ratio")
    print("-----------------------------\n")

    # Input waist between 50 to 300
    while True:
        try:
            waist = float(input("Please enter your waist measurement in cm: "))
            if 50 <= waist <= 300:
                break
            else:
                print(f"{Fore.RED}Please enter your waist in meters between 50"
                      f" and 300.")
        except ValueError:
            print(f"{Fore.RED}Input error, please enter a valid number for "
                  f"waist.")

    # Input hip between 50 to 300
    while True:
        try:
            hip = int(input("Please enter your hip measurement in cm: "))
            if 50 <= hip < 300:
                break
            else:
                print(f"{Fore.RED}Please enter your hip in between 50 and "
                      f"300.")
        except ValueError:
            print(f"{Fore.RED}Input error, please enter a valid number "
                  f"for hip.")

    # Input male or female
    while True:
        try:
            gender_choice = input("Please choose your gender ('male' or "
                                  "'female'): ").lower()
            if gender_choice in ["male", "female"]:
                break
            else:
                print(f"{Fore.RED}Invalid input. Please enter 'male' or "
                      f"'female")
        except ValueError:
            print(f"{Fore.RED}Input error")

    # Calculate waist to hip ratio for male and female
    if gender_choice.lower() == 'male':
        male_waist_to_hip = waist / hip
    elif gender_choice.lower() == 'female':
        female_waist_to_hip = waist / hip
    else:
        print(f"{Fore.RED}Invalid choice. Please enter 'male' or 'female'.")
        waist_hip()

    # Determine the selection male in which waist to hip area
    if gender_choice == "male":
        if male_waist_to_hip <= 0.91:
            print(f"\nYour waist-to-hip ratio is {male_waist_to_hip:.2f}, "
                  f"which means you are in {Fore.GREEN}low-risk.")
        elif 0.92 < male_waist_to_hip < 0.98:
            print(f"\nYour waist-to-hip ratio is {male_waist_to_hip:.2f}, "
                  f"which means you are in {Fore.YELLOW}medium-risk")
        else:
            print(f"\nYour waist-to-hip ratio is {male_waist_to_hip:.2f}, "
                  f"which means you are in {Fore.RED}high-risk.")

        print(f"{Back.GREEN}0 - Low - 0.91 {Back.YELLOW} 0.92 - Medium - 0.98 "
              f"{Back.RED} 0.99 - High - 6.00 \n")

    # Determine the selection female in which waist to hip area
    if gender_choice == "female":
        if female_waist_to_hip <= 0.81:
            print(f"\nYour waist-to-hip ratio is {female_waist_to_hip:.2f}, "
                  f"which means you are in {Fore.GREEN}low-risk.")
        elif 0.82 < female_waist_to_hip < 0.89:
            print(f"\nYour waist-to-hip ratio is {female_waist_to_hip:.2f}, "
                  f"which means you are in {Fore.YELLOW}medium-risk.")
        else:
            print(f"\nYour waist-to-hip ratio is {female_waist_to_hip:.2f}, "
                  f"which means you are in {Fore.RED}high-risk.")

        print(f"{Back.GREEN}0 - Low - 0.81 {Back.YELLOW} 0.82 - Medium - 0.89 "
              f"{Back.RED} 0.90 - High - 6.00 \n")

    input("To return to the main menu, please press enter\n")
    main_menu()


def how_it_work():
    """
    Displays section how it works
    """
    # Explaing how each section works
    clear_tml()
    print("--------------")
    print(f"{Style.BRIGHT}How this works")
    print("--------------\n")

    print(f"{Fore.GREEN}-------------------------------------------------"
          f"---------")
    print(f"{Style.BRIGHT}(1) Body Mass Index\n")
    print("Calculate your body mass index")
    print("Not sure about your weight in kilogram or height in Meter,")
    print("you can use the the converter from your preference")
    print("https://www.unitconverters.net/length-converter.html")
    print(f"{Fore.GREEN}--------------------------------------------------"
          f"--------\n")

    print(f"{Fore.GREEN}--------------------------------------------------"
          f"--------")
    print(f"{Style.BRIGHT}(2) Heart\n")
    print("Your target heart rate is the maximum heart rate that")
    print("it should be beating per minutes.")
    print(f"{Fore.GREEN}--------------------------------------------------"
          f"--------\n")

    print(f"{Fore.GREEN}--------------------------------------------------"
          f"--------")
    print(f"{Style.BRIGHT}(3) Waist to Hip Ratio\n")
    print("Compares your waist measurement to your hip measurement,")
    print("not sure about your waist or hip in centremeters")
    print("you can use the the converter from your preference")
    print("https://www.unitconverters.net/length-converter.html")
    print(f"{Fore.GREEN}--------------------------------------------------"
          f"---------\n")

    input("To return to the main menu, please press enter\n")
    main_menu()


def clear_tml():
    """
    Clears the terminal when called.
    """
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
    Runs necessary functions at the start of the program.
    """
    main_menu()


main()
