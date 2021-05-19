import __init__
from libs.mark_score.attribute_mark_score import *

def object_mark_score(data_vector, request_vector, list_map):
    demand_score = demand_mark_score(data_vector[0], request_vector[0])
    price_score = price_mark_score(data_vector[1], request_vector[1], data_vector[0])
    area_score = area_mark_score(data_vector[2], request_vector[2])
    location_score = location_mark_score(data_vector[3], request_vector[3], list_map)
    num_of_bedroom_score = num_of_bedroom_mark_score(data_vector[4], request_vector[4])
    num_of_WC_score = num_of_WC_mark_score(data_vector[5], request_vector[5])
    furniture_score = furniture_mark_score(data_vector[6], request_vector[6])
    juridical_score = juridical_mark_score(data_vector[7], request_vector[7])
    view_score = view_mark_score(data_vector[8], request_vector[8])
    floor_score = floor_mark_score(data_vector[9], request_vector[9])
    hot_score = hot_mark_score(data_vector[10], request_vector[10])
    object_score = [demand_score, price_score, area_score, location_score, num_of_bedroom_score, \
        num_of_WC_score, furniture_score, juridical_score, view_score, floor_score, hot_score]
    return object_score