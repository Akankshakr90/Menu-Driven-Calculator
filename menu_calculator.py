def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b
def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a % b
while True:
    print("\n===== MENU CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")
    try:
        choice = int(input("Enter your choice (1-7): "))

        if choice == 7:
            print("Thank you for using the calculator. Exiting...")
            break

        if choice < 1 or choice > 7:
            print("Invalid choice. Select 1 to 7.")
            continue
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            result = add(a, b)
        elif choice == 2:
            result = subtract(a, b)
        elif choice == 3:
            result = multiply(a, b)
        elif choice == 4:
            result = divide(a, b)
        elif choice == 5:
            result = power(a, b)
        elif choice == 6:
            result = modulus(a, b)

        print(f"Result: {result:.2f}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Invalid number. Enter numeric values only.")
      