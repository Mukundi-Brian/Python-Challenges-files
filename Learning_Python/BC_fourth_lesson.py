# Modules, scope resolution, if __name__ == '__main__', multithreading, reading API data

# Module = a file containing code you want to include in your program
#        - use 'import' to include a module (built-in ot your own)
#        - useful to break up a large program into reusable separate files

# To see all the modules
# print(help("modules"))
# To see the variables and function of a module
# print(help("math"))
# To import a module whether self-made or external
# import module_name

# Scope Resolution
# Variable scope = where a variable is visible and accessible
# Scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Functions cant see inside other functions, thats why we sometimes pass arguments to functions for other functions to be available

# def func1():
#     a = 1
#     print(a)

# def func2():
#     b = 2
#     print(b)

# a and b are local variables

# func1()
# func2()

# def func1():
#     x = 1
#     def func2()
#         print(x)
#     func2()

# x in this case is enclosed

# Global variables are outside functions and accessible by functions

# from math import e
# print(e)

# e in this case is a built-in variable

# if __name__ == __main__ : (This script can be imported OR run standalone)
#                           Functions and classes in this module can be reused
#                           without the main block of code executing

# def main():
#     # Your program goes here


# if __name__ == '__main__' :
#     main()



# Multithreading ----- ***************** -----------

# Multithreading = used to perform multiple tasks concurrently (multitasking),
#                  Good for I/O bound tasks like reading files or fetching data from API's
#                  threading, Thread(target=my_function)

# import threading
# import time

# def walk_dog(first, last):
#     time.sleep(8)
#     print(f"You finish walking {first} {last}")

# def take_out_trash():
#     time.sleep(2)
#     print("You take out the trash")

# def get_mail():
#     time.sleep(4)
#     print("You get the mail")

# # walk_dog()
# # take_out_trash()
# # get_mail()

# # We are doing the tasks simultaneously
# chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
# chore1.start()

# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()

# # If you do this it prints first when no tasks are done, so how to make it wait?
# # print("All chores are complete")

# chore1.join()
# chore2.join()
# chore3.join()

# print("All chores are complete!")



# Fetching data from APIs ----- ***************** -----------
# # How to connect to an API, we are going to connect to PokeAPI
# import requests

# base_url = "https://pokeapi.co/api/v2/"

# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url) # Will return a response code

#     if response.status_code == 200:
#         pokemon_data = response.json()
#         return pokemon_data
#     else:
#         print(f"Failed to retrieve data {response.status_code}")

# pokemon_name = "Typhlosion"
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"ID: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"]}")
#     print(f"Weight: {pokemon_info["weight"]}")
