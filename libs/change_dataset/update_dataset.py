import __init__
import pandas as pd

class Change_dataset:


    @staticmethod
    # return posible of apartment duplicate
    def num_line_duplicate(line, df):
        i = 0
        for floor in df['Mã căn']:
            # print(floor)
            if (floor.find(line[11]) == 0):
                return i
            i += 1
        return -1


    @staticmethod
    # change apartment information in dataset
    def update_line(update_line, num_line, df):
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


    @staticmethod
    # add new apartment at the end of dataset
    def add_line(line, df):
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


    @staticmethod
    # write dataset apartment for file csv
    def write_line(df, datapath):
        return df.to_csv(datapath)


    @staticmethod
    # remove apartment form dataset
    def remove_line(num_line, df):
        if (num_line != -1):
            df = df[: num_line].append(df[num_line+1 :])
        return df


    # paremeters:
    # input is apartment information
    # df is dataframe of apartment
    # datapath is path of dataset
    @classmethod
    def update_dataset(cls, line, df, datapath, request):

        num_line = cls.num_line_duplicate(line, df)
        request = request.lower()
        if(request== 'update'):
            if (num_line == -1):
                df = cls.add_line(line, df)
            else:
                df = cls.update_line(line, num_line, df)
        elif(request=='remove'):
            df = cls.remove_line(num_line, df)
        elif(request=='add'):
            df = cls.add_line(line, df)
        cls.write_line(df, datapath)

