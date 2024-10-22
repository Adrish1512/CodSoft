# Simple Python Calculator Logic
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is undefined"
    else:
        return "Invalid operation"

# Example of using the function directly
if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Enter your choice (1/2/3/4): ")
        result = calculate(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input, please enter numeric values.")
