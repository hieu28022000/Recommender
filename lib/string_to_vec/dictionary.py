import pandas as pd

# load data
data = pd.read_csv('../../dataset/Myhub_dataset.csv')
address = data['Địa chỉ']
view = data['View']
hot = data['Hot']
bedroom = data['Phòng ngủ']
wc = data['Phòng vệ sinh']


furniture = ['không', 'có', 'full']
juridical = ['sổ hồng', 'hợp đồng mua bán', 'khác']


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

# create dictionary for nearby services
# def create_dict_nearby_service(near_sw):
#     place = []
#     for str in near_sw:
#         str = separation.separetion_nearby_service(str)
#         place.append(str[0])
#     return indexing((place))

# create dictionary
dict_address = indexing(address)
dict_furniture = indexing(furniture)
dict_juridical = indexing(juridical)


