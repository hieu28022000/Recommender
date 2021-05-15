import numpy as np
import pandas as pd
import sklearn as skl

# Read dataset file
def Read_dataset(dataset_path):
    dataset = pd.read_csv(dataset_path).drop('Unnamed: 0', axis=1)
    return dataset

# Calcualte distance of obj and request with Numpy euclidean
def Cal_distance(score):
    score1D = np.array(score)
    ground_truth1D = np.array((10., 10., 10., 10., 10., 10., 10., 10., 10., 10., 10.))
    distance = np.linalg.norm(score1D - ground_truth1D)
    return distance

# Ranking distance and output is index of top
def Ranking_output(nums_top, list_values):  
    index_sorted = sorted(range(len(list_values)), key=list_values.__getitem__)
    index_top = []
    for num in range(nums_top):
        index_top.append(index_sorted[num])
    return index_top








dataset_path = '../dataset/Myhub_dataset.csv'
dataset = Read_dataset(dataset_path)
print(dataset)