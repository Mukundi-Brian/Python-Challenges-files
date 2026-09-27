# Hello, this code is supposed to create a terminal ToDo list program that
# should let the user choose a number of options such as: 
# 1. Having a main menu that:
#       A) Create a new ToDo list
#       B) Add a ToDo task
#       C) View Tasks
#       D) Remove or edit a previous list
# 2. Load previous user data
# 3. Handle errors well

# Let's start from easy and work our way up:
# 1. Create main menu using a while loop
# 2. Create the options that do stuff
# 3. Create a new todo list with predefined categories first then user_defined later
import json # This is for saving user data

mistake_counter = 0 # Adding a mistake counter to prevent spamming
# i = 1 # let's add a counter for the users's tasks - Turns out you can use enumerate
all_todo_lists = {
    "personal":[],
    "shopping":[],
    "groceries":[],
    "school work": []
}
# Using json to read saved user data
try:
    with open("todo_data.json", "r", encoding="utf-8") as file:
        all_todo_lists = json.load(file)
except FileNotFoundError:
    # If no save file exists, fall back to default dictionary
    all_todo_lists = {
    "personal":[],
    "shopping":[],
    "groceries":[],
    "school work": []
}
# While loop - for user to access main menu and options
while True:
    user_choice = input("""Hello, What would you like to do?
    A: Create a new ToDo List
    B: Add a Task
    C: View Tasks
    D: Remove a Task
    Q: Quit Program
    : """).strip().lower()

    # Let's make sure the user can quit the program
    if user_choice == "q":
        print("Exiting Program, have a good day!")
        with open("todo_data.json", "w", encoding="utf-8") as file:
            json.dump(all_todo_lists, file, indent=4)
        exit()

    #This should allow the user to create a new ToDo list
    elif user_choice == "a":
        print("You have chosen Create a new ToDo List\n")
        user_new_list_name = input("Enter the name of the new list: ").strip().lower()
        all_todo_lists[user_new_list_name] = []
        print(all_todo_lists)
        print(f"You have created a new '{user_new_list_name}' list, Proceed to add a task\n")

    elif user_choice == "b":
        print(f"({', '.join(all_todo_lists)})\n")
        user_target_List = input("You have chosen to add a new task, which list do you want to use?: ").strip().lower()

        if user_target_List in all_todo_lists:
            user_new_task = input("Enter new task: ")
            all_todo_lists[user_target_List].append(user_new_task)
            print(f"Successfully added '{user_new_task}' to '{user_target_List}'\n")
        else:
            print("List not found, try again\n")

    # This shows the user the tasks
    elif user_choice == "c":
        print("You have chosen to view tasks\n")
        if any(all_todo_lists.values()):
            for keys, values in all_todo_lists.items():
                if values:
                    print(f"{keys}: {values}")
        else:
            print("Nothing has been added yet.\n")

    # This block enables the user to remove a previously entered task
    elif user_choice == "d":
        # let's add all tasks to a menu map dictionary in order to remove them much easily
        print("You have chosen to remove a task\n")
        # Let's use a map instead to trace the path of the tasks and enable easy deletion of tasks
        menu_map = {}
        counter = 1 # Counter to display the lists for user
        if any (all_todo_lists.values()):
            for category, task in all_todo_lists.items():
                if task:
                    for item_index, item in enumerate (task):
                        print(f"{counter}. {item} in '{category}'")
                        menu_map[counter] = (category, item_index)
                        counter += 1

            # Now let's have the user choose the task they wish to remove
            # Let's wrap the user input in a try block to cater for value error
            try:
                user_remove_task = int(input("Enter the No of the task you wish to remove: "))
                if user_remove_task in menu_map:
                    target_category, target_task = menu_map[user_remove_task]
                    removed_task = all_todo_lists[target_category].pop(target_task)
                    print(f"You a have successfully removed '{removed_task}' from your tasks")
                else:
                    print("Invalid input, no such task exists")
            except (ValueError, IndexError):
                print("Invalid input, that is not a valid response\n")
        else:
            print("No task has been added yet\n")

    # Catches invalid inputs and prevents spamming wrong values
    else:
        print("Invalid input, try again\n")
        mistake_counter += 1
        if mistake_counter == 5:
            print("Too many invalid attempts, exiting program!")
            exit()