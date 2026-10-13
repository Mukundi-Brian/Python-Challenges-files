# Simple GIS layer manager

# Imports
from abc import ABC, abstractmethod

vector_types = ("point", "line", "polygon")
raster_types = ("grid", "cells")

mixed_types = ["point", "grid", "cells", "line", "polygon"]
organized_vectors = []
organized_rasters = []
unknown_types = []

class MapLayer(ABC):
    """Abstract class that serves as blueprint for creating layers"""

    @abstractmethod
    def render(self):
        """Function that dictates how a class renders layers"""

    @abstractmethod
    def type_determiner(self):
        """This function will go through a mixed list of raster and vector types and sorts them accordingly"""

class VectorLayer(MapLayer):
    """A class that renders vectors (points, lines, polygons)"""
    def __init__(self, data_type = "Unknown"):
        self.data_type = data_type

    def type_determiner(self):
        for vector in mixed_types:
            if vector in vector_types:
                organized_vectors.append(vector)

        print("------- Vector Types --------")
        for line in vector_types:
            print(f" - {line}")
    
    def render(self):
        self.type_determiner()
        for line in organized_vectors:
            print(f"Vector layer is rendering {line}...")

class RasterLayer(MapLayer):
    """A class that renders rasters (in grids or cells)"""
    def __init__(self, data_type = "Unknown"):
        self.data_type = data_type

    def type_determiner(self):
        for item in mixed_types:
            if item in raster_types:
                organized_rasters.append(item)

        print("------- Raster Types --------")
        for line in raster_types:
            print(f" - {line}")

    def render(self):
        self.type_determiner()
        for line in organized_rasters:
            print(f"Raster layer is rendering {line}...")

# def data_type_determiner():
#     """This function will go through a mixed list of raster and vector types and sorts them accordingly"""
#     for item in mixed_types:
#         if item in vector_types: 
#             organized_vectors.append(item)

#         elif item in raster_types:
#             organized_rasters.append(item)

#         else:
#             unknown_types.append(item)

vector_1 = VectorLayer()
raster_1 = RasterLayer("500*500 grid")
# data_type_determiner()

# print("-------- Vector Types --------")
# for line in vector_types:
#     print(f" - {line}")

# print("-------- Raster Types --------")
# for line in raster_types:
#     print(f" - {line}")

# print("-------- Unknown Types --------")
# for line in unknown_types:
#     print(f" - {line}")

# raster_1.type_determiner()
# vector_1.type_determiner()

raster_1.render()
vector_1.render()
