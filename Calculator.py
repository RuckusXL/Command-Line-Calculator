#This script will have basic mathmetical functions that I can use in other scripts
#This script is meant for trying out new functions as I learn them. 
#Since I created a bunch of math functions why not make a calculator? I've been itching to interact with user input.
#Day 6
#Author: RuckusXL

#This function adds the numerical inputs of the user.
def add(a, b):
    while True:
        try:
            print("\nAdding Numbers".upper())
            a = float(input("\n"))
            b = float(input(""))
            break
        except ValueError:
            print("\nFat Fingers? Numbers only.")
    return ("\nThe sum is: " + str(a + b))

#This function subtracts the numerical inputs of the user.
def subtract(a, b):
    while True:
        try:
            print("\nSubtracting Numbers".upper())
            a = float(input("\n"))
            b = float(input(""))
            break
        except ValueError:
            print("\nFat Fingers? Numbers only.")
    return ("\nThe difference is: " + str(a - b))
    
#This function multiplies the numerical inputs of the user.
def multiply(a, b):
    while True:
        try:
            print("\nMultiplying Numbers".upper())
            a = float(input("\n"))
            b = float(input(""))
            break
        except ValueError:
            print("\nFat Fingers? Numbers only.")
    return ("\nThe product is: " + str(a * b))

#This function divides the numerical inputs of the user.
def divide(a, b):
    while True:
        try:
            print("\nDividing Numbers".upper())
            a = float(input("\n"))
            b = float(input(""))
            break
        except ValueError:
            print("\nFat Fingers? Numbers only.")
            a = float(input("\n"))
            b = float(input(""))
            break
    if b == 0:
        return "Dividing Zero? Really?"
    return ("\nThe quotient is: " + str(a / b))

#This function calculates the area of a triangle
def calc_area_triangle(base, height):
    while True:
        try:
            print("\nCalculating Area of Triangle".upper())
            base = float(input("\n"))
            height = float(input(""))
            break
        except ValueError:
            print("\nFat Fingers? Numbers only.")
    return ("\nThe area of the triangle is: " + str(0.5 * base * height))

#This function prints a home screen message to the user.
def welcome():
     print("\n------------------------")
     print("\n Command Line Calculator".upper())
     print("\n------------------------")

def calc():
	while True:
		print("\n1. Add Numbers")
		print("2. Subtract Numbers")
		print("3. Multiply Numbers")
		print("4. Divide Numbers")
		print("5. Calculate Area of Triangle")
		print("6. Exit")

		try:
			choice = int(input("\nSelect a number 1 - 6: "))
		except ValueError:
			print("\nFat Fingers? 1 - 6.")
			continue

		if choice == 1:
			print(add(1,3))
		elif choice == 2:
			print(subtract(5,1))
		elif choice == 3:
			print(multiply(6,9))
		elif choice == 4:
			print(divide(10,2))
		elif choice == 5:
			print(calc_area_triangle(10,5))
		elif choice == 6:
			print("\nThank you for using me!")
			break
		else:
			print("\nFat Fingers? 1 - 6.")

welcome()
calc()