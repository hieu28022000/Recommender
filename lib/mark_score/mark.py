from numpy import double
def mark_money(value_attr, request):
    money = 100000000
    result = request - int(value_attr)
    if(result>0 and result<money):
        return 4
    elif(result>money and result<money*2):
        return 3
    elif(result>money*2 and result<money*3):
        return 2
    elif (result > money*3 and result<money*4):
        return 1
    elif (result >-money and result < 0):
        return 10
    elif (result > -money and result < -money*2):
        return 9
    elif (result > -money*2 and result <-3*money):
        return 8
    elif (result > -money*3 and result < -money*4):
        return 7
    elif (result > -money*4 and result < -money*5):
        return 6
    else:
        return 0

def mark_floor(value_attr,request):
    floor = 0
    floor = request - value_attr
    if(floor==0):
        return 10
    elif(floor==1 or floor==-1):
        return 9
    elif (floor == 2 or floor == -2):
        return 8
    elif (floor == 3 or floor == -3):
        return 7
    elif (floor == 4 or floor == -4):
        return 6
    elif (floor == 5 or floor == -5):
        return 5
    else:
        return 0
def mark_view(value_attr, request):
    for j in range(len(request)):
        if(request[j]==value_attr):
            return double(10/len(request))
    return 0
def mark_area(value_attr, request):
    result = request - value_attr
    if(abs(result)<5):
        return 10
    elif(abs(result)<15):
        return 5
    else:
        return 0

print(mark_area(70, 80))
