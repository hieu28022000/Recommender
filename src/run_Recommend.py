import __init__
from src.source import Source
from libs.change_dataset.update_dataset import Change_dataset

class Run:


    MAP_PATH = './dataset/map.json'
    DATASET_APARTMENT = './dataset/Apartment.csv'
    DATASET_SERVICE_FLOOR = './dataset/Service_floor.csv'
    CFG_PATH = './libs/config/basic.json'


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
        self.demand = demand
        self.price = price
        self.area = area
        self.location = location
        self.bedroom = bedroom
        self.wc = wc
        self.furniture = furniture
        self.juridical = juridical
        self.view = view
        self.floor = floor
        self.hot = hot


    @staticmethod
    def get_ranking_data(request_input, map_path, dataset_path, cfg_path, number_rank):
        ranks = []
        index_data, data = Source.run_source(request_input, map_path, dataset_path, cfg_path, number_rank)
        for index in index_data:
            rank_data = Source(data[index][0],
                               data[index][1],
                               data[index][2],
                               data[index][3],
                               data[index][4],
                               data[index][5],
                               data[index][6],
                               data[index][7],
                               data[index][8],
                               data[index][9],
                               data[index][10])
            ranks.append(rank_data)
        return ranks


    @classmethod
    def run_recommend(cls):
        request_input = Source.get_request()
        ranks = cls.get_ranking_data(request_input, cls.MAP_PATH, cls.DATASET_APARTMENT, cls.CFG_PATH, 20)
        # print(ranks[0].demand)
        return ranks


if __name__=='__main__':
    Run.run_recommend()

# this is test for request API
# line = ['Thuê', '8000000', '67.2', 'thủ đức', '2', '2', 'Full', 'HDMB', 'Đông Bắc', '8.0', 'FALSE', 'C.08.06-4s linh đông']
#
# data = Source.load_dataset(dataset_Apartment)
#
# Change_dataset.update_dataset(line, data, dataset_Apartment, 'add')



