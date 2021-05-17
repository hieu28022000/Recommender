import json
from numpy import double
from lib.distance.location_distance import *


def Load_map(map_path):
    map = json.load(open(map_path))
    x_location = []
    y_location = []
    list_location = np.zeros((20,2), dtype=float)
    i=0
    for location in map:
        j=0
        x_location.append(map[location]['x'])
        y_location.append(-map[location]['y'])
        list_location[i][j] = map[location]['x']
        j+= 1
        list_location[i][j] = map[location]['y']
        i+=1
    return x_location,y_location, list_location

def mark_demand(data_demand, request_demand):
    if int(data_demand) == int(request_demand):
        return 10
    return 0

def mark_price(value_attr, request):
    # money = 100000000
    result = abs(request - int(value_attr))
    # if(result>0 and result<money):
    #     return 4
    # elif(result>money and result<money*2):
    #     return 3
    # elif(result>money*2 and result<money*3):
    #     return 2
    # elif (result > money*3 and result<money*4):
    #     return 1
    # elif (result >-money and result < 0):
    #     return 10
    # elif (result > -money and result < -money*2):
    #     return 9
    # elif (result > -money*2 and result <-3*money):
    #     return 8
    # elif (result > -money*3 and result < -money*4):
    #     return 7
    # elif (result > -money*4 and result < -money*5):
    #     return 6
    # else:
    #     return 0
    if result < 100000000:
        return 10
    elif result < 300000000:
        return 5
    return 0


def mark_area(value_attr, request):
    result = request - float(value_attr)
    if(abs(result)<5):
        return 10
    elif(abs(result)<15):
        return 5
    else:
        return 0

def mark_location(rloc_num, loc_num):
    list_loc = Load_map('./lib/config/location_map.json')[2]
    x_re = list_loc[loc_num][0]
    y_re = list_loc[loc_num][1]
    x_data = list_loc[rloc_num][0]
    y_data = list_loc[rloc_num][1]
    dist = location_distance(x_re, y_re, x_data, y_data)
    list_dist = []
    for loc in list_loc:
        list_dist.append(location_distance(x_data, y_data, loc[0], loc[1]))
    max_dist = max(list_dist)
    dist = 10 - (dist/max_dist)*10
    return dist

def mark_room(value_attr, request):
    result = request - int(value_attr)
    if(abs(result)==0):
        return 10
    if(abs(result)==1):
        return 5
    else:
        return 0

def mark_wc(value_attr, request):
    result = request - int(value_attr)
    if(abs(result)==0):
        return 10
    if(abs(result)==1):
        return 5
    else:
        return 0
def mark_furniture(value_attr, request):
    if(value_attr==request):
        return 10
    else:
        return 0
def mark_juridical(value_attr, request):
    if(value_attr==request):
        return 10
    else:
        return 0

def mark_view(value_attr, request):
    if(request==value_attr):
        return 10
    return 0

def mark_floor(value_attr,request):
    floor = 0
    floor = request - int(value_attr)
    if(floor==0):
        return 10
    elif(floor==1 or floor==-1):
        return 9
    elif (floor == 2 or floor == -2):
        return 8
    elif (floor == 3 or floor == -3):
        return 7
    elif (floor == 4 or floor == -4):
        return 6
    elif (floor == 5 or floor == -5):
        return 5
    else:
        return 0

def mark_hot(value_attr):
    if(value_attr == 'true'):
        return 10
    return 0

