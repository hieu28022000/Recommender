

# Attribute 0]
# Demand word to vector function return 0 if demand is "Thuê" and return 1 if demand is "Bán" and if not return None
def demand_w2v(demand_input):
    if demand_input == '' or demand_input == 'None':
        return None

    demand_input = demand_input.lower()
    if demand_input == "thuê":
        return 0
    elif demand_input == "bán":
        return 1
    return None

# Attribute 1
# Price word to vector function return price with type is interger
def price_w2v(price_input):
    if price_input == '' or price_input == 'None':
        return None

    if len(price_input) != 0:
        price_input = int(price_input)
        return price_input
    return None

# Attribute 2
# Area word to vector function return area with type is float
def area_w2v(area_input):
    if area_input == '' or area_input == 'None':
        return None

    if len(area_input) !=0:
        area_input = float(area_input)
        return area_input
    return None

# Attribute 3
# Location word to vector function return location input on map
def location_w2v(location_input, list_location,list_map):
    if location_input == '' or location_input == 'None':
        return None

    location_input = location_input.lower()
    for location in list_location:
        if location == location_input:
            location_index = list_location.index(location)
            x_loc = list_map[location_index][0]
            y_loc = list_map[location_index][1]
            map_location = [x_loc, y_loc]
            return map_location  
    return None

# Attribute 4
# Numbers of bedrooms word to vector function return num of bedroom with type is interger
def num_of_bedroom_w2v(no_bedroom_input):
    if no_bedroom_input == '' or no_bedroom_input == 'None':
        return None

    if no_bedroom_input in ["Shophouse", "Officetel", "Penthouse", "Studio", "Duplex"]:
        return 0
    if len(no_bedroom_input) != 0:
        no_bedroom_input = int(no_bedroom_input)
        return no_bedroom_input
    return None

# Attribute 5
# Numbers of WC word to vector function return num of WC with type is interger
def num_of_WC_w2v(no_WC_input):
    if no_WC_input == '' or no_WC_input == 'None':
        return None
        
    if no_WC_input in ["Shophouse", "Officetel", "Penthouse", "Studio", "Duplex"]:
        return 0
    if len(no_WC_input) != 0:
        no_WC_input = int(no_WC_input)
        return no_WC_input
    return None

# Attribute 6
# Furniture word to vector function return 0 if furniture is "Không", return 1 if furniture is "Có" and return 2 if furniture is "Full"
def furniture_w2v(furniture_input):
    if furniture_input == '' or furniture_input == 'None':
        return None

    furniture_input = furniture_input.lower()
    if furniture_input == "không":
        return 0
    elif furniture_input == "có":
        return 1
    elif furniture_input == "full":
        return 2
    return None

# Attribute 7
# Juridical word to vector function return 0 if juridical is "Sổ hồng" and return 1 if juridical is "HDMB"
def juridical_w2v(juridical_input):
    if juridical_input == '' or juridical_input == 'None':
        return None

    juridical_input = juridical_input.lower()
    if juridical_input == "sổ hồng":
        return 0
    elif juridical_input == "hdmb":
        return 1
    return None

# Attribute 8
# View word to vector function return 0, 1, 2, 3, 4, -3, -2, -1 for "Đông, Đông Nam, Nam, Tây Nam, Tây, Tây Bắc, Bắc, Đông Bắc"
def view_w2v(view_input):
    if view_input == '' or view_input == 'None':
        return None

    view_input = view_input.lower()
    list_view = ["đông", "đông nam", "nam", "tây nam", "tây", "tây bắc", "bắc", "đông bắc"]
    if view_input in list_view:
        return list_view.index(view_input)
    return None

# Attribute 9
# Floor word to vector function return floor with type is interger
def floor_w2v(floor_input):
    if floor_input == '' or floor_input == 'None':
        return None
    
    if len(floor_input) != 0:
        floor_input = int(float(floor_input))
        return floor_input
    return None

# Attribute 10
# Hot word to vector function return 1 if hot is true and if not return 0
def hot_w2v(hot_input):
    if hot_input == '' or hot_input == 'None':
        return None
        
    # hot_input = hot_input.lower()
    if hot_input == "True":
        return 1
    elif hot_input == "False":
        return 0
    return None