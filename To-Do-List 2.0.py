print("Welcome to To-Do-List 2.0 Application")

#FUNCTIONS

def menu():
    print("------------------------")
    print("MENU")
    print("Please enter the corresponding number of the action you want to take")
    print("\n")
    print("1: Add task")
    print("0. Quit program")
    print("------------------------")


def menu_selection(command, tasks):
    match command:
        case 0:
            print("Quitting Application")
            return False
            
        case 1:
            item = input("Please enter task to add to your list: ")
            tasks.append((item, "Incomplete"))
            print(f"The task {item} has been added to your list")
            print(tasks)
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





