from scipy.spatial import distance
from decimal import Decimal
import numpy_ml
import numpy as np
import time

a = np.array((2.13, 6.81, -5.01, 0.88, 6.15, -1.56, 7.77, 2.84, 1.94, -9.11, 0.87, -0.99, 8.55))
b = np.array((5.81, -2.18, -0.03, 7.16, 6.64, 3.34, 0.01, -9.95, -8.87, 0.63, 4.78, 7.11, 3.03))

Scipy_minkowski_start = time.time()
Scipy_minkowski_dist = distance.minkowski(a,b)
print('Scipy minkowski:\t',Scipy_minkowski_dist, time.time() - Scipy_minkowski_start)

Numpy_minkowski_start = time.time()
Numpy_minkowski_dist = numpy_ml.utils.distance_metrics.minkowski(a, b, 2)
Numpy_minkowski_end = time.time() - Numpy_minkowski_start
print('Numpy minkowski:\t', Numpy_minkowski_dist, Numpy_minkowski_end)

def Custom_minkowski(vector1, vector2):
    dec_sum = Decimal(sum(pow(abs(x-y), 2) for x, y in zip(vector1, vector2)))
    dec_device = Decimal(1/float(2))
    distance = round(dec_sum ** dec_device, 2)
    return distance
Custom_minkowski_start = time.time()
Custom_minkowski_dist = Custom_minkowski(a,b)
print('Custom minkowski:\t', Custom_minkowski_dist, time.time() - Custom_minkowski_start)