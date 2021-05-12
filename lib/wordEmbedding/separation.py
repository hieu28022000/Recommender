
def shortten(add):
    words = ['xã', 'phường', 'thị trấn', 'quận', 'huyện', 'tỉnh', 'thành phố']
    for word in words:
        if add.find(word) != -1:
            add = add[len(word) + 1 :]
        if add.isnumeric():
            add = word + ' ' + add
    return add

def separation_address(address):
    address = address.lower()
    address = address.split(', ')
    for i in range(len(address)):
        address[i] = shortten(address[i])

    address = address[-2:]
    return address

def fix_str(str):
    kiso = '0123456789'
    i = str.find('cách')
    if (i == -1):
        for j in range(len(str)):
            if (kiso.find(str[j]) != -1):
                str = str[: j] + 'cách ' + str[j:]
                # print(str)
                break
    return str

def separetion_KC(str):
    str = str.lower()
    if (str.find('không có') == -1):
        str = fix_str(str)
        str = str.split(' cách ')
        str[1] = int(str[1][: -1])
    
        return str
    else:
        return [str, -1]

# print(separetion_KC('Bệnh viện Nhi Đồng 200m'.lower()))
# print(separation_address(('12 Nguyễn Tât Thành, phường Tân Phú, quận 4')))
