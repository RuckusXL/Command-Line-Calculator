number1 = input("Enter the first number:")
n1 = float(number1)
sign = input("Enter the sign:")
number2 = input("Enter the second number:")
n2 = float(number2)

if sign == "+":
    print("\nThe sum is: " + str(n1 + n2))
elif sign == "-":
    print("\nThe difference is: " + str(n1 - n2))
elif sign == "*":
    print("\nThe product is: " + str(n1 * n2))
elif sign == "/":
    print("\nThe quotient is: " + str(n1 / n2))
else:
    print("\nPlease use +, -, *, or / for your mathmatical operation.\n")
