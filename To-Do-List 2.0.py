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
    print("3: Mark Tasks as Complete")
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





