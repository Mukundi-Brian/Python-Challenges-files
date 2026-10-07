# This code is similar to the command line ToDo list, the only difference is that this one uses functions rather than having all things in one code, procedural programming I think its called.
# Let's first set the ideas that we want:
# 1. Having a main menu that:
#       A) Create a new ToDo list
#       B) Add a ToDo task
#       C) View Tasks
#       D) Remove or edit a previous list
# 2. Load previous user data
# 3. Handle errors well


# Let's try and set-up the functions
# Let's start with a function that create's a new ToDo list
# The todo list was set-up as a predefined set that the user could add a new list if necessary:
all_todo_list = {
    "personal": ["nutmeg", "Messi", "Neymar"],
    "school work": ["Cristianoooo"],
    "groceries": []
}
# counter = 1
# for keys, values in my_dict.items():
#     if values:
#         for (item_index, values) in enumerate (values):
#             print(f"{counter}.{values}")
#             counter += 1
def create_new_todo_list():
    """Creates a new todo list to the all_todo_list"""
    list_name = input("Enter the name of the list you wish to add: ").strip().lower()
    all_todo_list[list_name] = []

def add_new_task():
    """Adds a new task to one of the lists in the all_to_lists"""
    for keys, values in all_todo_list.items():
        print(keys)

    user_task_list = (input("Which list you wish to add the task in? : ")).strip().lower()
    user_new_task = input("Enter the task you wish to add: ")
    all_todo_list[user_task_list].append(user_new_task)
    print(f"You have successfully added '{user_new_task}' to '{user_task_list}'")

def view_all_tasks():
    """Allows user to view all tasks"""
    for category, task in all_todo_list.items():
        if task:
            print(f"{category} {task}")

def remove_task():
    """Enables user to remove a task in all_todo_Lists"""
    max_tries = 0
    print("The task lists are: ")
    for keys, values in all_todo_list.items():
        print(keys)
    while True:
        user_task_list_removal = (input("Enter the name of the list you want to remove tasks from: ")).strip().lower()
        if user_task_list_removal in all_todo_list.keys():
            print("Successfully chosen correct list")
            break
        else:
            print("That's not a valid response, try again")
            for keys, values in all_todo_list.items():
                    print(keys)
            max_tries += 1
            if max_tries == 20:
                print("Too many invalid responses, terminating program.")
                exit()

    counter = 0
    print(user_task_list_removal)
    if len(all_todo_list[user_task_list_removal]) > 0:
        print(f"The tasks in '{user_task_list_removal}' are: ")
        for items in all_todo_list[user_task_list_removal]:
            if items:
                print(f"{counter}. {items}")
                counter += 1
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
    else:
        print("There are no tasks in the chosen list")

def read_files():
    with 
# create_new_todo_list()
# print(all_todo_list)

# my_dict = {"Meow", "Chipo", "Nande", "Tomodachi", 1234}
# my_list = ["Meow", "Chipo", "Nande", "Tomodachi", 1234]
# my_dict_S = {"Personal": ["Meow", 1234],
#              "Foods": ["Chipo"],
#              "Japonais": ["Nande"],
#              "Topics": []
#             }

# my_dict_S["Topics"].pop(-1)
# print(my_dict_S)

# counter = 1
# for category, task in my_dict_S.items():
#     if task:
#         for items in task:
#             print(f"{counter}. {items}")
#             counter += 1
# print(len(all_todo_list["personal"]))
# remove_task()
# print(all_todo_list)

# add_new_task()
# print(all_todo_list)
# remove_task()
# print(all_todo_list)
# print(my_dict)
# Let's set up the user inputs
# while True:
#     user_main_menu_choice = (input("""What would you like to do?
#     A: Create a new ToDo list
#     B: Add a new task
#     C: View tasks
#     D: Remove a task
#     Q: Quit
#     : """)).strip().lower()

#     if user_main_menu_choice == "a":
#         create_new_todo_list()

#     if user_main_menu_choice == "b":
#         add_new_task()

#     if user_main_menu_choice == "c":


#     if user_main_menu_choice == "d":


#     if user_main_menu_choice == "q":
#         print("Exiting Program, have a great day.")
#         exit()