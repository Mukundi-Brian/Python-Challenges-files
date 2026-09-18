# Dictionary for the todo list
all_todo_lists = {
    "personal":["Go to school", "Run a marathon"],
    "shopping":["Buy Eggs"],
    "groceries":[],
    "school work": ["Finish the Assignment"]
}

# all_tasks = [] # Let's add an all tasks here to facilitate easy removing of a task
# Let's use a map instead
menu_map = {}
counter = 1

# let's add all tasks to one dictionary in order to remove them much easily
print("Available tasks to delete")
for category, task_list in all_todo_lists.items():
    for item_index, item in enumerate (task_list):
        print(f"{counter}. {item} in '{category}'")
        menu_map[counter] = (category, item_index)
        counter += 1

try:
    user_remove_task = int(input("Enter the number of the task you wish to remove: "))

    if user_remove_task in menu_map:
        #  Look for the category and item in the menu map
        target_category, target_item_index = menu_map[user_remove_task]
        # Delete it from the menu map
        removed_item = all_todo_lists[target_category].pop(target_item_index)
        print(f"Successfully deleted '{removed_item}' from tasks")
    else:
        print("Invalid choice")

except (ValueError, IndexError):
    print("Please enter a valid response")

task_counter = 1
print("Tasks remaining")
for keys, values in all_todo_lists.items():
    if values:
        for task in values:
            print(f"{task_counter}. {task}")
            task_counter += 1