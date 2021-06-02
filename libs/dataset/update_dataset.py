import pandas as pd



def num_line_duplicate(line, df):
    i = 0
    for floor in df['Mã căn']:
        print(floor)
        if (floor.find(line[11]) == 0):
            return i
        i += 1
    return -1


def update_data(update_line, num_line, df):
    df['Nhu cầu'][num_line] = update_line[0]
    df['Tổng tiền'][num_line] = update_line[1]
    df['Diện tích'][num_line] = update_line[2]
    df['Địa chỉ'][num_line] = update_line[3]
    df['Phòng ngủ'][num_line] = update_line[4]
    df['Phòng vệ sinh'][num_line] = update_line[5]
    df['Nội thất'][num_line] = update_line[6]
    df['Pháp lý sở hữu'][num_line] = update_line[7]
    df['View'][num_line] = update_line[8]
    df['Tầng'][num_line] = update_line[9]
    df['Hot'][num_line] = update_line[10]

    return df


def add_data(line, df):
    new_line = {}
    new_line['Nhu cầu'] = line[0]
    new_line['Tổng tiền'] = line[1]
    new_line['Diện tích'] = line[2]
    new_line['Địa chỉ'] = line[3]
    new_line['Phòng ngủ'] = line[4]
    new_line['Phòng vệ sinh'] = line[5]
    new_line['Nội thất'] = line[6]
    new_line['Pháp lý sở hữu'] = line[7]
    new_line['View'] = line[8]
    new_line['Tầng'] = line[9]
    new_line['Hot'] = line[10]
    new_line['Mã căn'] = line[11]

    df = df.append(new_line, ignore_index = True)
    return df


def removed_line(df, num_line):
    df = df[: num_line].append(df[num_line +1 :])
    return df


def write_data(df, datapath):
    return df.to_csv(datapath)


def update_dataset(input, df, datapath):
    num_line = num_line_duplicate(input, df)
    print(num_line)
    if (num_line == -1):
        add_data(input, df)
    else:
        update_data(input, num_line, df)

    write_data(df, datapath)


 