import numpy as np

# Attribute 0 
# Demand distance function return 0 if demand1 same demand2
def demand_distance(demand1, demand2):
    return demand1 - demand2

# Attribute 1
# Price distance function return distance of price1 and price 2
def price_distance(price1, price2):
    return price1 - price2

# Attribute 2
# Area distance function return distance of area1 and area2
def area_distance(area1, area2):
    return area1 - area2

# Attribute 3
# Location distance function return distance of location1 and location 2
def location_distance(location1, location2):
    loc1_1D = np.array((location1[0], location1[1]))
    loc2_1D = np.array((location2[0], location2[1]))
    loc_dist = np.linalg.norm(loc1_1D - loc2_1D) 
    return loc_dist

# Attribute 4
# Numbers of bedroom distance function return distance of num of bedrooms1 and num of bedrooms2
def num_of_bedroom_distance(no_bedroom1, no_bedroom2):
    return no_bedroom1 - no_bedroom2

# Attribute 5
# Numbers of WC distance function return distance of num of WC1 and num of WC2
def num_of_WC_distance(no_WC1, no_WC2):
    return no_WC1 - no_WC2

# Attribute 6
# Furniture distance function return distance of furniture1 and furniture2
def furniture_distance(furniture1, furniture2):
    return furniture1 - furniture2

# Attribute 7
# Juridical distance funtion return distance of juridical1 and juridical2
def juridical_distance(juridical1, juridical2):
    return juridical1 - juridical2

# Attribute 8
# View distance funtion return distance of view1 and view2 
def view_distance(view1, view2):
    view_dist = abs(view1) - abs(view2)
    return view_dist

# Attribute 9
# Floor distance funtion return distance of floor1 and floor2
def floor_distance(floor1, floor2):
    return floor1 - floor2

# Attribute 10
# Hot distance funtion return 0 if hot1 same hot2
def hot_distance(hot1, hot2):
    return hot1 - hot2
