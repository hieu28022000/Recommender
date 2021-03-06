from collections import Counter

import __init__
import json
import numpy as np
import pandas as pd
from libs.distance.sigmoid import sigmoid
from libs.word_to_vec.object_w2v import object_w2v
from libs.mark_score.attribute_mark_score import Mark_score
import argparse
from datetime import datetime


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


    def get_attr(self):
        return [self.demand,
                self.price,
                self.area,
                self.location,
                self.bedroom,
                self.wc,
                self.furniture,
                self.juridical,
                self.view,
                self.floor,
                self.hot]


    @classmethod
    def get_request(cls):
        parser = cls.parser_args()
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
        # request_input = ['B??n', '2400000000', 'None', 'B??nh D????ng', '2', '2', 'Full', 'HDMB', '????ng Nam', '10', 'None']
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
    def load_config(cfg_path):
        cfg = []
        with open(cfg_path) as json_file:
            data = json.load(json_file)
        for info in data:
            cfg.append(int(data[info]))
        return cfg


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
    def partition(list_score, dataset, low, high):
        data = list_score[0]
        pivot = list_score[0][(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while list_score[0][i] < pivot:
                i += 1
            j -= 1
            while list_score[0][j] > pivot:
                j -= 1

            if i >= j:
                return j

            for index in range(4):
                list_score[index][i], list_score[index][j] = list_score[index][j], list_score[index][i]
            dataset[i], dataset[j] = dataset[j], dataset[i]


    @classmethod
    def quick_sort_first(cls, nums, dataset):
        # Create a helper function that will be called recursively
        def _quick_sort(items, data, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = cls.partition(items, data, low, high)
                _quick_sort(items, data, low, split_index)
                _quick_sort(items, data, split_index + 1, high)

        _quick_sort(nums, dataset, 0, len(nums[0]) - 1)


    @staticmethod
    def partition1(data, data1, dataset, low, high):
        pivot = data[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while data[i] < pivot:
                i += 1

            j -= 1
            while data[j] > pivot:
                j -= 1

            if i >= j:
                return j
            data[i], data[j] = data[j], data[i]
            data1[i], data1[j] = data1[j], data1[i]
            dataset[i], dataset[j] = dataset[j], dataset[i]


    @classmethod
    def quick_sort_first1(cls, list_score, list_score1, dataset):
        # Create a helper function that will be called recursively
        def _quick_sort(items, items1, data, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = cls.partition1(items, items1, data, low, high)
                _quick_sort(items, items1, data, low, split_index)
                _quick_sort(items, items1, data, split_index + 1, high)

        _quick_sort(list_score, list_score1, dataset, 0, len(list_score) - 1)


    @classmethod
    def assign_sort_result(cls, list_score, dataset, request_input, index_sort, previous_index_sort, next_index_sort):
        temp_data_score = []
        temp_data_score1 = []
        temp_data = []
        index_data = []
        for index in range(0, len(list_score[index_sort])):
            if list_score[previous_index_sort][index] == request_input[previous_index_sort]:
                temp_data_score.append(list_score[index_sort][index])
                temp_data_score1.append(list_score[next_index_sort][index])
                temp_data.append(dataset[index])
                index_data.append(index)

        cls.quick_sort_first1(temp_data_score, temp_data_score1, temp_data)
        for index in range(len(index_data)):
            dataset[index_data[index]] = temp_data[index]
            list_score[index_sort][index_data[index]] = temp_data_score[index]
            list_score[next_index_sort][index_data[index]] = temp_data_score1[index]

    @classmethod
    # Ranking distance and output is index of top
    def ranking_output(cls, nums_top, request_input, list_score, dataset):
        list_data = []
        list_new_data = []
        for i in range(10):
            for j in range(len(list_score)):
                list_data.append(list_score[j][i])
            list_new_data.append(list_data)
            list_data = []

        for element in range(len(list_new_data)):
            for index in range(len(list_new_data[element])):
                if list_new_data[element][index] == None:
                    list_new_data[element][index] = 0

        cls.quick_sort_first(list_new_data, dataset)
        cls.assign_sort_result(list_new_data, dataset, request_input, 3, 0, 1)
        cls.assign_sort_result(list_new_data, dataset, request_input, 1, 3, 2)

        # for index in range(-1, -30, -1):
        #     print(dataset[index])
        # Result
        result = []
        for index in range(-1, -nums_top, -1):
            result.append(dataset[index])
        return result


    @classmethod
    def load_source(cls, number_top, request_input, map_path, dataset_path, cfg_path):
        list_loc, list_map = cls.load_map(map_path)

        # Load dataset
        dataframe = cls.load_dataset(dataset_path)

        # Load config
        cfg = cls.load_config(cfg_path)

        # Convert request from string to number
        request_vector = object_w2v(request_input, list_loc, list_map)
        request_score = Mark_score.object_mark_score(request_vector, request_vector, list_map)
        request_data_score = request_score.get_data()
        # Create dataset score
        dataset = []
        dataset_score = []
        for index in range(len(dataframe)):
            # Get data
            data_line = cls.get_line(index, dataframe)
            dataset.append(data_line)
            # Convert to vector
            data_line_vector = object_w2v(data_line, list_loc, list_map)
            # Calculate score
            data_line_score = Mark_score.object_mark_score(data_line_vector, request_vector, list_map)
            dataset_score.append(data_line_score.get_data())


        indexs_of_top = cls.ranking_output(number_top, request_data_score, dataset_score, dataset)
        top = []
        for index in indexs_of_top:
            rank_object = cls(index[0],
                              index[1],
                              index[2],
                              index[3],
                              index[4],
                              index[5],
                              index[6],
                              index[7],
                              index[8],
                              index[9],
                              index[10])
            top.append(rank_object)
        return top




