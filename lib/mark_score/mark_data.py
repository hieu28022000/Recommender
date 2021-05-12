import pandas as pd
import mark
import distance

request = [3700000000, 30, ["Nam"]]
def get_data_from_csv():
    data = pd.read_csv('../../dataset/dataset.csv')
    id = data['STT']
    lgd = data['Loại giao dich']
    gtien = data['Giá tiền']
    vt = data['Vị trí']
    tang = data['Tầng']
    view = data['View']
    hcc = data['Hướng cửa chính']
    spn = data['Số phòng ngủ']
    swc = data['Số WC']
    nt = data['Nội thất']
    ti = data['Tiện ích']
    gt = ['Giấy tờ']
    gbv = data['Gần bệnh viện']
    gth = data['Gần trường học']
    return [id,lgd,gtien,vt,tang,view, hcc, spn, swc, nt, ti, gt,gbv,gth]
def get_ranking(gtien, tang, hcc):
    money = mark.mark_money(gtien, request[0])
    floor = mark.mark_floor(tang, request[1])
    direction = mark.mark_direction(hcc, request[2])
    temp = []
    # create a list of distance vectors
    for i in range(len(money)):
        temp.append([money[i], floor[i], direction[i]])
    # create dictionary of vectors to get index
    dic = {}
    for i in range(len(money)):
        dic[i] = distance.caculate_distance(temp[i])
    result = sorted(dic.items(), key=lambda x: x[1])
    return result
if __name__== '__main__':
    get_data = get_data_from_csv()
    rank = get_ranking(get_data[2],get_data[4], get_data[6])
    print(rank[-5:])












