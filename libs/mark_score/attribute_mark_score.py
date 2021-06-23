import __init__
from distance.attribute_distance import Distance
from word_to_vec.attribute_w2v import Attribute_w2v

class Mark_score(Attribute_w2v):


    def __init__(self,
                 demand,
                 price,
                 area,
                 location,
                 bedroom,
                 wc,
                 furniture,
                 juridical,
                 view,
                 floor,
                 hot):
        self.demand_score = demand
        self.price_score = price
        self.area_score = area
        self.location_score = location
        self.bedroom_score = bedroom
        self.wc_score = wc
        self.furniture_score = furniture
        self.juridical_score = juridical
        self.view_score = view
        self.floor_score = floor
        self.hot_score = hot


    def get_data(self):
        return [self.demand_score,
                self.price_score,
                self.area_score,
                self.location_score,
                self.bedroom_score,
                self.wc_score,
                self.furniture_score,
                self.juridical_score,
                self.view_score,
                self.floor_score,
                self.hot_score]


    @staticmethod
    def demand_mark_score(data_demand, request_demand):
        if(data_demand == None) or (request_demand == None):
            return None
        demand_dist = Distance.demand_distance(data_demand, request_demand)
        if demand_dist == 0:
            return 10
        return 0


    @staticmethod
    def price_mark_score(data_price, request_price, demand):
        if (data_price == None) or (request_price == None) or (demand == None):
            return None

        if demand == 1:
            request_price -= request_price / 20
        if demand == 0:
            request_price -= request_price / 5
        dist = (data_price / request_price) - 1
        if dist >= 0:
            return 10 - dist
        return 0

    # Attribute 2
    # Area mark score function return score of data area
    @staticmethod
    def area_mark_score(data_area, request_area):
        if (data_area == None) or (request_area == None):
            return None

        area_dist = abs(Distance.area_distance(data_area, request_area))
        if area_dist <= 5:
            return 10
        elif area_dist <= 5:
            return 5
        return 0


    # Attribute 3
    # Location mark score function return score of data location
    @staticmethod
    def location_mark_score(data_location, request_location, list_location):
        if (data_location == None) or (request_location == None):
            return 0
        location_dist = Distance.location_distance(data_location, request_location)
        list_dist = []
        for location in list_location:
            list_dist.append(Distance.location_distance(location, request_location))
        max_dist = max(list_dist)
        location_dist = 10 - (location_dist / max_dist) * 10
        return location_dist


    # Attribute 4
    # Numbers of bedrooms mark score function return score of data num of bed
    @staticmethod
    def num_of_bedroom_mark_score(data_no_bedroom, request_no_bedroom):
        if (data_no_bedroom == None) or (request_no_bedroom == None):
            return None

        no_bed_dist = abs(Distance.num_of_bedroom_distance(data_no_bedroom, request_no_bedroom))
        # if no_bed_dist == 0:
        #     return 10
        # elif no_bed_dist == 1:
        #     return 5
        return no_bed_dist


    # Attribute 5
    # Numbers of WC mark score function return score of data num of WC
    @staticmethod
    def num_of_WC_mark_score(data_no_WC, request_no_WC):
        if (data_no_WC == None) or (request_no_WC == None):
            return None

        no_WC_dist = abs(Distance.num_of_WC_distance(data_no_WC, request_no_WC))
        # if no_WC_dist == 0:
        #     return 10
        # elif no_WC_dist == 1:
        #     return 5
        return no_WC_dist


    # Attribute 6
    # Furniture mark score function return score of data furniture
    @staticmethod
    def furniture_mark_score(data_furniture, request_furniture):
        if (data_furniture == None) or (request_furniture == None):
            return None

        furniture_dist = Distance.furniture_distance(data_furniture, request_furniture)
        if furniture_dist == 0:
            return 10
        elif furniture_dist == 1:
            return 5
        return 0


    # Attribute 7
    # Juridical mark score function return score of data juridical
    @staticmethod
    def juridical_mark_score(data_juridical, request_juridical):
        if (data_juridical == None) or (request_juridical == None):
            return None

        juridical_dist = Distance.juridical_distance(data_juridical, request_juridical)
        if juridical_dist == 0:
            return 10
        return 0


    # Attribute 8
    # View mark score function return score of data juridical
    @staticmethod
    def view_mark_score(data_view, request_view):
        if (data_view == None) or (request_view == None):
            return None

        view_dist = abs(Distance.view_distance(data_view, request_view))
        if view_dist == 0:
            return 10
        elif view_dist == 1:
            return 5
        return 0


    # Attribute 9
    # Floor mark score function return  score of data floor
    @staticmethod
    def floor_mark_score(data_floor, request_floor):
        if (data_floor == None) or (request_floor == None):
            return None
        floor_dist = abs(Distance.floor_distance(data_floor, request_floor))
        if floor_dist <= 1:
            return 10
        elif floor_dist <= 3:
            return 8
        elif floor_dist < 7:
            return 5
        return 0


    # Attribute 10
    # Hot mark score function return score of data hot
    @staticmethod
    def hot_mark_score(data_hot, request_hot):
        if (data_hot == None) or (request_hot == None):
            return None
        hot_dist = Distance.hot_distance(data_hot, request_hot)
        if hot_dist == 0:
            return 10
        return 0


    @classmethod
    def object_mark_score(cls, data_vector, request_vector, list_map):
        demand_score = cls.demand_mark_score(data_vector[0], request_vector[0])
        price_score = cls.price_mark_score(data_vector[1], request_vector[1], data_vector[0])
        area_score = cls.area_mark_score(data_vector[2], request_vector[2])
        location_score = cls.location_mark_score(data_vector[3], request_vector[3], list_map)
        num_of_bedroom_score = cls.num_of_bedroom_mark_score(data_vector[4], request_vector[4])
        num_of_WC_score = cls.num_of_WC_mark_score(data_vector[5], request_vector[5])
        furniture_score = cls.furniture_mark_score(data_vector[6], request_vector[6])
        juridical_score = cls.juridical_mark_score(data_vector[7], request_vector[7])
        view_score = cls.view_mark_score(data_vector[8], request_vector[8])
        floor_score = cls.floor_mark_score(data_vector[9], request_vector[9])
        hot_score = cls.hot_mark_score(data_vector[10], request_vector[10])
        return cls(demand_score,
                   price_score,
                   area_score,
                   location_score,
                   num_of_bedroom_score,
                   num_of_WC_score,
                   furniture_score,
                   juridical_score,
                   view_score,
                   floor_score,
                   hot_score)

