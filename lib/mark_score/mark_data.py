import pandas as pd
import mark
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from string_to_vec import w2v, dictionary

request = ["Thuê", 2100000000, 72.36, "Bình Dương", 2, 2, "Có", "Sổ hồng", "Tây", 7, True]

#return to normalized vectors
def normalize_request(request, path):
    data = pd.read_csv(path)
    request = w2v.Convert_obj2vector(request, data)
    return request
#get and return a list of vectors from file csv
def get_data_from_csv(path):
    data = pd.read_csv(path)
    demand = data['Nhu cầu']
    address= data['Địa chỉ']
    total_money = data['Tổng tiền']
    area = data['Diện tích']
    floor = data['Tầng']
    views = data['View']
    room = data['Phòng ngủ']
    WC = data['Phòng vệ sinh']
    furniture = data['Nội thất']
    juridical = data['Pháp lý sở hữu']
    hot = data['Hot']
    attr = []
    list_vectors = []
    list_attr = []
    for i in range(len(demand)):
        attr = [demand[i], total_money[i], area[i], address[i], room[i], WC[i], furniture[i], juridical[i], views[i], floor[i], hot[i]]
        list_attr.append(attr)
    # normalizing data
    for i in range(len(list_attr[0])):
            list_vectors.append(w2v.Convert_obj2vector(list_attr[i],data))
    return list_vectors
# return list of marked vectors
def list_mark_score(request, path):
    list_mark_data = []
    vectors = get_data_from_csv(path)
    for i in range(len(vectors)):
        price = mark.mark_money(vectors[i][1], request[1])
        area = mark.mark_area(vectors[i][2], request[2])
        location = mark.mark_area(vectors[i][3], request[3])
        room = mark.mark_room(vectors[i][4],request[4])
        wc = mark.mark_wc(vectors[i][5],request[5])
        furniture = mark.mark_furniture(vectors[i][6], request[6])
        juridical = mark.mark_juridical(vectors[i][7], request[7])
        view = mark.mark_view(vectors[i][8], request[8])
        floor = mark.mark_floor(vectors[i][9], request[9])
        hot = mark.mark_juridical(vectors[i][10], request[10])
        all_attr = [price, area, location, room, wc, furniture,juridical, view, floor, hot]
        list_mark_data.append(all_attr)
    return list_mark_data
# l = list_mark_score(normalize_request(request, '../../dataset/Myhub_dataset.csv'), '../../dataset/Myhub_dataset.csv')
# print(l[1:20])


