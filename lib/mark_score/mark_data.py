import pandas as pd
import mark
import distance
from operator import itemgetter, attrgetter
request = [3700000000,30]
data = pd.read_csv('dataset.csv')
id = data['STT']
lgd = data['Loại giao dich']
gtien = data['Giá tiền']
vt = data['Vị trí']
tang = data['Tầng']
view = data['View']
hcc = data['Hướng cửa chính']
spn = data['Số phòng ngủ']
swc = data['Số WC']
nt = data['Nội thất']
ti = data['Tiện ích']
gt = ['Giấy tờ']
gbv = data['Gần bệnh viện']
gth = data['Gần trường học']

#print(mark.mark_money(gtien,request[0]))
money = mark.mark_money(gtien,request[0])
floor = mark.mark_floor(tang,request[1])

temp = []
for i in range(len(money)):
    temp.append([money[i],floor[i]])
print(temp[0])
result_dis = distance.caculate_distance(temp)
dic_rank = {}
for i in range(len(money)):
    dic_rank[id[i]].append(result_dis[i])
sorted(dic_rank, key=itemgetter(1))






