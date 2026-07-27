def print_fibonacci(n):
    if n <= 0:
        print("N must be a positive integer.")
        return

    first = 0
    second = 1

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(first, end=" ")
        next_num = first + second
        first = second
        second = next_num

    print()


def check_fibonacci(number):
    if number < 0:
        print(f"{number} is NOT a Fibonacci number.")
        return

    first = 0
    second = 1

    while first < number:
        next_num = first + second
        first = second
        second = next_num

    if first == number:
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


n = int(input("How many terms? "))
print_fibonacci(n)

number = int(input("Enter a number to check: "))
check_fibonacci(number)
