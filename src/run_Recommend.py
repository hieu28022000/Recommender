import __init__
from src.source import Source
from libs.change_dataset.update_dataset import Change_dataset
from datetime import datetime


class Run:
    MAP_PATH = './dataset/map.json'
    DATASET_APARTMENT = './dataset/Apartment.csv'
    DATASET_SERVICE_FLOOR = './dataset/Service_floor.csv'
    CFG_PATH = './libs/config/basic.json'


    @staticmethod
    def get_ranking_data(request_input, map_path, dataset_path, cfg_path, number_rank):
        data = Source.load_source(request_input, map_path, dataset_path, cfg_path, number_rank)
        return data

    @classmethod
    def run_recommend(cls):
        result = []
        request_input = Source.get_request()
        ranks = cls.get_ranking_data(10, request_input, cls.MAP_PATH, cls.DATASET_APARTMENT, cls.CFG_PATH)
        for index in ranks:
            print(index.get_attr())
               #This is test for get all of attributes
        #      result.append(index.get_attr())
        #      #This is test for get demand attribute
        #      # result.append(index.demand)


if __name__=='__main__':
    start = datetime.now()
    Run.run_recommend()
    print(datetime.now()-start)

# this is test for request API
# line = ['Thuê', '8000000', '67.2', 'thủ đức', '2', '2', 'Full', 'HDMB', 'Đông Bắc', '8.0', 'FALSE', 'C.08.06-4s linh đông']
#
# data = Source.load_dataset(dataset_Apartment)
#
# Change_dataset.update_dataset(line, data, dataset_Apartment, 'add')



