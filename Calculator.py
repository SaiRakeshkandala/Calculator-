def calculator():
    print("🧮 Simple Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get the user's choice
    operation = input("Enter your choice (1/2/3/4): ")
    
    # Validate the operation
    if operation not in ['1', '2', '3', '4']:
        print("❌ Invalid choice. Please select a valid operation.")
        return
    
    try:
        # Get two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")
        return
    
    # Perform the calculation
    if operation == '1':
        result = num1 + num2
        print(f"The result of addition: {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of subtraction: {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of multiplication: {num1} * {num2} = {result}")
    elif operation == '4':
        if num2 == 0:
            print("❌ Division by zero is not allowed.")
            return
        result = num1 / num2
        print(f"The result of division: {num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()
