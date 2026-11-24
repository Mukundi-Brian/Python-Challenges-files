# Testing code :)

# warehouse_data
warehouse = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
# print(len(warehouse))
# print(len(warehouse[0]))

direction = {"up":(-1, 0),
             "down":(1, 0),
             "left":(0, -1),
             "right":(0, 1)
            }

robot_position = (1, 1)

miam_names = []

miam_names.append("Miam")
miam_names.append("Muhahahaha, you are a genius")

print(miam_names)
# for pos_name, (d_row, d_col) in direction.items():
#     new_row = robot_position[0] + d_row
#     new_col = robot_position[1] + d_col
#     if new_row < 0 or new_row >= len(warehouse):
#         print("Out of bounds")
#         continue
#     elif new_col < 0 or new_col >= len(warehouse[0]):
#         print("Out of bounds")
#         continue
#     new_robot_pos = warehouse[new_row][new_col]
#     if new_robot_pos == 0:
#         print(f"{pos_name}: safe")
#     elif new_robot_pos == 1:
#         print(f"{pos_name}: unsafe")
#     else:
#         print("Something is wrong but I can't tell you what :)")
