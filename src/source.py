import __init__
import json
import numpy as np
import pandas as pd
from libs.distance.sigmoid import sigmoid
from libs.word_to_vec.object_w2v import object_w2v
from libs.mark_score.attribute_mark_score import Mark_score
from libs.distance.object_distance import object_distance
import argparse


class Source:

    def __init__(self,
                 demand,
                 price,
                 area,
                 location,
                 bedroom,
                 wc,
                 furniture,
                 juridical,
                 view,
                 floor,
                 hot):
        self.demand = demand
        self.price = price
        self.area = area
        self.location = location
        self.bedroom = bedroom
        self.wc = wc
        self.furniture = furniture
        self.juridical = juridical
        self.view = view
        self.floor = floor
        self.hot = hot


    @staticmethod
    def parser_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("--demand", type=str)
        parser.add_argument("--price", type=str)
        parser.add_argument("--area", type=str, default='None')
        parser.add_argument("--location", type=str)
        parser.add_argument("--no_bedroom", type=str, default='None')
        parser.add_argument("--no_WC", type=str, default='None')
        parser.add_argument("--furniture", type=str, default='None')
        parser.add_argument("--juridical", type=str, default='None')
        parser.add_argument("--view", type=str, default='None')
        parser.add_argument("--floor", type=str, default='None')
        parser.add_argument("--hot", type=str, default='False')
        return parser.parse_args()


    @staticmethod
    def get_request():
        # parser = parser_args()
        # demand = parser.demand

        # price = parser.price

        # area = parser.area

        # location = parser.location

        # no_bedroom = parser.no_bedroom

        # no_WC = parser.no_WC

        # furniture = parser.furniture

        # juridical = parser.juridical

        # view = parser.view

        # floor = parser.floor

        # hot = parser.hot

        # request_input = [demand,
        #                  price,
        #                  area,
        #                  location,
        #                  no_bedroom,
        #                  no_WC,
        #                  furniture,
        #                  juridical,
        #                  view,
        #                  floor,
        #                  hot]
        request_input = ['Bán', '2100000000', '56.7', 'Quận 9', '3', '2', 'Full', 'None', 'Tây Nam', '10', 'False']
        return request_input


    @staticmethod
    def load_map(map_path):
        map = json.load(open(map_path, encoding='utf8'))
        list_location = []
        list_map = []
        for loc in map:
            list_location.append(loc.lower())
            x_loc = map[loc]['x']
            y_loc = map[loc]['y']
            list_map.append([x_loc, y_loc])
        return list_location, list_map


    @staticmethod
    def load_dataset(dataset_path):
        dataset = pd.read_csv(dataset_path).drop('Unnamed: 0', axis=1)
        return dataset


    @staticmethod
    # Load on-off attribute
    def load_onoff(onoff_file_path):
        onoff = open(onoff_file_path).read().split(',')
        list_onoff = []
        for o in onoff:
            list_onoff.append(int(o))
        return list_onoff


    @staticmethod
    # Load config
    def load_config(cfg_path):
        cfg = []
        with open(cfg_path) as json_file:
            data = json.load(json_file)
        for info in data:
            cfg.append(int(data[info]))
        return cfg


    @staticmethod
    # Get line in dataset
    def get_line(num_line, dataset):
        line = dataset[num_line:num_line + 1]
        line = line.values[0]
        result_line = []
        for attribute in line:
            result_line.append(str(attribute))
        return result_line


    @staticmethod
    # Update score with cofig
    def normalize_with_cofig(score, cfg):
        result = []
        for index in range(len(score)):
            if score[index] == None:
                result.append(None)
            else:
                result.append(score[index] * sigmoid(int(cfg[index]) * 5 / int(max(cfg))))
        return result


    @staticmethod
    # Ranking distance and output is index of top
    def ranking_output(nums_top, list_values):
        if len(list_values) < nums_top:
            nums_top = len(list_values)
            print('Chỉ có chừng này thôi ><!')
        index_sorted = sorted(range(len(list_values)), key=list_values.__getitem__)
        index_top = []
        for num in range(nums_top):
            index_top.append(index_sorted[num])
        return index_top


    @classmethod
    def run_source(cls, request_input, map_path, dataset_path, cfg_path, number_rank):
        list_loc, list_map = cls.load_map(map_path)
        dataset = cls.load_dataset(dataset_path)
        cfg = cls.load_config(cfg_path)
        request_w2v = object_w2v(request_input, list_loc, list_map)
        list_distance = []
        same_demand_dataset = []
        for index in range(len(dataset)):
            # INPUT
            data_input = cls.get_line(index, dataset)
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
            # print(data_w2v)
            # Score
            object_data = Mark_score.object_mark_score(data_w2v, request_w2v, list_map)
            data_score = object_data.get_data()
            # print(data_score)
            # Update score with config
            data_score = cls.normalize_with_cofig(data_score, cfg)
            # print(data_score)
            # DISTANCE
            data_dist = object_distance(data_score)
            list_distance.append(data_dist)

        indexs_of_top = cls.ranking_output(number_rank, list_distance)
        return indexs_of_top, same_demand_dataset




