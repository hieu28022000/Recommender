from scipy.spatial import distance
from sklearn.metrics.pairwise import cosine_distances
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import time 

a = np.array((2.13, 6.81, -5.01, 0.88, 6.15, -1.56, 7.77, 2.84, 1.94, -9.11, 0.87, -0.99, 8.55))
b = np.array((5.81, -2.18, -0.03, 7.16, 6.64, 3.34, 0.01, -9.95, -8.87, 0.63, 4.78, 7.11, 3.03))

Scipy_cosin_start = time.time()
Scipy_cosin_dist = distance.cosine(a,b)
print('Scipy cosin:\t', Scipy_cosin_dist, time.time() - Scipy_cosin_start)

Numpy_cosin_start = time.time()
Numpy_cosin_dist = 1 - np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
print('Numpy cosin:\t', Numpy_cosin_dist, time.time() - Numpy_cosin_start)

Sklearn_cosin_start = time.time()
Sklearn_cosin_dist = cosine_distances([a],[b])
print('Sklearn cosin:\t', Sklearn_cosin_dist, time.time() - Sklearn_cosin_start)

# Sklearn_cosins_start = time.time()
# Sklearn_cosin_simi = cosine_similarity([a],[b])
# print('Sklearn cosin simi:\t', Sklearn_cosin_simi, time.time() - Sklearn_cosins_start)
