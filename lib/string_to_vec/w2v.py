import dictionary

# single comversion
def str2vec(str, dict):
    str = str.lower()
    return dict[str]


# def nearby_service2vec(near, dict):
#     near = near.lower()
#     near = separation.separetion_KC(near)
#     return dict[near[0]], near[1]

# def view2vec(view, dict_view):
#     view = view.lower()
#     vec = '0.0.0.0.0'
#     flag = True
#     for i in range(len(dict_view)): 
#         if (flag):
#             for j in range(len(dict_view[i])):
#                 if (dict_view[i][j] in view):
#                     vec = vec[: i*2] + str(j) + vec[i*2 + 1 :]
#                     flag = False
#     return vec

# column conversion
def convert_att2vec(attribute, dict):
    int_att  = []
    for att in attribute:
        int_att.append(str2vec(att, dict))
    return int_att

# def convert_nearby_service2vec(service, dict):
    # near = []
    # for str in service:
    #     near.append(nearby_service2vec(str, dict))
    # return near

