#This script will have basic mathmetical functions that I can use in other scripts
#This script is meant for trying out new functions as I learn them. 
#Since I created a bunch of math functions why not make a calculator? I've been itching to interact with user input.
#Day 6
#Author: RuckusXL

from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

#This function adds the numerical inputs of the user.
def add():
    while True:
        try:
            print(Fore.YELLOW + "\nAdding Numbers".upper())
            a = float(input("\n"))
            b = float(input(""))
            break
        except ValueError:
            print(Fore.RED +"\nFat Fingers? Numbers only.")
    return (Fore.BLUE + "\nThe sum is: " + str(a + b))

#This function subtracts the numerical inputs of the user.
def subtract():
    while True:
        try:
            print(Fore.YELLOW + "\nSubtracting Numbers".upper())
            a = float(input("\n"))
            b = float(input(""))
            break
        except ValueError:
            print(Fore.RED + "\nFat Fingers? Numbers only.")
    return (Fore.BLUE + "\nThe difference is: " + str(a - b))
    
#This function multiplies the numerical inputs of the user.
def multiply():
    while True:
        try:
            print(Fore.YELLOW + "\nMultiplying Numbers".upper())
            a = float(input("\n"))
            b = float(input(""))
            break
        except ValueError:
            print(Fore.RED +"\nFat Fingers? Numbers only.")
    return (Fore.BLUE + "\nThe product is: " + str(a * b))

#This function divides the numerical inputs of the user.
def divide():
    while True:
        try:
            print(Fore.YELLOW + "\nDividing Numbers".upper())
            a = float(input("\n"))
            b = float(input(""))
            break
        except ValueError:
            print(Fore.RED + "\nFat Fingers? Numbers only.")
            a = float(input("\n"))
            b = float(input(""))
            break
    if b == 0:
        return "Dividing Zero? Really?"
    return (Fore.BLUE + "\nThe quotient is: " + str(a / b))

#This function calculates the area of a triangle
def calc_area_triangle():
    while True:
        try:
            print(Fore.YELLOW + "\nCalculating Area of Triangle".upper())
            base = float(input("\nBase: "))
            height = float(input("Height: "))
            break
        except ValueError:
            print(Fore.RED + "\nFat Fingers? Numbers only.")
    return (Fore.BLUE + "\nThe area of the triangle is: " + str(0.5 * base * height))

#This function will square the numerical input of the user
def squared():
    while True:
        try:
            print(Fore.YELLOW + "\nSquaring Numbers".upper())
            a = float(input("\nWhat number do you want to square? "))
            break
        except ValueError:
            print(Fore.RED + "\nFat Fingers? Numbers Only.")
    return (Fore.BLUE + f"\n{a} squared is: " + str(a * a))

#This function will square the numerical input of the user
def cubed():
    while True:
        try:
            print(Fore.YELLOW + "\nCubing Numbers".upper())
            a = float(input("\nWhat number do you want to cube: "))
            break
        except ValueError:
            print(Fore.RED + "\nFat Fingers? Numbers Only.")
    return (Fore.BLUE + f"\n{a} cubed is: " + str(a * a * a))

#This function will calculate the area of a circle
def simple_interest_calc():
    while True:
        try:
            print(Fore.YELLOW + "\nCalculating Simple Interest".upper())
            a = float(input("Principal: "))
            b = float(input("Interest Rate: "))
            c = float(input("Years: "))
            d = b / 100
            break
        except ValueError:
            print(Fore.RED + "\nFat Fingers? Numbers Only.")
    return (Fore.BLUE + f"\nTotal Interest: {a * d * c + a}")

#This function will calculate annual income
def annual_income():
    while True:
        try:
            print(Fore.YELLOW + "Calculating Annual Income".upper())
            a = float(input("\nInput Hourly Rate: "))
            b = float(input("Hours Worked a week: "))
            c = float(input("Weeks worked in a year: "))
            break
        except ValueError:
            print(Fore.RED + "\nFat Fingers? Numbers Only")
            continue
    return (Fore.BLUE + f"\n{a} an hour is {a * b * c} yearly")

#This function prints a home screen message to the user.
def welcome():
     print(Fore.BLUE + "\n-----------------------------")
     print(Fore.BLUE + "\n 📏Command Line Calculator📐".upper())
     print(Fore.BLUE + "\n-----------------------------")
     print("Date & Time:", datetime.now().strftime("%m-%d-%Y %H:%M:%S"))

#This function prints the selections for math operations, then outputs the results.
def calc():
     while True:
        print("\n1. Add Numbers ➕")
        print("2. Subtract Numbers ➖")
        print("3. Multiply Numbers ✖️")
        print("4. Divide Numbers ➗")
        print("5. Area of Triangle 🔼")
        print("6. Simple Interest 🪙")
        print("7. Squared ⬜")
        print("8. Cubed 🧊")
        print("9. Annual Income 💸")
        print("0. Exit 💭")
        
        try:
            choice = int(input("\nSelect a number 1 - 9: "))
        except ValueError:
            print(Fore.RED + "\nFat Fingers? 1 - 9.")
            continue

        if choice == 1:
            print(add())
        elif choice == 2:
            print(subtract())
        elif choice == 3:
            print(multiply())
        elif choice == 4:
            print(divide())
        elif choice == 5:
            print(calc_area_triangle)
        elif choice == 6:
            print(simple_interest_calc())
        elif choice == 7:
            print(squared())
        elif choice == 8:
            print(cubed())
        elif choice == 9:
            print(annual_income())
        elif choice == 0:
            print("\nThank you for using me!👋\n")
            break
        else:
            print(Fore.RED + "\nFat Fingers? 1 - 9.")

def run_progam():
    welcome()
    calc()

if __name__ == "__main__":
    run_progam()