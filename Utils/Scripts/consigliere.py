import shutil

import pandas as pd
import os

# 遍历文件夹，读取所有合约名
def check_file(file_path):
    os.chdir(file_path)
    # print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    files = []
    for f in all_file:
        files.append(f)
    # return files
    a = 0
    for i in range(0,len(files)):
        # print(files[i])
        address = 'D:\\SmartContracts\\BSC\\ContractsSourceCode\\' + files[i]
        print(address)
        filename = open(address,'r',encoding = 'utf-8')
        MaxVersions = 4
        CompiledOrNotFlag = 0
        for line in filename:
            everyline = line.replace('\n', '').split(' ')
            # for a in everyline:

            for j in range(0, len(everyline)):
                try:
                    if everyline[j] == 'pragma' and everyline[j+1] == 'solidity':
                        CompiledOrNotFlag = 1
                        ContractVersions = 0
                        # print(everyline[j+2])
                        if everyline[j + 2][0] == '^':
                            # ContractVersions = everyline[j + 2][3:6]
                            ContractVersions = int(everyline[j + 2][3])
                            # print(MaxVersions)
                        elif everyline[j + 2][0] == '=':
                            # ContractVersions = everyline[j + 2][3:6]
                            ContractVersions = int(everyline[j + 2][3])
                            # print(ContractVersions)
                        elif everyline[j + 2][0] == '>' and everyline[j + 2][1] != '=':
                            # ContractVersions = everyline[j + 2][4:7]
                            ContractVersions = int(everyline[j + 2][3])
                            # print(ContractVersions)
                        elif everyline[j + 2][0] == '<' and everyline[j + 2][0] != '=':
                            # ContractVersions = everyline[j + 2][4:7]
                            ContractVersions = int(everyline[j + 2][3])
                            # print(ContractVersions)
                        elif everyline[j + 2][0] == '>' and everyline[j + 2][1] == '=':
                            # ContractVersions = everyline[j + 2][4:7]
                            ContractVersions = int(everyline[j + 2][4])
                            # print(ContractVersions)
                        elif everyline[j + 2][0] == '<' and everyline[j + 2][1] == '=':
                            # ContractVersions = everyline[j + 2][4:7]
                            ContractVersions = int(everyline[j + 2][4])
                            # print(ContractVersions)
                        elif everyline[j + 2][0] == '0':
                            # ContractVersions = everyline[j + 2][2:5]
                            ContractVersions = int(everyline[j + 2][2])
                            # print(ContractVersions)
                        if ContractVersions > MaxVersions:
                            MaxVersions = ContractVersions

                except IndexError:
                    pass
        filename.close()
        if CompiledOrNotFlag == 1:
            print(MaxVersions)
            if MaxVersions == 4:
                shutil.move(address,'D:\\SmartContracts\\BSC\VersionClassification_BSC\\4')
            if MaxVersions == 5:
                shutil.move(address,'D:\\SmartContracts\\BSC\VersionClassification_BSC\\5')
            if MaxVersions == 6:
                shutil.move(address,'D:\\SmartContracts\\BSC\VersionClassification_BSC\\6')
            if MaxVersions == 7:
                shutil.move(address,'D:\\SmartContracts\\BSC\VersionClassification_BSC\\7')
            if MaxVersions == 8:
                shutil.move(address,'D:\\SmartContracts\\BSC\VersionClassification_BSC\\8')
            if MaxVersions == 9:
                shutil.move(address,'D:\\SmartContracts\\BSC\VersionClassification_BSC\\8')
        if CompiledOrNotFlag == 0:
            print('--------------------------------------Warning!----------------------------------------')
            shutil.move(address,'D:\\SmartContracts\\BSC\\VersionClassification_BSC\\warning')


        # # 计数
        # a += 1
        # print(a)


file_list = check_file('D:\\SmartContracts\\BSC\\ContractsSourceCode')






#file.readline()
#file = open('D:\\EthContracts\\test.txt','r',encoding = 'utf-8')






# filename = open('D:\\EthContracts\\batch1\\0x00b17e5c7f4096ec7c67b05e41f77a724b927e62.sol','r',encoding = 'utf-8')
#
# for line in filename:
#
#     everyline = line.replace("\n", "").split(' ')
#     # for a in everyline:
#     for i in range(0, len(everyline)):
#         try:
#             if everyline[i][0] == '^':
#                 print(everyline[i][1:-1])
#         except IndexError:
#             pass
# filename.close()
