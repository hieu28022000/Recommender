import pandas as pd
from lib.mark_score import  mark
from lib.string_to_vec import w2v, dictionary

# request = ["Thuê", 2100000000, 72.36, "Bình Dương", 2, 2, "Có", "Sổ hồng", "Tây", 7]

#return to normalized vectors
# def normalize_request(request, path):
#     data = pd.read_csv(path)
#     request = w2v.Convert_obj2vector(request, data)
#     return request
#get and return a list of vectors from file csv
# def get_data_from_csv(path):
#     data = pd.read_csv(path)
#     demand = data['Nhu cầu']
#     address= data['Địa chỉ']
#     total_money = data['Tổng tiền']
#     area = data['Diện tích']
#     floor = data['Tầng']
#     views = data['View']
#     room = data['Phòng ngủ']
#     WC = data['Phòng vệ sinh']
#     furniture = data['Nội thất']
#     juridical = data['Pháp lý sở hữu']
#     hot = data['Hot']
#     attr = []
#     list_vectors = []
#     list_attr = []
#     for i in range(len(demand)):
#         attr = [demand[i], total_money[i], area[i], address[i], room[i], WC[i], furniture[i], juridical[i], views[i], floor[i], hot[i]]
#         list_attr.append(attr)
#     # normalizing data
#     for i in range(len(list_attr[0])):
#             list_vectors.append(w2v.Convert_obj2vector(list_attr[i],data))
#     return list_vectors
# return list of marked vectors
# return list of marked vectors
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
# l = list_mark_score(normalize_request(request, '../../dataset/Myhub_dataset.csv'), '../../dataset/Myhub_dataset.csv')
# print(l[:10])