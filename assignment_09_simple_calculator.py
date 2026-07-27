def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None  # signal error to caller
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        return None  # signal error to caller
    return a % b


def exponentiate(a, b):
    return a ** b


def get_numbers():
    while True:
        try:
            first = float(input("Enter first number : "))
            second = float(input("Enter second number: "))
            return first, second
        except ValueError:
            print("Invalid input. Please enter numeric values.")


def print_menu():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def format_number(n):
    # print whole numbers without a trailing .0, keep decimals otherwise
    return int(n) if float(n).is_integer() else n


def main():
    while True:
        print_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid choice. Please enter a number between 1 and 7.")
            continue

        a, b = get_numbers()

        if choice == "1":
            result = add(a, b)
            symbol = "+"
        elif choice == "2":
            result = subtract(a, b)
            symbol = "-"
        elif choice == "3":
            result = multiply(a, b)
            symbol = "*"
        elif choice == "4":
            result = divide(a, b)
            symbol = "/"
            if result is None:
                print("Error: Cannot divide by zero.")
                continue
        elif choice == "5":
            result = modulus(a, b)
            symbol = "%"
            if result is None:
                print("Error: Cannot divide by zero.")
                continue
        elif choice == "6":
            result = exponentiate(a, b)
            symbol = "**"

        print(f"Result: {format_number(a)} {symbol} {format_number(b)} = {format_number(result)}")


if __name__ == "__main__":
    main()
