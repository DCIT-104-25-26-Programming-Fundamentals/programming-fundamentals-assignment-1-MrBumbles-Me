def calculate_sum(numbers):
    """Return the sum of a list of numbers, without using sum()."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Return the average of a list of numbers."""
    return calculate_sum(numbers) / len(numbers)


def calculate_max(numbers):
    """Return the largest value in a list, without using max()."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def calculate_min(numbers):
    """Return the smallest value in a list, without using min()."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


if __name__ == "__main__":
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        numbers = []
        for i in range(n):
            value = int(input(f"Enter number {i + 1}: "))
            numbers.append(value)

        print("\nResults:")
        print(f"Sum:     {calculate_sum(numbers)}")
        print(f"Average: {calculate_average(numbers)}")
        print(f"Maximum: {calculate_max(numbers)}")
        print(f"Minimum: {calculate_min(numbers)}")
