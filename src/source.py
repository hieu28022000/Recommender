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
    # request_input = ['Bán', '2500000000', 'None', 'Bình Dương', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
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
def Ranking_output(nums_top, request_vector, list_score, cfg, dataset):  
    # Sort for first favorite
    first_favor_index = cfg.index(1)
    for i in range(len(list_score)):
        for j in range(i+1, len(list_score)):
            # dataset at i index
            i_att1 = list_score[i][first_favor_index]
            if i_att1 == None:
                i_att1 = 0
            # dataset at j index 
            j_att1 = list_score[j][first_favor_index]
            if j_att1 == None:
                j_att1 = 0

            # Compare
            if i_att1 < j_att1:
                # Swap dataset[i] and dataset[j]
                temp_data = dataset[i]
                dataset[i] = dataset[j]
                dataset[j] = temp_data
                # Swap list_score[i] and list_score[j]
                temp_score = list_score[i]
                list_score[i] = list_score[j]
                list_score[j] = temp_score


    # Sort for remain favorrite
    for favor in range(2, max(cfg)+1):
        favor_index = cfg.index(favor)
        # Check request[favor] 
        if request_vector[favor_index] != None:
            for i in range(len(list_score)):
                for j in range(i+1, len(list_score)):
                    if list_score[i][cfg.index(favor-1)] == list_score[j][cfg.index(favor-1)]:
                        
                        # dataset at i index
                        i_att = list_score[i][favor_index]
                        if i_att == None:
                            i_att = 0
                        # dataset at j index 
                        j_att = list_score[j][favor_index]
                        if j_att == None:
                            j_att = 0

                        # Compare
                        if i_att < j_att:
                            # Swap dataset[i] and dataset[j]
                            temp_data = dataset[i]
                            dataset[i] = dataset[j]
                            dataset[j] = temp_data
                            # Swap list_score[i] and list_score[j]
                            temp_score = list_score[i]
                            list_score[i] = list_score[j]
                            list_score[j] = temp_score

    # Result
    result = []
    for index in range(nums_top):
        result.append(dataset[index])   
    return result


# main function to run system
def run_source(request_input, map_path, dataset_path, cfg_path):
    # Load location name and map
    list_loc, list_map = Load_map(map_path)
    
    # Load dataset
    dataframe = Load_dataset(dataset_path)
    
    # Load config
    cfg = Load_config(cfg_path)
    
    # Convert request from string to number
    request_vector = object_w2v(request_input, list_loc, list_map)
    
    # Create dataset score 
    dataset = []
    dataset_score = []
    for index in range(len(dataframe)):
        # Get data
        data_line = Get_line(index, dataframe)
        dataset.append(data_line)
        # Convert to vector
        data_line_vector = object_w2v(data_line, list_loc, list_map)
        # Calculate score
        data_line_score = object_mark_score(data_line_vector, request_vector, list_map)
        dataset_score.append(data_line_score)

    # Ranking 
    top_10 = Ranking_output(10, request_vector, dataset_score, cfg, dataset)
    for top in top_10:
        print(top)
        