import time
import datetime
import os



def check_file(file_path):
    os.chdir(file_path)

    all_file = os.listdir()
    files = []
    for f in all_file:
        files.append(f)

    oct = 0
    lines = 0



    for i in range(0,len(files)):

        # address = 'D:\\SmartContracts\\Polygon\\BackUp\\ContractsSourceCode\\' + files[i]
        address = 'D:\\SmartContracts\\Polygon\\BackUp\\ContractsSourceCode\\' + files[i]

        result = get_FileCreateTime(address)
        if result[1] == '03' :
            oct += 1
            file = open(address,'r',encoding = 'utf-8')
            line = len(file.readlines())
            lines += line
            file.close()

        else :
            True
    print(oct)
    print(lines)

def get_FileCreateTime(filePath):

    t = os.path.getmtime(filePath)
    time = TimeStampToTime(t)
    month = time.replace('\n','').split('-')
    return month


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)


file_list = check_file('D:\\SmartContracts\\Polygon\\BackUp\\ContractsSourceCode')