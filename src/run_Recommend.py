import __init__
from src.source import Get_request, run_source, Load_dataset
from libs.dataset.update_dataset import update_dataset

map_path = './dataset/map.json'
dataset_Apartment = './dataset/Apartment.csv'
dataset_Service_floor = './dataset/Service_floor.csv'
cfg_path = './libs/config/basic.json'

request_input = Get_request()
print(request_input, '\n')

run_source(request_input, map_path, dataset_Apartment, cfg_path)


# line including attribute in dataset
# line = ['Thuê', '8000000', '67.2', 'thủ đức', '2', '2', 'Full', 'HDMB', 'Đông Bắc', '8.0', 'FALSE', 'C.08.06-4s linh đông']

# data = Load_dataset(dataset_Apartment)

# update_dataset(line, data, dataset_Apartment)
