# This code is similar to the command line ToDo list, the only difference is that this one uses functions and tries to separate user input from the core logical
# Let's first set the ideas that we want:
# 1. Having a main menu that:
#       A) Create a new ToDo list
#       B) Add a ToDo task
#       C) View Tasks
#       D) Remove or edit a previous list
# 2. Load previous user data
# 3. Handle errors well

# Imports
import json

# Let's start with a function that create's a new ToDo list
# The todo list was set-up as a predefined set that the user could add a new list if necessary:
all_todo_list = {
    "personal": ["nutmeg", "Messi", "Neymar"],
    "school work": ["Cristianoooo"],
    "groceries": []
}
todo_list_keys = all_todo_list.keys()

file_path = "todo_list_S.json"

def save_data():
    """Function that saves user data to a json file"""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(all_todo_list, file, indent=4)
        print("Saved file successfully")

def load_data():
    """This function loads user data"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            user_data = json.load(file)
            for category, values in user_data.items():
                print(f"{category} : {values}")

    except FileNotFoundError:
        print("File was not found")

def create_new_todo_list():
    """Creates a new todo list to the all_todo_list"""
    list_name = input("Enter the name of the list you wish to add: ").strip().lower()
    all_todo_list[list_name] = []
    save_data()

def add_new_task():
    """Adds a new task to one of the lists in the all_to_lists"""
    for keys, values in all_todo_list.items():
        print(keys)

    user_task_list = (input("Which list you wish to add the task in? : ")).strip().lower()
    user_new_task = input("Enter the task you wish to add: ")
    all_todo_list[user_task_list].append(user_new_task)
    print(f"You have successfully added '{user_new_task}' to '{user_task_list}'")
    save_data()

def view_all_tasks():
    """Allows user to view all tasks"""
    for category, task in all_todo_list.items():
        if task:
            print(f"{category} {task}")

def remove_task():
    """Enables user to remove a task in all_todo_Lists"""
    max_tries = 0
    print("The task lists are: ")
    key_counter = 1
    for key in todo_list_keys:
        print(f"{key_counter}. {key}")
        key_counter += 1
    while True:
        user_task_list_removal = (input("Enter the name of the list you want to remove tasks from: ")).strip().lower()
        if user_task_list_removal in todo_list_keys:
            print("Successfully chosen correct list")
            break
        else:
            print("That's not a valid response, try again")
            key_counter = 1
            for key in todo_list_keys:
                print(f"{key_counter}. {key}")
                key_counter += 1

            max_tries += 1
            if max_tries == 20:
                print("Too many invalid responses, terminating program.")
                exit()

    task_counter = 0
    print(user_task_list_removal)
    if len(all_todo_list[user_task_list_removal]) > 0:
        print(f"The tasks in '{user_task_list_removal}' are: ")
        for items in all_todo_list[user_task_list_removal]:
            if items:
                print(f"{task_counter}. {items}")
                task_counter += 1
        while True:
            try:
                user_task_removal = int(input("Enter the number of the task you wish to remove: "))
                if 0 <= user_task_removal < len(all_todo_list[user_task_list_removal]):
                    break
                else:
                    print("That's not a valid response, enter the number before the task.")
                    counter = 0
                    for items in all_todo_list[user_task_list_removal]:
                                if items:
                                    print(f"{counter}. {items}")
                                    counter += 1

            except ValueError:
                print("That is not a number therefore invalid. Try again")
                if max_tries == 20:
                    print("Too many invalid responses, exiting program.")
                    exit()

        removed_task = all_todo_list[user_task_list_removal].pop(user_task_removal)
        print(f"You have successfully removed '{removed_task}' from '{user_task_list_removal}' list")
        save_data()
    else:
        print("There are no tasks in the chosen list")

