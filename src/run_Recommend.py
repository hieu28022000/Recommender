import __init__
from src.source import Get_request, run_source, Load_dataset

map_path = './dataset/map.json'
dataset_Apartment = './dataset/Apartment.csv'
dataset_Service_floor = './dataset/Service_floor.csv'
cfg_path = './libs/config/basic.json'

print("Apartmen{0} or Service floor{1}: ")
service = int(input())

request_input = Get_request()
print(request_input, '\n\n')
if service == 0:
    run_source(request_input, map_path, dataset_Apartment, cfg_path)
else:
    run_source(request_input, map_path, dataset_Service_floor, cfg_path)






