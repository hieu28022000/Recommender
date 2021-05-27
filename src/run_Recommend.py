import __init__
from src.source import Get_request, run_source, Load_dataset

map_path = './dataset/map.json'
dataset_Apartment = './dataset/Apartment.csv'
dataset_Service_floor = './dataset/Service_floor.csv'
cfg_path = './libs/config/basic.json'

request_input = Get_request()
print(request_input, '\n')

run_source(request_input, map_path, dataset_Apartment, cfg_path)






