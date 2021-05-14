import dictionary

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

# Convert an object to vector
def Convert_obj2vector(line, dataset):
    cls = dataset['Nhu cầu']
    address = dataset['Địa chỉ']
    furniture = dataset['Nội thất']
    juridical = dataset['Pháp lý sở hữu']
    dict_cls = indexing(cls)
    dict_address = indexing(address)
    dict_furniture = indexing(furniture)
    dict_juridical = indexing(juridical)

    vector = [0,0,0,0,0,0,0,0,0,0,0]
    vector[0] = str2vec(line[0], dict_cls)
    vector[1] = int(line[1])
    vector[2] = float(line[2])
    vector[3] = str2vec(line[3], dict_address)
    vector[4] = int(line[4])
    vector[5] = int(line[5])
    vector[6] = str2vec(line[6], dict_furniture)
    vector[7] = str2vec(line[7], dict_juridical)
    vector[8] = line[8]
    vector[9] = int(line[9])
    return vector
