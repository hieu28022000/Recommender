import __init__

import json
import math
import numpy as np
import pandas as pd
import sklearn as skl

from time import time
from lib.mark_score.mark import *
from lib.string_to_vec.w2v import *
from lib.mark_score.mark_data import *
from lib.string_to_vec.dictionary import *


# Read dataset file
def Read_dataset(dataset_path):
    dataset = pd.read_csv(dataset_path).drop('Unnamed: 0', axis=1)
    return dataset

# Get line in dataset
def Get_line(num_line, dataset):
    line = dataset[num_line:num_line+1]
    line = line.values[0]
    return line

# Input
def Request_input():
    print('Nhập nhu cầu: ')
    nhu_cau = input()
    print('Nhập giá tiền: ')
    gia = int(input())
    # print('Nhập diện tích: ')
    # dien_tich = float(input())
    dien_tich = 70
    print('Nhập vị trí: ')
    dia_chi = input()
    # print('Nhập số phòng ngủ: ')
    # phong_ngu = int(input())
    phong_ngu = 2
    # print('Nhập số phòng vệ sinh: ')
    # phong_wc = int(input())
    phong_wc = 2
    # print('Nhập nội thất: ')
    # noi_that = input()
    noi_that = 'Có'
    # print('Nhập pháp lý sở hữu: ')
    # phap_ly = input()
    phap_ly = 'Sổ hồng'
    print('Nhập view/hướng: ')
    view = input()
    # print('Nhập số tầng: ')
    # tang = int(input())
    tang = 12
    # print('Có hot hay không:')
    # hot = bool(input())
    hot = 0
    request = [nhu_cau, gia, dien_tich, dia_chi, phong_ngu, phong_wc, noi_that, phap_ly, view, tang, hot]
    return request



# Calcualte distance of obj and request with Numpy euclidean
def Cal_distance(score):
    # score1D = np.array(score)
    # ground_truth1D = np.array((10., 10., 10., 10., 10., 10., 10., 10., 10., 10., 10.))
    score1D = np.array((score[1], score[3]*10))
    ground_truth1D = np.array((10., 100.))
    distance = np.linalg.norm(score1D - ground_truth1D)
    return distance

# Ranking distance and output is index of top
def Ranking_output(nums_top, list_values):  
    if len(list_values) < nums_top:
        nums_top = len(list_values)
        print('Chỉ có chừng này thôi ><!')
    index_sorted = sorted(range(len(list_values)), key=list_values.__getitem__)
    index_top = []
    for num in range(nums_top):
        index_top.append(index_sorted[num])
    return index_top

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Update score with cofig
def Normalize_with_cofig(score, cfg):
    result = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
    for index in range(11):
        result[index] = (score[index] * sigmoid(cfg[index]*5 / max(cfg)))
    return result

def Load_config(cfg_path):
    cfg = []
    with open(cfg_path) as json_file:
        data = json.load(json_file)
    for info in data:
        cfg.append(int(data[info]))
    return cfg

def Run(dataset_path, cfg_path):
    # INPUT
    request = Request_input()
    dataset = Read_dataset(dataset_path)
    cfg = Load_config(cfg_path)
    
    # PROCESSING
    request_vector = Convert_obj2vector(request, dataset)

    fit_dataset = []
    for index in range(len(dataset)):
        line = Get_line(index, dataset)
        line_vector = Convert_obj2vector(line, dataset)
        if (line[0] == request[0] and line[8] == request[8]):
            fit_dataset.append(line)
    # print(len(fit_dataset))

    
    list_distance = []
    for aparment in fit_dataset:
        line_vector = Convert_obj2vector(aparment, dataset)
        vector_score = mark_score(request_vector, line_vector)
        vector_score = Normalize_with_cofig(vector_score, cfg)
        distance = Cal_distance(vector_score)
        list_distance.append(distance)
    top = Ranking_output(10, list_distance)
    for i in top:
        print(fit_dataset[i])
