# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================

students = []  # list of dictionaries, e.g. {"name": ..., "id": ..., "scores": [...]}


def add_student():
    name = input("Student name: ")
    while True:
        try:
            student_id = int(input("Student ID: "))
            break
        except ValueError:
            print("Invalid ID. Please enter a number.")

    while True:
        try:
            num_scores = int(input("How many scores? "))
            if num_scores < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid number. Please enter an integer.")

    scores = []
    for i in range(1, num_scores + 1):
        while True:
            try:
                score = float(input(f"Enter score {i}: "))
                scores.append(score)
                break
            except ValueError:
                print("Invalid score. Please enter a number.")

    student = {"name": name, "id": student_id, "scores": scores}
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_students():
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print("-" * 50)

    for student in students:
        scores = student["scores"]
        avg = round(sum(scores) / len(scores), 2) if scores else 0
        scores_str = ", ".join(str(int(s)) if s.is_integer() else str(s) for s in scores)
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{avg:<10}")

    print("-" * 50)


def calculate_average():
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid ID format.")
        return

    for student in students:
        if student["id"] == student_id:
            scores = student["scores"]
            if not scores:
                print(f"{student['name']} has no scores recorded.")
                return
            avg = round(sum(scores) / len(scores), 2)
            print(f"{student['name']}'s average score: {avg}")
            return

    print(f"Error: No student found with ID {student_id}.")


def print_menu():
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
