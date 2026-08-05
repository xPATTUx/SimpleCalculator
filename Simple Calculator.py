def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def calculator():
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("\nThank you for using the calculator!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numeric values.")
            continue

        if choice == "1":
            print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")

        elif choice == "2":
            print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")

        elif choice == "3":
            print(f"\nResult: {num1} × {num2} = {multiply(num1, num2)}")

        elif choice == "4":
            print(f"\nResult: {num1} ÷ {num2} = {divide(num1, num2)}")


if __name__ == "__main__":
    calculator()