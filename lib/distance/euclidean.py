from scipy.spatial import distance
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np 
import time 

a = np.array((2.13, 6.81, -5.01, 0.88, 6.15, -1.56, 7.77, 2.84, 1.94, -9.11, 0.87, -0.99, 8.55))
b = np.array((5.81, -2.18, -0.03, 7.16, 6.64, 3.34, 0.01, -9.95, -8.87, 0.63, 4.78, 7.11, 3.03))


Scipy_euclidean_start = time.time()
Scipy_euclidean_dist = distance.euclidean(a, b)
print('Scipy euclidean:\t',Scipy_euclidean_dist, time.time() - Scipy_euclidean_start)

Numpy_euclidean_start = time.time()
Numpy_euclidean_dist = np.linalg.norm(a-b)
print('Numpy euclidean:\t', Numpy_euclidean_dist, time.time() - Numpy_euclidean_start)

Sklearn_euclidean_start = time.time()
Sklearn_euclidean_dist = euclidean_distances([a], [b])
print('Sklearn euclidean:\t', Sklearn_euclidean_dist, time.time() - Sklearn_euclidean_start)

def Custom_euclidean(vector1, vector2):
    distance = np.sqrt(np.sum((vector1 - vector2) ** 2))
    return distance
Custom_sum_start = time.time()
Custom_sum_dist = Custom_euclidean(a,b)
print('Custom sum euclidean:\t', Custom_sum_dist, time.time() - Custom_sum_start)





