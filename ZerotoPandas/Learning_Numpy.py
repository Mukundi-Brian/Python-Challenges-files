# Numpy = Numerical Python
#       - A python library used for numerical computing
#       - Used in fields that need heavy data processing
#       - Under-hood its written with C
#       - Arrays are OP
#       - Vectorized Operations

# import numpy as np

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

# my_array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
#                      [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
#                      [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]]) # 3 dimensional array

# You can go to even higher dimensions

# print(my_array.ndim) # Checking the dimensions of an array
# print(my_array.shape) # Returns a tuple of integers. Shows depth, rows, columns
# print(my_array[0][0][0]) # Chain indexing
# print(my_array[0, 0, 0]) # Multidimensional indexing

# Exercise - Create a 3 letter word using string concatenation

# word = (my_array[1, 2, 0] + my_array[0, 0, 0] + my_array[1, 1, 1] + my_array[0, 1, 0] + my_array[0, 0, 0])

# print(word)

# Exercise 3: Slicing --------------------------

# my_array = np.array([[1, 2, 3, 4],
#                     [5, 6, 7, 8],
#                     [9, 10, 11, 12],
#                     [13, 14, 15, 16]])

# array[start: end: step]

# print(my_array[ :: -1]) # row selection
# print(my_array[:, -1]) # column selection
# print(my_array[:, 0:3]) # column selection
# print(my_array[:, 1::2]) # column selection
# print(my_array[:, :: -1]) # column selection
# print(my_array[0:2 , 2: ]) # Combined selection
# print(my_array[2: , 0: 2]) # Combined selection


# Exercise 4: Arithmetic --------------------------

# Scalar arithmetic - a single value

# my_array = np.array([1, 2, 3])

# print(my_array + 1)
# print(my_array - 2)
# print(my_array * 3)
# print(my_array / 4)
# print(my_array ** 5)

# Vectorized math functions - a single dimension, we can apply a function to an array without a loop

# my_array = np.array([1, 2, 3])

# my_array = np.array([1.01, 2.5, 3.99])

# print(np.sqrt(my_array))
# print(np.round(my_array))
# print(np.floor(my_array)) - always round down
# print(np.ceil(my_array)) - always round up

# print(np.pi)

# Exercise - convert radius to area of a circle

# radii = np.array([1, 2, 3])

# area_of_circle = pi r ** 2
# area_of_circle = np.pi * (radii ** 2)
# print(area_of_circle)

# print(np.pi * radii ** 2)

# Element-wise arithmetic

# array_1 = np.array([1, 2, 3])
# array_2 = np.array([4, 5, 6])

# print(array_1 + array_2)
# print(array_1 - array_2)
# print(array_1 * array_2)
# print(array_1 / array_2)
# print(array_1 ** array_2)

# Comparison operators - we can create boolean arrays, filter data and use element-wise comparisons

# scores = np.array([91, 55, 100, 73, 82, 64])

# print(scores == 100)
# print(scores >= 60)
# print(scores < 60)

# scores[scores < 60] = 0
# print(scores)



# Exercise 5: Broadcasting --------------------------

# Broadcasting allows numpy to perform operations on arrays with different shapes by virtually expanding dimensions so they match the larger array's shape

# A couple of rules for broadcasting:
# The dimensions have the same size OR one of the dimensions has a size of 1

# array_1 = np.array([[1, 2, 3, 4]])
# array_1 = np.array([[1, 2, 3, 4],
# #                     [5, 6, 7, 8]])
# array_1 = np.array([[1, 2, 3, 4],
#                     [5, 6, 7, 8],
#                     [9, 10, 11, 12],
#                     [13, 14, 15, 16]])

# # array_2 = np.array([[1], [2], [3], [4]])
# # array_2 = np.array([[1, 3], [2, 4], [3, 5], [4, 6]])

# print(array_1.shape)
# print(array_2.shape)

# print(array_1 * array_2)

# Exercise -  create a multiplication table using broadcasting

# array_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# array_2 = np.array([[1],
#                     [2],
#                     [3],
#                     [4],
#                     [5],
#                     [6],
#                     [7],
#                     [8],
#                     [9]])

# print(array_1.ndim)
# print(array_1.shape)

# print(array_2.ndim)
# print(array_2.shape)

# print(array_1 * array_2)

# array_1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
# array_2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])

# # print(array_1.ndim)
# print(array_1.shape)

# # print(array_2.ndim)
# print(array_2.shape)

# print(array_1 * array_2)



# Exercise 6: Aggregate functions --------------------------

# Aggregate functions = summarize data and typically return a single value

# my_array = np.array([[1, 2, 3, 4, 5],
#                      [6, 7, 8, 9, 10]])

# print(np.sum(my_array))
# print(np.mean(my_array))
# print(np.std(my_array))
# print(np.var(my_array))
# print(np.min(my_array))
# print(np.max(my_array))
# print(np.argmin(my_array))
# print(np.argmax(my_array))

# print(np.sum(my_array, axis=1)) # Axis can sum rows or columns



# Exercise 7: Filtering --------------------------

# Filtering = refers to the process of selecting elements from an array that match a given condition

# ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                #  [39, 22, 15, 99, 18, 19, 20, 21]])

# teenagers = ages[ages < 18] # Boolean indexing - it flattens out the array,  you can maintain shape using WHERE function

# adults = ages[(ages >= 18) & (ages < 65)]
# adults = ages[(ages < 18) | (ages >= 65)]

# seniors = ages[ages >= 65]
# evens = ages[ages % 2 == 0]
# odds = ages[ages % 2 != 0]

# print(odds)

# Where function - will keep original shape but is slower than boolean indexing

# adults = np.where(ages >= 18, ages, 0) # You need to write a replacement for the data that does not meet the condition, you can use 0, -1 or np.non

# print(adults)
# print(adults.ndim)



# Exercise 8: Random Numbers --------------------------

# Integers
# random_num_gen = np.random.default_rng(seed=1) # Seed allows us to reproduce the same results

# print(random_num_gen.integers(low=1, high=101, size=(3, 5)))

# floating point numbers

# np.random.seed(seed=1)
# print(np.random.uniform(low=-1, high=1, size=(2, 2)))

# Shuffling an array
# random_num_gen = np.random.default_rng()

# # array = np.array([1, 2, 3, 4, 5])
# # random_num_gen.shuffle(array)
# fruits = np.array(["apple", "banana", "coconut", "pizza"])
# fruits = np.array(["🍎", "🍌", "🥥", "🍕"])
# fruit = random_num_gen.choice(fruits, size=(2, 2))

# print(fruits)
# print(fruit)
