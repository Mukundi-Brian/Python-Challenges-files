# Modules, scope resolution, if __name__ == '__main__',

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
