import pandas as pd

import mark
import distance

request = [1800000000, 10, ["Tây Nam"],70.0]
def get_data_from_csv():
    data = pd.read_csv('../../dataset/Myhub_dataset.csv')
    dia_chi= data['Địa chỉ']
    tong_tien = data['Tổng tiền']
    dien_tich = data['Diện tích']
    tang = data['Tầng']
    views = data['View']
    return [dia_chi, tong_tien, dien_tich, tang, views]
def list_attr_vectors(request):
    data = get_data_from_csv()
    prices = []
    floors = []
    views = []
    areas = []
    for i in range(len(data[1])):
        prices.append(mark.mark_money(data[1][i],request[0]))
        floors.append(mark.mark_floor(data[3][i], request[1]))
        views.append(mark.mark_view(data[4][i], request[2]))
        areas.append(mark.mark_area(data[2][i], request[3]))
    return [prices, floors, views, areas]
result = list_attr_vectors(request)
print(result[3][:20])
















