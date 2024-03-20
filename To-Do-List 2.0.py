print("Welcome to To-Do-List 2.0 Application")

#FUNCTIONS

def menu():
    print("------------------------")
    print("MENU")
    print("\n")
    print("Please enter the corresponding number of the action you want to take")
    print("\n")
    print("1: Add Task")
    print("2: Show Tasks")
    print("3: Mark Task as Complete")
    print("4: Delete Task")
    print("0. Quit Program")
    print("------------------------")


def menu_selection(command, tasks):
    match command:
        case 0:
            print("Quitting Application")
            return False
            
        case 1:
            item = input("Please enter task to add to your list: ")
            tasks.append((item, "Incomplete")) # Modifying the tasks list
            print("\n")
            print(f"The task {item} has been added to your list")
            return True
        
        case 2:
            for i, (task, status) in enumerate(tasks, start=1):
                print(f"{i}. {task} - {status}")
            return True
        
        case 3:
            print("Mark Task as Complete")
            for i, (task, status) in enumerate(tasks, start=1):
                print(f"{i}. {task} - {status}")
            task_index = int(input("Enter the number of that ask you want to complete: ")) - 1
            if task_index >= 0 and task_index < len(tasks):
                tasks[task_index] = (tasks[task_index][0], "Complete")
                print(f"Task '{tasks[task_index][0]}' has been marked as complete.")
            else:
                print("Invalid task number.")
            return True
        
        case 4:
            print("Delete Task")
            for i, (task, status) in enumerate(tasks, start=1):
                print(f"{i}. {task} - {status}")
            task_index = int(input("Enter the number of that task you want to delete: ")) - 1
            if task_index >= 0 and task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                print(f"Task '{deleted_task[0]}' has been deleted.")
            else:
                print("Invalid task number.")
            return True

        case _:
            print("Incorrect entry. Please choose correct action")
            command
            return True
          

#EMPTY LISTS
tasks = []

while True:

    menu()
    command = int(input("What do you want to do?: "))

    if not menu_selection(command, tasks):
        break





