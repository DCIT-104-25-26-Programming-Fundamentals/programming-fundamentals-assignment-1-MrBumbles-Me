tasks = []


def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("Your Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")


def delete_task():
    if len(tasks) == 0:
        print("Your to-do list is empty.")
        return

    view_tasks()

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f'Task "{removed}" has been removed.')
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
