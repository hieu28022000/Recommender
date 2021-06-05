import __init__
from libs.word_to_vec.attribute_w2v import Attribute_w2v

def object_w2v(list_attribute, list_location, list_map):
    w2v = Attribute_w2v()
    w2v.get_demand(list_attribute[0])
    w2v.get_price(list_attribute[1])
    w2v.get_area(list_attribute[2])
    # location = w2v.get_location()
    w2v.get_location(list_attribute[3],list_location, list_map)
    w2v.get_num_of_bedroom(list_attribute[4])
    w2v.get_num_of_WC(list_attribute[5])
    w2v.get_furniture(list_attribute[6])
    w2v.get_juridical(list_attribute[7])
    w2v.get_view(list_attribute[8])
    w2v.get_floor(list_attribute[9])
    w2v.get_hot(list_attribute[10])
    obj_vec = [w2v.demand,
               w2v.price,
               w2v.area,
               w2v.location,
               w2v.bedroom,
               w2v.wc,
               w2v.furniture,
               w2v.juridical,
               w2v.view,
               w2v.floor,
               w2v.hot]
    return obj_vec
