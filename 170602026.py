
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Perform addition
addition_result = first_number + second_number

# Perform subtraction
subtraction_result = first_number - second_number

# Perform multiplication
multiplication_result = first_number * second_number
# Perform division with error handling for division by zero
if second_number != 0:
    division_result = first_number / second_number
else:
    division_result = "Error: Division by zero is not allowed."

print("\n--- Results ---")
print(f"Addition: {first_number} + {second_number} = {addition_result}")
print(f"Subtraction: {first_number} - {second_number} = {subtraction_result}")
print(f"Multiplication: {first_number} * {second_number} = {multiplication_result}")
print(f"Division: {first_number} / {second_number} = {division_result}")
