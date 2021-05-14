import numpy as np
import pandas as pd
import sklearn as skl

def Read_dataset(dataset_path):
    dataset = pd.read_csv(dataset_path).drop('Unnamed: 0', axis=1)
    return dataset







dataset_path = '../dataset/Myhub_dataset.csv'
dataset = Read_dataset(dataset_path)
print(dataset)