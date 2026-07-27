def single_table():
    try:
        number = int(input("Enter a number: "))

        if number <= 0:
            print("Error: Please enter a positive integer.")
            return

        print(f"\nMultiplication Table for {number}:")
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")

    except ValueError:
        print("Error: Please enter a valid positive integer.")


def tables_to_n():
    try:
        n = int(input("Enter a positive integer (N): "))

        if n <= 0:
            print("Error: Please enter a positive integer.")
            return

        for num in range(1, n + 1):
            print(f"\nMultiplication Table for {num}:")
            for i in range(1, 13):
                print(f"{num} x {i} = {num * i}")
            print("---------------------------")

    except ValueError:
        print("Error: Please enter a valid positive integer.")


print("PART A - Single Multiplication Table")
single_table()

print("\nPART B - Multiplication Tables from 1 to N")
tables_to_n()
