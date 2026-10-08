# print("Hello, World!")

# Mynum = 10

# print(Mynum)

# mynum = 20
# print(mynum)

# Python writing files (txt, json, csv)
# Writing text and lists
# For writing to a file for dictionaries we need
import json

# For writing to a file for csv, we need
import csv

my_csv = [
    ["Name", "Age", "Job"],
    ["Ferda", "19", "Regent"],
    ["Valdrova", "???", "Protector"],
    ["Luri", "???", "Housekeeper"],
    ["Isabella", "???", "Administrator"],
    ["Zed Swallow", "30", "Knight"]
]

my_employee = {
    "Name": "Isabella",
    "age": "???",
    "job": "Administrator",
    "class": "Dragon"
}

txt_data = "I love pizza 🍕"
employees = ["Ferda", "Valdrova", "Luri", "William", "Erika"]
file_path = "Output.txt"
file_path2 = "Output_for_lists.txt"
file_path3 = "Output_for_dict.json"
file_path4 = "Output_for_csv.csv"

# Writing for a txt
# with open(file_path, "w", encoding="utf-8") as file:
#     file.write(txt_data)
#     print(f"{file_path} created successfully")

# Writing for a list
# with open(file_path2, "w", encoding="utf-8") as file:
#     for employee in employees:
#         file.write(employee + ", ")
#     print(f"{file_path2} created successfully")

# Writing for a json
# Json file best for anything that has key value pairs
# with open(file_path3, "w", encoding="utf-8") as file:
#     json.dump(my_employee, file, indent=4)
#     print("Json file was created")

# Writing for a csv
# with open(file_path4, "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     for row in my_csv:
#         writer.writerow(row)
#     print("CSV file created successfully")

# Reading files (txt, json, csv)

# Reading txt file
# with open(file_path, "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# Reading a json file
# with open(file_path3, "r", encoding="utf=8") as file:
#     content = json.load(file)
#     print(content)

# Reading a csv file
# with open(file_path4, "r", encoding="utf=8") as file:
#     content = csv.reader(file)
#     for line in content:
#         print(line)
