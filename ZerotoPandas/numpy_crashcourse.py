# Relearning numerical Python
import numpy as np

elevation_readings = np.array([100, 250, 300, 450, 200, 100])
coordinate_pts_meters = np.array([[1001,2200],
                                  [3001, 2000],
                                  [1150, 3120]])

# print(np.ndim(elevation_readings))
# print(np.shape(elevation_readings))
print(elevation_readings.dtype)

# print(np.ndim(coordinate_pts_meters))
# print(np.shape(coordinate_pts_meters))
print(coordinate_pts_meters.dtype)

# print(elevation_readings)
# print(coordinate_pts_meters)

# Row and column slicing and aggregate along axis = 0, axis = 1
# arr[start : stop : step]

east_coordinates = coordinate_pts_meters[:, 1]
north_coordinates = coordinate_pts_meters[:, 0]
last_two_rows = coordinate_pts_meters[1:]
# print(east_coordinates)
# print(north_coordinates)
print(last_two_rows)
