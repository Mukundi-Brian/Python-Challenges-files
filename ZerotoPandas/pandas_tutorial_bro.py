# Pandas = panel data, it is a python library built on top of numpy
# It is used in fields mostly:
#   1. Data analysis
#   2. Data science
#   3. Machine learning

# You typically work with:
#   1. Series - like a 1-d labeled column
#   2. Dataframe - like a 2-d labeled grid or table

import pandas as pd

# print(pd.__version__) # Current version of pandas


# Lesson 1: Series ------------------------------------------

# Series = A pandas 1-d labeled array that can hold any data type. Think of it like a single column in a spreadsheet (1-dimensional)

# data = [100, 102, 104, 200, 202,]
# data = ["A", "B", "C"]
# data = [True, False, True]

# series = pd.Series(data) # Constructing series
# series = pd.Series(data, index=["Door #1", "Door #2", "Door #3", "D", "E"]) # Making a custom index label

# print(series)
# print(series.loc["Door #2"]) # Access a value directly in a series
# print(series.loc["Door #3"]) # Access a value directly in a series

# series.loc["Door #3"] = 200 # Accessing a specific value and updating it
# print(series.iloc[0]) # Accessing by integer position

# print(series) # Access a value directly in a series

# Filtering by values
# print(series[series < 200])

# calories = {
#     "Day 1": 1750,
#     "Day 2": 2100,
#     "Day 3": 1700
# }

# series = pd.Series(calories)

# series.loc["Day 3"] += 500
# print(series)
# print(series.loc["Day 1"])
# print(series.loc["Day 3"])

# Filter by value
# print(series[series >= 2000])
# print(series[series < 2000])


# Lesson 2: Dataframes ------------------------------------------

# DataFrame = A tabular data structure with rows AND columns. (2-D). Similar to an excel spreadsheet

# data = {
#     "Name": ["Ferda", "Valdrova", "Luri", "Burnell", "Zed"],
#     "Age": [20, "???", "???", 25, 30]
# }

# df = pd.DataFrame(data, index=["Employee #1", "Employee #2", "Employee #3","Employee #4","Employee #5",])

# # print(df)

# # print(df.loc["Employee #2"])
# # print(df.loc["Employee #5"])
# # print(df.loc["Employee #1"])

# # Adding a new column
# df["Job"] = ["Regent", "N/A", "Housekeeper", "Engineer", "Knight"]

# # Adding a new row
# # Easiest way is to create a new dataframe then concatenate it
# new_row = pd.DataFrame([{"Name": "Malcom", "Age": 32, "Job": "Knight"}], index=["Employee #6"])
# df = pd.concat([df, new_row])


# # Adding new rows
# new_rows = pd.DataFrame([{"Name": "Isabella", "Age": "???", "Job": "Administrator"},
#                          {"Name": "Echdina", "Age": 28, "Job": "Researcher"}], index=["Employee #7", "Employee #8"])

# df = pd.concat([df, new_rows])
# # print(df.iloc[4])
# print(df)




# Lesson 3: Importing ------------------------------------------
# The next lessons are in importing_csv_pandas.py
# Alright fine I will redo it here

# df = pd.read_csv("ZerotoPandas/Bro_code_pokemonData.csv")

# print(df)
# print(df.to_string()) # This will print everything




# Lesson 4: Selection ------------------------------------------

# df = pd.read_csv("ZerotoPandas/Bro_code_pokemonData.csv")

# Selection by column
# print(df["Name"])
# print(df["Name"].to_string()) # Prints everything
# print(df["Height"])
# print(df["Weight"].to_string())
