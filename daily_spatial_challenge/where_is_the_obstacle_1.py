# Write a Python function that converts a point from the robot's local coordinate system into a global coordinate system.

# imports
import math

# Where:
#   robot_x - robot's global position on the x axis
#   robot_y - robot's global position on the y axis
#   heading - head of the robot measured from East anti-clockwise in degrees
#   local_x - local x position of the object forward of the robot
#   local_y - local y position of the object left of the robot

def transform_point(robot_x, robot_y, heading, local_x, local_y):
    heading_in_radians = math.radians(heading)
    change_in_x = local_x * math.cos(heading_in_radians) - local_y * math.sin(heading_in_radians)
    change_in_y = local_x * math.sin(heading_in_radians) + local_y * math.cos(heading_in_radians)
    object_global_x = robot_x + change_in_x
    object_global_y = robot_y + change_in_y

    return object_global_x, object_global_y

def reverse_transform_point(robot_x, robot_y, heading, object_global_x, object_global_y):
    # Un-rotating the robot
    heading_in_radians = math.radians(-heading)
    change_in_x = object_global_x - robot_x
    change_in_y = object_global_y - robot_y
    local_x = change_in_x * math.cos(heading_in_radians) - change_in_y * math.sin(heading_in_radians)
    local_y = change_in_x * math.sin(heading_in_radians) + change_in_y * math.cos(heading_in_radians)
    return local_x, local_y

# x, y = transform_point(10, 5, 0, 3, 2) # 13, 7
# a, b = transform_point(10, 5, 90, 4, 2) # 8, 9
# i, j = transform_point(10, 5, 180, 3, 2) # 7, 3

x, y = reverse_transform_point(10, 5, 0, 13, 7)
a, b = reverse_transform_point(10, 5, 90, 8, 9)
i, j = reverse_transform_point(10, 5, 180, 7, 3)

print(f"({x:.2f}, {y:.2f})")
print(f"({a:.2f}, {b:.2f})")
print(f"({i:.2f}, {j:.2f})")
