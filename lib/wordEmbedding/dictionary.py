import separation
import pandas as pd

# load data
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

# add index to the object and removes duplicates
def indexing(obj):
    str2vec = {}
    i = 0
    for str in obj:
        str = str.lower()
        try:
            t = str2vec[str]
        except:
            str2vec[str] = i
            i += 1
    return str2vec

# create dictionary for address
def create_dict_address(vt):
    ward = []
    district = []
    for address in vt:
        temp = separation.separation_address(address)
        ward.append(temp[0])
        district.append(temp[1])

    return indexing(ward), indexing(district)

# create dictionary for nearby service
def create_dict_nearby_service(near_sw):
    place = []
    for str in near_sw:
        str = separation.separetion_nearby_service(str)
        place.append(str[0])

    return indexing((place))

# create dictionary
dict_ward, dict_district = create_dict_address(vt)
dict_bv = create_dict_nearby_service(gbv)
dict_th = create_dict_nearby_service(gth)
dict_lgd = indexing(lgd)
dict_view = indexing(view)
dict_hcc = indexing(hcc)
dict_tienich = indexing(ti)
dict_giayto = indexing(gt)
