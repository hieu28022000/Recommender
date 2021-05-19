import __init__
from src.source import Get_request, run_source, Load_dataset, Get_line
from libs.distance.attribute_distance import location_distance

map_path = './dataset/map.json'
dataset_path = './dataset/Myhub_dataset.csv'
cfg_path = './libs/config/basic.json'
onoff_file_path = './src/on_off.txt'


request_input = Get_request()
print(request_input, '\n\n')
run_source(request_input, map_path, dataset_path, cfg_path)





