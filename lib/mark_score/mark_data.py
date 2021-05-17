import json
import numpy as np
from lib.mark_score import  mark

def Load_map(map_path):
    map = json.load(open(map_path))
    x_location = []
    y_location = []
    list_location = np.zeros((19,2), dtype=float)
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

def mark_score(request, data_line):
    vectors = data_line
    demand = mark.mark_demand(vectors[0], request[0])
    price = mark.mark_price(vectors[1], request[1])
    area = mark.mark_area(vectors[2], request[2])
    location = mark.mark_location(vectors[3], request[3])
    room = mark.mark_room(vectors[4],request[4])
    wc = mark.mark_wc(vectors[5],request[5])
    furniture = mark.mark_furniture(vectors[6], request[6])
    juridical = mark.mark_juridical(vectors[7], request[7])
    view = mark.mark_view(vectors[8], request[8])
    floor = mark.mark_floor(vectors[9], request[9])
    hot = mark.mark_juridical(vectors[10], request[10])
    vector_score = [demand, price, area, location, room, wc, furniture,juridical, view, floor, hot]
    return vector_score
