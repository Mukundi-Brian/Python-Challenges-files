# Numpy = Numerical Python
#       - A python library used for numerical computing
#       - Used in fields that need heavy data processing
#       - Under-hood its written with C
#       - Arrays are OP
#       - Vectorized Operations

import numpy as np

# print(np.__version__)

# my_list = [1, 2, 3, 4]

# my_list *= 2

# print(my_list)

# my_array = np.array([1, 2, 3, 4])

# my_array *= 2
# print(my_array)
# print(type(my_array))

# Exercise 2: Multi-dimensional Arrays --------------------------

# my_array = np.array('A') # 0 dimensional array
# my_array = np.array(['A', 'B', 'C', 'D']) # 1 dimensional array
# my_array = np.array([['A', 'B', 'C'],
#                      ['D', 'E', 'F'],
#                      ['G', 'H', 'I']]) # 2 dimensional array

my_array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                     [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                     [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]]) # 3 dimensional array

# You can go to even higher dimensions

# print(my_array.ndim) # Checking the dimensions of an array
# print(my_array.shape) # Returns a tuple of integers. Shows depth, rows, columns
# print(my_array[0][0][0]) # Chain indexing
# print(my_array[0, 0, 0]) # Multidimensional indexing

# Exercise - Create a 3 letter word using string concatenation

# word = (my_array[1, 2, 0] + my_array[0, 0, 0] + my_array[1, 1, 1] + my_array[0, 1, 0] + my_array[0, 0, 0])

# print(word)

# Exercise 3: Slicing --------------------------
