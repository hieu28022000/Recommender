import separation

# single comversion
def address2vec(address, dict_ward, dict_district):
    address = address.lower()
    add = separation.separation_address(address)
    return dict_ward[add[0]], dict_district[add[1]]

def nearby_service2vec(near, dict):
    near = near.lower()
    near = separation.separetion_KC(near)
    return dict[near[0]], near[1]

def str2vec(str, dict):
    str = str.lower()
    return dict[str]

# column conversion
def convert_vitri_2vec(vt):
    vitri = []
    for address in vt:
        vitri.append(address2vec(address))

    return  vitri

def convert_nearby_service2vec(service, dict):
    near = []
    for str in service:
        near.append(nearby_service2vec(str, dict))
    return near

def convert_att2vec(attribute, dict):
    int_att  = []
    for att in attribute:
        int_att.append(str2vec(att, dict))
    return int_att

