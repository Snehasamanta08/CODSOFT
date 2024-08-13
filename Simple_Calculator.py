def calculate(num1, num2, operation):
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': "Error: Division by zero is not allowed." if num2 == 0 else num1 / num2
    }
    return operations.get(operation, "Error: Invalid operation.")

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Choose an operation from [+, -, *, /]: ")

    result = calculate(number1, number2, operation)
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid numbers.")
