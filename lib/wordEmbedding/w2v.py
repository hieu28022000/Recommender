import separation
import pandas as pd

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
gt = data['Giấy tờ']
gbv = data['Gần bệnh viện']
gth = data['Gần trường học']

def add_index(ward, district):
    ward2int = {}
    district2int = {}
    i = 0
    for w in ward:
        try:
            t = ward2int[w]
        except:
            ward2int[w] = i
            i += 1

    i = 0
    for d in district:
        try:
            t = district2int[d]
        except:
            district2int[d] = i
            i += 1
    return ward2int, district2int

def create_dict_address(vt):
    ward = []
    district = []
    for address in vt:
        temp = separation.separation_address(address)
        ward.append(temp[0])
        district.append(temp[1])

    return add_index(ward, district)

def indexing(obj):
    str2vec = {}
    i = 0
    for str in obj:
        try:
            t = str2vec[str]
        except:
            str2vec[str] = i
            i += 1
    return str2vec

def create_dict_KC(near_sw):
    place = []
    for str in near_sw:
        str = separation.separetion_KC(str)
        place.append(str[0])

    return indexing((place))


# dictionary
dict_ward, dict_district = create_dict_address(vt)
dict_bv = create_dict_KC(gbv)
dict_th = create_dict_KC(gth)
dict_lgd = indexing(lgd)
dict_view = indexing(view)
dict_hcc = indexing(hcc)
dict_tienich = indexing(ti)
dict_giayto = indexing(gt)

def address2vec(address):
    add = separation.separation_address(address)
    return ward[add[0]], district[add[1]]

def dis_to_service2vec(near, dict):
    near = separation.separetion_KC(near)
    return dict[near[0]], near[1]

def str2vec(str, dict):
    return dict[str]

# print(dict_hcc)
# print(dict_lgd)
# print(dis_to_service2vec('Bệnh viện chợ Rẫy cách 300m', dict_bv))