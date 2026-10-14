# A simple python function that builds spatial query tables

def build_spatial_query(table_name: str = "", *columns, **filters):
    """Function that builds a simple spatial query table"""
    if not table_name:
        table_name = input("Enter the name of the table: ").lower().strip()
        print(f"You have successfully created table: '{table_name}'")

    # Implementing columns
    if not columns:
        print("Write the columns you will use")

    for item in columns:
            print(item)
            
    for key in filters.keys():
         print(key)

build_spatial_query("miam", "id", "reset_value", "new", is_free = "Yes/No", id_value = "Id_value")
