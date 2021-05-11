import numpy as np
from numpy import linalg as LA
re = [10,10,10]
re = LA.norm(re)
result = []
s = []
x = [[1,2,3],
     [2,3,4],
     [2,5,6],
     [7,6,8]]
for i in x:
    result.append(LA.norm(i))

for i in result:
    s.append(i/re)

s.sort()
