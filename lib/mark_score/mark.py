def mark_money(s, request):
    mark = []
    money = 1000000000
    for i in range(len(s)):
        result = request - int(s[i])
        if(result>0 and result<money):
            mark.append(4)
        elif(result>money and result<money*2):
            mark.append(3)
        elif(result>money*2 and result<money*3):
            mark.append(2)
        elif (result > money*3 and result<money*4):
            mark.append(1)
        elif (result >-money and result < 0):
            mark.append(10)
        elif (result > -money and result < -money*2):
            mark.append(9)
        elif (result > -money*2 and result <-3*money):
            mark.append(8)
        elif (result > -money*3 and result < -money*4):
            mark.append(7)
        elif (result > -money*4 and result < -money*5):
            mark.append(6)
        else:
            mark.append(0)
    return mark

def mark_floor(s,request):
    mark = []
    floor = 0
    for i in range(len(s)):
        floor = request - s[i]
        if(floor==0):
            mark.append(10)
        elif(floor==1 and floor==-1):
            mark.append(9)
        elif (floor == 2 and floor == -2):
            mark.append(8)
        elif (floor == 3 and floor == -3):
            mark.append(7)
        elif (floor == 4 and floor == -4):
            mark.append(6)
        elif (floor == 5 and floor == -5):
            mark.append(5)
        else:
            mark.append(0)
    return mark

def mark_view(s, request):
    mark = []

