import pandas as pd

# df = pd.read_csv("Bro_code_pokemonData.csv", index_col="Name")
df = pd.read_csv("Bro_code_pokemonData.csv")

# Selection by column
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df[["Name", "Height", "Weight"]].to_string())

# Selection by rows
# print(df.loc["Charizard": "Blastoise", ["Height", "Weight"]])
# print(df.iloc[0:11:2, 0:3])

# pokemon = input("Enter a pokemon name: ")

# try:
    # print(df.loc[pokemon])
# except KeyError:
    # print(f"{pokemon} not found")

# Filtering = keeping rows that match a condition

# tall_pokemon = df[df["Height"] >= 2]
# heavy_Pokemon = df[df["Weight"] > 100]
# Legendary_Pokemon = df[df["Legendary"] == True]
# Water_Pokemon = df[(df["Type1"] == "Water") | 
#                    (df["Type2"] == "Water") ]
# Ff_pokemon = df[(df["Type1"] == "Fire") &
#                 (df["Type2"] == "Flying")]

# print(Ff_pokemon)

# Aggregation = Reduces a set of values into a single summary value
# used to summarise and analyze data often used with the groupby() function
# Mean/Averge etc

# Apply to the whole dataframe
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# Apply to a single column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

# Groupby function

# group = df.groupby("Type1")

# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
# print(group["Height"].count())

# Data Cleaning - the process of fixing/removing: incomplete, incorrect, or irrelevant
# data, ~75% of work done with pandas is data cleaning

# 1. Dropping irrelevant columns

# df = df.drop(columns=["Legendary", "No"])

# 2. Handling missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2": "None"})

# 3. Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE",
                                #    "Water": "WATER"})

# 4. Standardize Text
# df["Name"] = df["Name"].str.lower()

# 5. Change or fix data types
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicate data
# df = df.drop_duplicates()

print(df.to_string())
