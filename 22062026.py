#-------------
#1.Function to Compare Two Integers
#--------------
def compare_numbers(num1, num2):
    """Compares two integers and prints which one is larger."""
    if num1 > num2:
        print(f"{num1} is larger than {num2}")
    elif num2 > num1:
        print(f"{num2} is larger than {num1}")
    else:
        print("Both numbers are equal")

#-------
#2.Logical Operators Program
#---------
# Check if a number is within a specified range
number = 15
if number >= 10 and number <= 20:
    print(f"{number} is within the range 10–20")
else:
    print(f"{number} is outside the range 10–20")

# Check if a string is not empty and length > 5
text = "HelloWorld"
if text != "" and len(text) > 5:
    print("The string is not empty and has more than 5 characters")
else:
    print("Condition not met")

#------------
#3.Simple Calculator Using Conditional Statements
#--------------------

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
#--------------
#4.Age Classification Script
#-------------
age = int(input("Enter age: "))

if age < 13:
    print("Category: Child")
elif age >= 13 and age < 20:
    print("Category: Teenager")
elif age >= 20 and age < 60:
    print("Category: Adult")
else:
    print("Category: Senior")

#----------------
#5.Simple Login System
#--------------

valid_username = "admin"
valid_password = "password123"


username = input("Enter username: ")
password = input("Enter password: ")

if username == valid_username and password == valid_password:
    print("Login successful!")
else:
    print("Invalid credentials. Access denied.")



