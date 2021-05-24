import __init__
import json
import numpy as np
import pandas as pd
from libs.distance.sigmoid import sigmoid
from libs.word_to_vec.object_w2v import object_w2v
from libs.mark_score.object_mark_score import object_mark_score
from libs.distance.object_distance import object_distance
import argparse

def parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demand", type = str)
    parser.add_argument("--price", type = str)
    parser.add_argument("--area", type = str, default = 'None')
    parser.add_argument("--location", type = str)
    parser.add_argument("--no_bedroom", type = str, default = 'None')
    parser.add_argument("--no_WC", type = str, default = 'None')
    parser.add_argument("--furniture", type = str, default = 'None')
    parser.add_argument("--juridical", type = str, default = 'None')
    parser.add_argument("--view", type = str, default = 'None')
    parser.add_argument("--floor", type = str, default = 'None')
    parser.add_argument("--hot", type = str, default = 'False')
    return parser.parse_args()


def Get_request():
    parser = parser_args()
    demand = parser.demand

    price = parser.price

    area = parser.area

    location = parser.location

    no_bedroom = parser.no_bedroom

    no_WC = parser.no_WC

    furniture = parser.furniture

    juridical = parser.juridical

    view = parser.view

    floor = parser.floor

    hot = parser.hot

    request_input = [demand, price, area, location, no_bedroom, no_WC, furniture, juridical, view, floor, hot]
    return request_input

# Load map function return list name location and list location on map
def Load_map(map_path):
    map = json.load(open(map_path, encoding='utf8'))
    list_location = []
    list_map = []
    for loc in map:
        list_location.append(loc.lower())
        x_loc = map[loc]['x']
        y_loc = map[loc]['y']
        list_map.append([x_loc, y_loc])
    return list_location, list_map

# Load dataset function return dataset type board csv
def Load_dataset(dataset_path):
    dataset = pd.read_csv(dataset_path).drop('Unnamed: 0', axis=1)
    return dataset

# Load on-off attribute
def Load_onoff(onoff_file_path):
    onoff = open(onoff_file_path).read().split(',')
    list_onoff = []
    for o in onoff:
        list_onoff.append(int(o))
    return list_onoff

# Load config
def Load_config(cfg_path):
    cfg = []
    with open(cfg_path) as json_file:
        data = json.load(json_file)
    for info in data:
        cfg.append(int(data[info]))
    return cfg

# Get line in dataset
def Get_line(num_line, dataset):
    line = dataset[num_line:num_line+1]
    line = line.values[0]
    result_line = []
    for attribute in line:
        result_line.append(str(attribute))
    return result_line

# Update score with cofig
def Normalize_with_cofig(score, cfg):
    result = []
    for index in range(len(score)):
        if score[index] == None:
            result.append(None)
        else:
            result.append(score[index] * sigmoid(int(cfg[index])*5 / int(max(cfg))))
    return result

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

# main function to run system
def run_source(request_input, map_path, dataset_path, cfg_path):
    list_loc, list_map = Load_map(map_path)
    dataset = Load_dataset(dataset_path)
    cfg = Load_config(cfg_path)
    request_w2v = object_w2v(request_input, list_loc, list_map)
    list_distance = []
    same_demand_dataset = []
    for index in range(len(dataset)):
        # INPUT
        data_input = Get_line(index, dataset)
        # W2V
        data_w2v = object_w2v(data_input, list_loc, list_map)

        if cfg[3] != 0:
            # View true
            if cfg[8] != 0:
                if data_w2v[0] == request_w2v[0] and data_w2v[3] == request_w2v[3] and data_w2v[8] == request_w2v[8]:
                    same_demand_dataset.append(data_input)
            # View false
            else:
                if data_w2v[0] == request_w2v[0] and data_w2v[3] == request_w2v[3]:
                    same_demand_dataset.append(data_input)
        else:
            # View true
            if cfg[8] != 0:
                if data_w2v[0] == request_w2v[0] and data_w2v[8] == request_w2v[8]:
                    same_demand_dataset.append(data_input)
            # View false
            else:
                if data_w2v[0] == request_w2v[0]:
                    same_demand_dataset.append(data_input)
    
    for data_input in same_demand_dataset:
        # W2V
        data_w2v = object_w2v(data_input, list_loc, list_map)
        # Score
        data_score = object_mark_score(data_w2v, request_w2v, list_map)
        # Update score with config
        data_score = Normalize_with_cofig(data_score, cfg)
        # DISTANCE
        data_dist = object_distance(data_score)
        list_distance.append(data_dist)
    indexs_of_top = Ranking_output(10, list_distance)
    for index in indexs_of_top:
        print(same_demand_dataset[index])
        # print(list_distance[index])
        

