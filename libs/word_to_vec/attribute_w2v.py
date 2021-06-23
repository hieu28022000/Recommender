class Attribute_w2v:

    def __init__(self):
        self.demand = None
        self.price = None
        self.area = None
        self.location = None
        self.bedroom = None
        self.wc = None
        self.furniture = None
        self.juridical = None
        self.view = None
        self.floor = None
        self.hot = None


    def get_demand(self, demand):
        if demand == '' or demand == 'None':
           self.demand = None
           return self.demand
        demand = demand.lower()
        if demand == "thuê":
            self.demand = 0
        elif demand == "mua":
            self.demand = 1
        return self.demand


    # Attribute 1
    # Price word to vector function return price with type is interger
    def get_price(self, price):
        if price == '' or price == 'None':
            self.price = None
            return self.price
        if len(price) != 0:
            self.price = int(price)
        return self.price


    # Attribute 2
    # Area word to vector function return area with type is float
    def get_area(self, area):
        if area == '' or area == 'None':
            self.area = None
            return self.area

        if len(area) != 0:
            self.area = float(area)
        return self.area

    # Attribute 3
    # Location word to vector function return location input on map
    def get_location(self, location_line, list_location, list_map):
        if location_line == '' or location_line == 'None':
            self.location = None
        location_line = location_line.lower()
        for location in list_location:
            if location == location_line:
                location_index = list_location.index(location)
                x_loc = list_map[location_index][0]
                y_loc = list_map[location_index][1]
                self.location = [x_loc, y_loc]
                return self.location
        return self.location


    # Attribute 4
    # Numbers of bedrooms word to vector function return num of bedroom with type is interger
    def get_num_of_bedroom(self, bedroom):
        if bedroom == '' or bedroom == 'None':
            self.bedroom = None
            return self.bedroom
        if bedroom in ["Shophouse", "Officetel", "Penthouse", "Studio", "Duplex"]:
            self.bedroom = 0
            return self.bedroom
        if len(bedroom) != 0:
            self.bedroom = int(bedroom)
        return self.bedroom


        # Attribute 5
        # Numbers of WC word to vector function return num of WC with type is interger
    def get_num_of_WC(self, wc):
        if wc == '' or wc == 'None':
            self.wc = None
            return self.wc
        if wc in ["Shophouse", "Officetel", "Penthouse", "Studio", "Duplex"]:
            self.wc = 0
            return self.wc
        if len(wc) != 0:
            self.wc = int(wc)
        return self.wc


    # Attribute 6
    # Furniture word to vector function return 0 if furniture is "Không", return 1 if furniture is "Có" and return 2 if furniture is "Full"
    def get_furniture(self, furniture):
        if furniture == '' or furniture == 'None':
            self.furniture = None

        furniture = furniture.lower()
        if furniture == "không":
            self.furniture = 0
        elif furniture == "có":
            self.furniture = 1
        elif furniture == "full":
            self.furniture = 2
        return self.furniture


        # Attribute 7
        # Juridical word to vector function return 0 if juridical is "Sổ hồng" and return 1 if juridical is "HDMB"
    def get_juridical(self, juridical):
        if juridical == '' or juridical == 'None':
            self.juridical = None

        juridical = juridical.lower()
        if juridical == "sổ hồng":
            self.juridical = 0
        elif juridical == "hdmb":
            self.juridical = 1
        return self.juridical


        # Attribute 8
        # View word to vector function return 0, 1, 2, 3, 4, -3, -2, -1 for "Đông, Đông Nam, Nam, Tây Nam, Tây, Tây Bắc, Bắc, Đông Bắc"
    def get_view(self, view):
        if view == '' or view == 'None':
            self.view = None
            return self.view
        view = view.lower()
        list_view = ["đông", "đông nam", "nam", "tây nam", "tây", "tây bắc", "bắc", "đông bắc"]
        for index in list_view:
            self.view = list_view.index(index)
            return self.view
        return self.view
        # Attribute 9
        # Floor word to vector function return floor with type is interger


    def get_floor(self, floor):
        if floor == '' or floor == 'None':
            self.floor = None
            return self.floor
        if len(floor) != 0:
            self.floor = float(floor)
        return self.floor

        # Attribute 10
        # Hot word to vector function return 1 if hot is true and if not return 0


    def get_hot(self, hot):
        if hot == '' or hot == 'None':
            self.floor = None
            return self.hot
        # hot_input = hot_input.lower()
        if hot == "True":
            self.hot = 1
        elif hot == "False":
            self.hot = 0
        return self.hot


