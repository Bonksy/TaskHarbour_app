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
    print("5: Edit Task")
    print("6. Quit Program")
    print("------------------------")

def add_task(tasks):
    task_name = input("Please enter task to add to your list: ")
    due_date = input("Please enter due date (DD-MM-YYYY): ")
    reminder_date = input("Please enter reminder date (YYYY-MM-DD): ")
    tasks.append((task_name, "Incomplete", due_date, reminder_date)) # Modifying the tasks list
    print("\n")
    print(f"The task {task_name} has been added to your list with due date {due_date} & reminder date {reminder_date}.")

def display_tasks(tasks):
    print("Show Task")
    for i, (task, status, due_date, reminder_date) in enumerate(tasks, start=1):
        print(f"{i}. {task} - {status} - Due: {due_date} - Reminder: {reminder_date}")

def mark_complete(tasks):
    display_tasks(tasks)
    print("Mark Tasks as Complete")
    task_index = int(input("Enter the number of that ask you want to complete: ")) - 1
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index] = (tasks[task_index][0], "Complete", tasks[task_index][2], tasks[task_index][3])
        print(f"Task '{tasks[task_index][0]}' has been marked as complete.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
     print("Delete Task")
     display_tasks(tasks)
     task_index = int(input("Enter the number of that task you want to delete: ")) - 1
     if task_index >= 0 and task_index < len(tasks):
         deleted_task = tasks.pop(task_index)
         print(f"Task '{deleted_task[0]}' has been deleted.")
     else:
         print("Invalid task number.")

def edit_task(tasks):
    print("Edit Task")
    display_tasks(tasks)
    task_index = int(input("Enter the number of that ask you want to edit: ")) - 1
    if task_index >= 0 and task_index < len(tasks):
        old_task_name = tasks[task_index]
        new_task_name = input("Enter a new task name: ")
        tasks[task_index] = (new_task_name, tasks[task_index][1])
        print(f"Task '{old_task_name}' has been updated to {new_task_name}.")
    else:
        print("Invalid task number.")


def menu_selection(command, tasks):
    match command:
                    
        case 1:
            add_task(tasks)
            return True
        
        case 2:
            display_tasks(tasks)
            return True
        
        case 3:
            mark_complete(tasks)
            return True
        
        case 4:
           delete_task(tasks)
           return True
        
        case 5:
            edit_task(tasks)
            return True
        
        case 6:
            print("Quitting Application")
            return False


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





