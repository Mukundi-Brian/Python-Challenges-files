# # A simple python function that builds spatial query tables

# # A good function should not handle input data inside the logic
# # Defining what this function will do:
# #   1. It will take in parameters: (table_name, *columns, **filters)
# #   2. It will process whatever data was entered and return an SQL query
# #   3. Therefore, user input should be outside the function

# def build_spatial_query(table_name, *columns, **filters):
#     """Function that builds a simple spatial query table"""
#     # Implementing columns
#     if not columns:
#         print("No columns found")
#         columns = list(columns)
#         while True:
#             column_name = input("Write the name of the column to add: ").strip().lower()
#             columns.append(column_name)
#             more_columns = input("Do you wish to enter another column (y/n): ").strip().lower()
#             if not more_columns == "y":
#                 break
#             else:
#                 continue
#     # Query selector
#     # Basic queries: SELECT, WHERE, FROM
#     print("-----------Query Builder------------")
#     build_query = input("Do you want to use the query builder? (y/n):  ").strip().lower()
#     if build_query == "y":
#        # Printing columns
#         print("-----------Your Columns------------")
#         for item in columns:
#             print(f" - {item}")
#         while True:
#             column_choice = input("Enter the name of the column to SELECT (* to select all): ").lower().strip()
#             if column_choice in columns:
#                 break
#             elif column_choice == "*":
#                 print("-----------Your Columns------------")
#                 for item in columns:
#                     print(f" - {item}")
#                 exit()
#             else:
#                 print(f"'{column_choice}' not found")
#                 continue

#         # printing filters for user:
#         print("-----------Your Filters------------")
#         for key, value in filters.items():
#             print(f"{key}: {value}")

#         while True:
#             filter_choice = input("Enter the name of the filter to use: ").lower().strip()
#             if filter_choice in filters:
#                 filter_choice = filters[filter_choice]
#                 break
#             else:
#                 print(f"'{filter_choice}' was not found")
#                 continue

#     else:
#         print("Exiting Program, have a great day.")
#         exit()

#     return (f"SELECT {column_choice} using filter '{filter_choice}' FROM table '{table_name}'")

# print(build_spatial_query("My_table", is_free = "Yes/No", id_value = "Id_value", has_attributes = "Yes/No", area = "Area"))

def build_spatial_query(table_name, *columns, **filters):
    """Function that builds a simple spatial query table"""

    # Column builder
    if columns:
        column_string = ", ".join(columns)
    else:
        column_string = "*"

    # Filter Builder
    if filters:
        filter_string = ", ".join(filters)
    else:
        filter_string = ";"

    sql_query =  f"SELECT '{column_string}' FROM table '{table_name}' WHERE {filter_string}"

    return sql_query



# Accepting user_input
named_table = input("Enter the name of the table: ")
print(f"Successfully added '{named_table}'")
named_columns = ["id", "location", "pop_density"]
table_filters = {
    "is_free" : "yes/no",
    "id" : "id_value",
    "has_attributes" : "yes/no",
    "area" : "area_km^2"
}
is_adding_columns = True
is_adding_filters = True

while is_adding_columns:
    user_choice_add = input("Do you want to add columns? (y/n): ").strip().lower()
    if not user_choice_add == "y":
        is_adding_columns = False
    else:
        named_column = input("Enter the name of the column to add: ")
        if named_column in named_columns:
            print(f"'{named_column}' already exists")
            continue
        else:
            named_columns.append(named_column)

while is_adding_filters:
    user_choice_add = input("Do you want to add filters? (y/n): ").strip().lower()
    if not user_choice_add == "y":
        is_adding_filters = False
    else:
        table_filter = input("Enter the name of the filter to add: ")
        table_filter_role = input("Enter the value of the filter: ")
        if table_filter in table_filters:
            print(f"'{table_filter}' already exists")
            continue
        else:
            table_filters[table_filter] = table_filter_role

is_choosing_settings = True

while is_choosing_settings:
    print("\n-----------Your Columns------------")
    for column in named_columns:
        print(f" - {column}")

    chosen_column = input("Enter the name of the column to use (q for none): ").strip().lower()
    if chosen_column == "q":
        is_choosing_settings = False
    elif chosen_column not in named_columns:
        print(f"{chosen_column} not found")
        continue

    print("\n-----------Your Filters------------")
    for key, value in table_filters.items():
        print(f"{key}: {value}")
        
    chosen_filter = input("Enter the name of the column to use (q for none):  ").strip().lower()
    if chosen_filter == "q":
        is_choosing_settings = False
    elif chosen_filter not in table_filters:
        print(f"{chosen_filter} not found")

# build_spatial_query(user_table_name, user_columns, filters = table_filters)
print(build_spatial_query(named_table, *named_columns, **table_filters))
