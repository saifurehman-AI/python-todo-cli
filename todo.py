import json

tasks = []


def save_tasks():

    with open("CLI.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():
    with open("CLI.json", "r", encoding="utf-8") as file:
        return json.load(file)


try:
    tasks = load_tasks()
except FileNotFoundError:
    tasks = []
    print("No previous tasks found. Starting fresh.")

while True:
    print("1: Add Task")
    print("2: View Task")
    print("3: Complete Task")
    print("4: Delete Task")
    print("5: Exit")

    choice = input("Enter Your Choice:")

    if choice == "1":
        task = input("Enter your Task:").strip()
        if not task:
            print("Task is Empty")
        else:
            tasks.append(task)
            save_tasks()
            print("Task Added Successfully")
    elif choice == "2":
        for number, task in enumerate(tasks, start=1):
            print(f"{number}.{task}")
    elif choice == "3":
        try:
            task_no = int(input("Enter Your Task Number:"))
            indext = task_no - 1
            if 0 <= indext < len(tasks):
                if tasks[indext].startswith("[Completed]"):
                    print("Task Already Completed")
                else:
                    tasks[indext] = "[Completed]" + tasks[indext]
                    save_tasks()
                    print(tasks[indext])
            else:
                print("Invalid Task Number")

        except ValueError:
            print("Please Enter a Valid Number")
            continue

    elif choice == "4":
        try:
            task_no = int(input("Enter Your Task Number:"))
            index = task_no - 1

            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks()
            else:
                print("Invalid Task Number")
        except ValueError:
            print("Please Enter Valid Number")
            continue
    elif choice == "5":
        print("Exiting....")
        break
    else:
        print("Invalid Choice")
