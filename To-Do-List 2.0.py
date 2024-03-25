from datetime import datetime, timedelta
import schedule
import time
from plyer import notification

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

# Function to send reminders for tasks
def send_reminders(tasks):
    current_time = datetime.now()

    # Iterate through tasks and check for reminders
    for task in tasks:
        task_name, status, due_date, reminder_date = task
        if status == "Incomplete" and current_time.date() == reminder_date.date() and current_time.hour == 12:
            # Send reminder notification
            notification_title = f"Reminder: Task '{task_name}' is due today"
            notification_message = f"Don't forget to complete '{task_name}' today!"
            notification.notify(
                title=notification_title,
                message=notification_message,
                app_name="TaskHarbor"
            )

def add_task(tasks, categories):
    task_name = input("Please enter task to add to your list: ")

    print("Available Categories")
    for category in categories:
        print(category)

    while True:
        category = input("Please enter the category for the task, or type 'new' to create a new category: ")
        if category.lower() == 'new':
            category = input("Please enter the name for the new category: ")
            if not category.strip():  # Check if category is empty or whitespace
                print("Category name cannot be empty. Please enter a valid category name.")
            elif not category.isalnum():  # Check if category contains only alphanumeric characters
                print("Invalid category name. Category name should contain only letters and numbers.")
            elif len(category) > 50:  # Check if category name exceeds maximum length
                print("Category name is too long. Please enter a shorter name.")
            elif category in categories:
                print("Category already exists. Please choose a different name or select from the existing categories. ")
            else:
                categories.append(category)
                break
        elif category in categories:
            break
        else:
            print("Invalid category. Please choose form the existing categories or create a new one.")

    while True:
        due_date_input = input("Please enter due date (DD/MM/YYYY): ")
        try:
            due_date = datetime.strptime(due_date_input, "%d/%m/%Y")
            if due_date < datetime.now():
                print("Due date cannot be in the past. Please enter a valid due date.")
            else:
                break
        except ValueError:
            print("Invalid due date format. Please enter the date in DD/MM/YYYY format.")
            due_date_input = input("Please enter due date (DD/MM/YYYY): ")

          
    while True:
        reminder_date_input = input("Please enter reminder date (DD/MM/YYYY): ")

        try:
            reminder_date = datetime.strptime(reminder_date_input, "%d/%m/%Y")
            if reminder_date <= due_date:
                    tasks.append((task_name, "Incomplete", due_date, reminder_date, category)) # Modifying the tasks list
                    print("\n")
                    print(f"The task {task_name} has been added to your list with due date {due_date.strftime('%d/%m/%Y')} & reminder date {reminder_date.strftime('%d/%m/%Y')}.")
                    break
            else:
                print("Reminder date cannot be after due date. Please enter a valid reminder date")            
        except ValueError:
            print("Invalid reminder date format. Please enter the date in DD/MM/YYYY format.")
            reminder_date_input = input("Please enter reminder date (DD/MM/YYYY): ")
            
def display_tasks(tasks):
    print("Show Tasks")
    for i, (task, status, due_date, reminder_date, category) in enumerate(tasks, start=1):
        print(f"{i}. {task} - {status} - Due: {due_date} - Reminder: {reminder_date} - Category: {category}")

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
categories = {"Personal": [],
              "Work": [],
              "Home": []
              }
while True:

    menu()
    command = int(input("What do you want to do?: "))

    if not menu_selection(command, tasks):
        break





