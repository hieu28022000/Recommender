from numpy import linalg as la
def caculate_distance(s):
    result = []
    for i in range(len(s)):
        result.append(la.norm(s[i]))
    return result



