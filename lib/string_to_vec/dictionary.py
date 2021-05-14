import pandas as pd

# load data
data = pd.read_csv('../../dataset/Myhub_dataset.csv')
address = data['Địa chỉ']

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

# create dictionary
dict_address = indexing(address)
dict_furniture = indexing(furniture)
dict_juridical = indexing(juridical)
