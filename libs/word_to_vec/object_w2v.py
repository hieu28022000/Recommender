import __init__
from libs.word_to_vec.attribute_w2v import *

def object_w2v(list_attribute_input, list_location, list_map):
    demand = demand_w2v(list_attribute_input[0])
    price = price_w2v(list_attribute_input[1])
    area = area_w2v(list_attribute_input[2])
    location = location_w2v(list_attribute_input[3], list_location, list_map)
    num_of_bedroom = num_of_bedroom_w2v(list_attribute_input[4])
    num_of_WC = num_of_WC_w2v(list_attribute_input[5])
    furniture = furniture_w2v(list_attribute_input[6])
    juridical = juridical_w2v(list_attribute_input[7])
    view = view_w2v(list_attribute_input[8])
    floor = floor_w2v(list_attribute_input[9])
    hot = hot_w2v(list_attribute_input[10])
    obj_vec = [demand, price, area, location, num_of_bedroom, num_of_WC, furniture, juridical, view, floor, hot]
    return obj_vec
