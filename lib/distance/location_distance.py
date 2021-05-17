import numpy as np


def location_distance(x1, y1, x2, y2):
    point1 = np.array((x1, y1))
    point2 = np.array((x2, y2))
    loc_dist = np.linalg.norm(point1 - point2) 
    return loc_dist