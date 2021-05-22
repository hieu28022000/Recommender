import __init__
from libs.distance.attribute_distance import *

# Attribute 0
# Demand mark score function return 10 if request demand same data demand else return 0
def demand_mark_score(data_demand, request_demand):
    if (data_demand == None) or (request_demand == None):
        return None

    demand_dist = demand_distance(data_demand, request_demand)
    if demand_dist == 0:
        return 10
    return 0


# Attribute 1
# Price mark score funtion return score of data price
def price_mark_score(data_price, request_price, demand):
    if (data_price == None) or (request_price == None ) or (demand == None):
        return None

    price_dist = price_distance(data_price, request_price)
    # if price_dist < 0:
    #     return 10
    # Demand is "Thuê"
    if demand == 0:
        if price_dist < 0 and price_dist > -5000000:
            return 10
        elif price_dist >= 0 and price_dist <= 1000000:
            return 8
        elif price_dist >= 0 and price_dist <= 1500000:
            return 5
    # Demand is "Bán"
    elif demand == 1:
        if price_dist < 0 and price_dist > -500000000:
            return 10
        elif price_dist >= 0 and price_dist <= 100000000:
            return 8
        elif price_dist >= 0 and  price_dist <= 300000000:
            return 5
    return 0

# Attribute 2
# Area mark score function return score of data area
def area_mark_score(data_area, request_area):
    if (data_area == None) or (request_area == None):
        return None

    area_dist = abs(area_distance(data_area, request_area))
    if area_dist <= 5:
        return 10
    elif area_dist <=5: 
        return 5
    return 0

# Attribute 3
# Location mark score function return score of data location
def location_mark_score(data_location, request_location, list_location):
    if (data_location == None) or (request_location == None):
        return 0

    location_dist = location_distance(data_location, request_location)
    list_dist = []
    for location in list_location:
        list_dist.append(location_distance(location, request_location))
    max_dist = max(list_dist)
    location_dist = 10 - (location_dist/max_dist)*10
    return location_dist

# Attribute 4
# Numbers of bedrooms mark score function return score of data num of bed
def num_of_bedroom_mark_score(data_no_bedroom, request_no_bedroom):
    if (data_no_bedroom == None) or (request_no_bedroom == None):
        return None

    no_bed_dist = abs(num_of_bedroom_distance(data_no_bedroom, request_no_bedroom))
    if no_bed_dist == 0:
        return 10
    elif no_bed_dist == 1:
        return 5
    return 0

# Attribute 5
# Numbers of WC mark score function return score of data num of WC
def  num_of_WC_mark_score(data_no_WC, request_no_WC):
    if (data_no_WC == None) or (request_no_WC == None):
        return None

    no_WC_dist = abs(num_of_WC_distance(data_no_WC, request_no_WC))
    if no_WC_dist == 0:
        return 10
    elif no_WC_dist == 1:
        return 5
    return 0

# Attribute 6
# Furniture mark score function return score of data furniture
def furniture_mark_score(data_furniture, request_furniture):
    if (data_furniture == None) or (request_furniture == None):
        return None

    furniture_dist = furniture_distance(data_furniture, request_furniture)
    if furniture_dist == 0:
        return 10
    elif furniture_dist == 1:
        return 5
    return 0

# Attribute 7
# Juridical mark score function return score of data juridical
def juridical_mark_score(data_juridical, request_juridical):
    if (data_juridical == None) or (request_juridical == None):
        return None

    juridical_dist = juridical_distance(data_juridical, request_juridical)
    if juridical_dist == 0:
        return 10
    return 0

# Attribute 8
# View mark score function return score of data juridical
def view_mark_score(data_view, request_view):
    if (data_view == None) or (request_view == None):
        return None

    view_dist = abs(view_distance(data_view, request_view))
    if view_dist == 0:
        return 10
    elif view_dist == 1:
        return 5
    return 0

# Attribute 9
# Floor mark score function return  score of data floor
def floor_mark_score(data_floor, request_floor):
    if (data_floor == None) or (request_floor == None):
        return None

    floor_dist = abs(floor_distance(data_floor, request_floor))
    if floor_dist <= 1: 
        return 10
    elif floor_dist <= 3:
        return 8
    elif floor_dist < 7:
        return 5
    return 0 

# Attribute 10
# Hot mark score function return score of data hot
def hot_mark_score(data_hot, request_hot):
    if (data_hot == None) or (request_hot == None):
        return None
        
    hot_dist = hot_distance(data_hot, request_hot)
    if hot_dist == 0:
        return 10
    return 0