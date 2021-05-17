from lib.string_to_vec.dictionary import *
# single comversion
def str2vec(str, dict):
    str = str.lower()
    return dict[str]

# column conversion
def convert_att2vec(attribute, dict):
    int_att  = []
    for att in attribute:
        int_att.append(str2vec(att, dict))
    return int_att

# convert number of room to vec
def num_room(room):
    if str(room).isnumeric():
        return room
    else:
        return 0

# Get line in dataset
def Get_line(num_line, dataset):
    line = dataset[num_line:num_line+1]
    line = line.values[0]
    return line

# index of location in dictionary
def Search_location(location):
    loc_dict =  open('./lib/config/location_dict.txt', encoding='utf8').read().split('\n')
    
    for index in range(len(loc_dict)):
        if location == loc_dict[index]:
            return index
    return 19


# Convert an object to vector
def Convert_obj2vector(line, dataset):
    if line[4] == 'Shophouse':
        line[4] = 0
        line[5] = 0
    cls = dataset['Nhu cầu']
    address = dataset['Địa chỉ']
    furniture = dataset['Nội thất']
    juridical = dataset['Pháp lý sở hữu']
    view = dataset['View']
    dict_cls = indexing(cls)
    dict_furniture = indexing(furniture)
    dict_juridical = indexing(juridical)
    dict_view = indexing(view)

    vector = [0,0,0,0,0,0,0,0,0,0,0]
    vector[0] = str2vec(line[0], dict_cls)
    vector[1] = int(line[1])
    vector[2] = float(line[2])
    vector[3] = Search_location(line[3])
    vector[4] = int(line[4])
    vector[5] = int(line[5])
    vector[6] = str2vec(line[6], dict_furniture)
    vector[7] = str2vec(line[7], dict_juridical)
    vector[8] = str2vec(line[8], dict_view)
    vector[9] = int(line[9])
    vector[10] = line[10]
    return vector
