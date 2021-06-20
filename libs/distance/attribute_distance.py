import numpy as np

class Distance:

    @staticmethod
    def demand_distance(demand1, demand2):
        return demand1 - demand2


    @staticmethod
    def price_distance(price1, price2):
        return price1 - price2


    @staticmethod
    def area_distance(area1, area2):
        return area1 - area2

    @staticmethod
    def location_distance(location1, location2):
        loc1_1D = np.array((location1[0], location1[1]))
        loc2_1D = np.array((location2[0], location2[1]))
        loc_dist = np.linalg.norm(loc1_1D - loc2_1D)
        return loc_dist

    @staticmethod
    def num_of_bedroom_distance(no_bedroom1, no_bedroom2):
        return no_bedroom1 - no_bedroom2

    @staticmethod
    def num_of_WC_distance(no_WC1, no_WC2):
        return no_WC1 - no_WC2


    @staticmethod
    def furniture_distance(furniture1, furniture2):
        return furniture1 - furniture2


    @staticmethod
    def juridical_distance(juridical1, juridical2):
        return juridical1 - juridical2

    @staticmethod
    def view_distance(view1, view2):
        view_dist = abs(view1) - abs(view2)
        return view_dist

    @staticmethod
    def floor_distance(floor1, floor2):
        return floor1 - floor2

    @staticmethod
    def hot_distance(hot1, hot2):
        return hot1 - hot2
