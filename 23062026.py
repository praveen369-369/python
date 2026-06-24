#1.Voting Eligibility Program

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

#2.Grade to Letter Conversion Function
def get_letter_grade(percentage):
    """Returns the letter grade based on percentage."""
    if 90 <= percentage <= 100:
        return "A"
    elif 80 <= percentage < 90:
        return "B"
    elif 70 <= percentage < 80:
        return "C"
    elif 60 <= percentage < 70:
        return "D"
    else:
        return "F"

#3.Simple Calculator Program

operation = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "+":
    print(f"Result: {num1 + num2}")
elif operation == "-":
    print(f"Result: {num1 - num2}")
elif operation == "*":
    print(f"Result: {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation")


#4.Random Number Odd/Even Guess
import random
number = random.randint(1, 100)
print(f"Generated number: {number}")

# Check if odd or even
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

