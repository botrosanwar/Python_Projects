def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return a
    return a / b

def calculator():
    print("=== Simple Calculator ===")
    result = None

    while True:
        if result is None:
            a = float(input("Enter first number: "))
        else:
            print(f"\nCurrent result: {result}")
            choice = input("Do you want to continue with this result? (y/n): ").lower()
            if choice == 'y':
                a = result
            else:
                a = float(input("Enter first number: "))

        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = subtract(a, b)
        elif operator == '*':
            result = multiply(a, b)
        elif operator == '/':
            result = divide(a, b)
        else:
            print("Invalid operator!")
            continue

        print(f"Result: {result}")

        cont = input("\nDo you want another calculation? (y/n): ").lower()
        if cont != 'y':
            print("Goodbye!")
            break

# Run the calculator
calculator()
