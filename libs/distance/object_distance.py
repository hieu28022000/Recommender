import __init__
import numpy as np

def object_distance(object_score):
    score_remove_None = []
    ground_truth = []
    for score in object_score:
        if score != None:
            score_remove_None.append(score)
            ground_truth.append(10.)
    score_remove_None = np.asarray(score_remove_None)
    ground_truth = np.asarray(ground_truth)
    # obj_distance = np.linalg.norm(score_remove_None - ground_truth)

    score_13 = np.array((object_score[1],object_score[3]))
    gr_tr = np.array((10.,10.))
    obj_distance = np.linalg.norm(score_13 - gr_tr)
    return obj_distance