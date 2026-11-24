# An autonomous warehouse robot has a map of its surroundings. Some locations are free, while others contain obstacles.
# Before moving, the robot checks the four cells immediately around it to determine which directions are safe.

# warehouse_data
warehouse = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

direction = {"up":(-1, 0),
             "down":(1, 0),
             "left":(0, -1),
             "right":(0, 1)
            }

# The function should:
# It should:
    #   1. Check 4 cells: up, down, left, right
    #   2. Identify which neighboring cells contain 0
    #   3. Return a list containing safe directions
    #   4. Ignore directions that lead outside the map

def find_safe_direction(grid, position_of_object):
    """Function that evaluates the immediate 4 cells and determines whether its safe to move"""
    # List for storing safe positions
    safe_positions = []
    # Unpacking the robot_position
    robot_pos_row, robot_pos_col = position_of_object
    for pos_name, (d_row, d_col) in direction.items():
        new_row = robot_pos_row + d_row
        new_col = robot_pos_col + d_col
        if new_row < 0 or new_row >= len(grid):
            print("Out of bounds")
            continue
        elif new_col < 0 or new_col >= len(grid[0]):
            print("Out of bounds")
            continue
        new_robot_pos = grid[new_row][new_col]
        if new_robot_pos == 0:
            # print(f"{pos_name}: safe")
            safe_positions.append(pos_name)
    if not safe_positions:
        safe_positions.append("No safe positions")
    return safe_positions

robot_position = (10, 1)
print(find_safe_direction(warehouse, robot_position))
