import pandas as pd

calories = {"Day 1" : 1750, "Day 2": 2100, "Day 3": 1700}

Calories_tracked = pd.Series(calories)
# series.index=['a', 'b', 'c']
# series.loc["Day 3"] += 500
# print(Calories_tracked)

data = {"Name": ["Spongebob", "Squidward", "Patrick"],
         "Age": [30, 50, 35]
         }
dataframe = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])

# Add a new column
dataframe ["Job"] = ["Cook", "Cashier", "N/A"]

# Add a new rows
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                         {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                       index=["Employee 4", "Employee 5"])

dataframe = pd.concat([dataframe, new_rows])
print(dataframe)