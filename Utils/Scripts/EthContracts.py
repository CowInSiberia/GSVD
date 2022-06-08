# -*- coding: utf8 -*-
# SmartContactSpider.py
import requests
from bs4 import BeautifulSoup
import traceback
import re
import os
import time
import datetime


def printtime():
    print(time.strftime("%Y-%m-%d %H:%M:%S:", time.localtime()), end=' ')
    return 0


def getsccodecore(eachLine):
    # 伪装成浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537'}

    failedTimes = 100
    while True:  # 在制定次数内一直循环，直到访问站点成功

        if (failedTimes <= 0):
            printtime()
            print("失败次数过多，请检查网络环境！")
            break

        failedTimes -= 1
        try:
            # 以下except都是用来捕获当requests请求出现异常时，
            # 通过捕获然后等待网络情况的变化，以此来保护程序的不间断运行
            printtime()
            print('正在连接的的网址链接是 ' + eachLine, end='')
            response = requests.get(eachLine, headers=headers, timeout=5)
            break

        except requests.exceptions.ConnectionError:
            printtime()
            print('ConnectionError！请等待3秒！')
            time.sleep(6)

        except requests.exceptions.ChunkedEncodingError:
            printtime()
            print('ChunkedEncodingError！请等待3秒！')
            time.sleep(3)

        except:
            printtime()
            print('Unfortunitely,出现未知错误！请等待3秒！')
            time.sleep(3)

    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")

    targetPRE = soup.find_all('pre', 'js-sourcecopyarea editor')

    ContractFilePath = "D:\\SmartContracts\\Polygon\\ContractsSourceCode"


    filename = eachLine[31:73]

    if (os.path.exists(ContractFilePath + filename + '.sol')):
        printtime()
        print(filename + '已存在！')
        return 0

    fo = open(ContractFilePath + filename + '.sol', "w+", encoding="utf-8");
    fo.write(targetPRE[0].text)
    fo.close()
    printtime()
    print(filename + '新建完成！')

    return 0


def getsccode():
    ToCountPath = 'D:\\SmartContracts\\Polygon\\'

    f2 = open(ToCountPath + 'ToCount.txt')
    ToCount = int(f2.read())
    f2.close()
    print(ToCount)
    try:
        SCAddress = open("D:\\SmartContracts\\Polygon\\address.txt", "r")
        for eachLine in SCAddress:
            getsccodecore(eachLine)  # 这个才是获取智能合约代码的核心函数
            ToCount += 1
        os.remove(ToCountPath + 'ToCount.txt')


        f3 = open(ToCountPath + 'ToCount.txt', 'w')
        f3.write(str(ToCount))
        print(ToCount)

        SCAddress.close()
    except Exception as e:
        print(e)
        printtime()
        print('打开智能合约URL地址仓库错误！请检查文件目录是否正确！')


    return 0


def getSCAddress(eachurl, BasicInfoFilePath):
    # 伪装成某种浏览器，防止被服务器拒绝服务
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

    # 设置访问网址失败的最高次数，达到制定次数后，报告错误，停止程序
    failedTimes = 50

    while True:  # 一直循环，直到在制定的次数内访问站点成功

        if (failedTimes <= 0):
            printtime()
            print("失败次数过多，请检查网络环境！")
            break

        failedTimes -= 1  # 每执行一次就要减1
        try:
            # 以下except都是用来捕获当requests请求出现异常时，
            # 通过捕获然后等待网络情况的变化，以此来保护程序的不间断运行'https://etherscan.io/contractsVerified/1?filter=solc&ps=100'
            print('正在连接的的网址链接是 ' + eachurl)

            response = requests.get(url=eachurl, headers=headers, timeout=(3.05, 27))

            # 执行到这一句意味着成功访问，于是退出while循环
            break
        except requests.exceptions.ConnectionError:
            printtime()
            print('ConnectionError!请等待3秒！')
            time.sleep(6)

        except requests.exceptions.ChunkedEncodingError:
            printtime()
            print('ChunkedEncodingError!请等待3秒！')
            time.sleep(3)

        except:
            printtime()
            print('出现未知错误！请等待3秒！')
            time.sleep(3)

    # 转换成UTF-8编码
    response.encoding = response.apparent_encoding

    # 煲汤
    soup = BeautifulSoup(response.text, "html.parser")

    # 查找这个字段，这个字段下，包含智能合约代码的URL地址
    targetDiv = soup.find_all('div', 'table-responsive mb-2 mb-md-0')

    try:
        targetTBody = targetDiv[0].table.tbody
    except:
        printtime()
        print("targetTBody未成功获取！")
        return 1

    # 以追加的方式打开文件。
    # 如果文件不存在，则新建；如果文件已存在，则在文件指针末尾追加
    f0 = open(BasicInfoFilePath + "address.txt", "a")
    f1 = open(BasicInfoFilePath + 'MoreInfo.txt', "a")


    # 把每一个地址，都写到文件里面保存下来
    for targetTR in targetTBody:
        if targetTR.name == 'tr':
            # print(targetTR)
            # fo.write("https://etherscan.io" + targetTR.td.find('a', 'hash-tag text-truncate').attrs['href'] + "\n")
            f0.write("https://polygonscan.com" + targetTR.td.find('a', 'hash-tag text-truncate').attrs['href'] + "\n")
            # print(targetTR.td.find('a', 'hash-tag text-truncate').attrs['href'] + "\n")
            # print(len(targetTR))
            f1.write(targetTR.td.find('a', 'hash-tag text-truncate').attrs['href'] + "\n")








            



            #命名准则 How~~~~~
            # f1.write("CPolyD" + " " + "\n")
            # 命名准则 How~~~~~













            count = 0
            for td in targetTR:
                if count == 4:
                    # print(td.getText())
                    # 获得该合约当前余额
                    f1.write(td.getText() + "\n")
                if count == 5:
                    # print(td.getText())
                    # 获得该合约当前交易数
                    f1.write(td.getText() + "\n")
                count += 1

    f0.close()
    f1.close()
    return 0


def updatescurl():
    # urlList = ["https://etherscan.io/contractsVerified/1?ps=100",
    #            "https://etherscan.io/contractsVerified/2?ps=100",
    #            "https://etherscan.io/contractsVerified/3?ps=100",
    #            "https://etherscan.io/contractsVerified/4?ps=100",
    #            "https://etherscan.io/contractsVerified/5?ps=100"]

    urlList = ["https://polygonscan.com/contractsVerified/1?filter=solc&ps=100",
               "https://polygonscan.com/contractsVerified/2?filter=solc&ps=100",
               "https://polygonscan.com/contractsVerified/3?filter=solc&ps=100",
               "https://polygonscan.com/contractsVerified/4?filter=solc&ps=100",
               "https://polygonscan.com/contractsVerified/5?filter=solc&ps=100"]

    # urlList = ["https://polygonscan.com/contractsVerified?filter=solc"]

    # filepath是保存要爬取的智能合约地址的文件的存放路径
    # 请根据自己的需求改成自己想要的路径。
    BasicInfoFilePath = 'D:\\SmartContracts\\Polygon\\'


    # 把旧的存放合约地址的文件清除干净
    try:
        if (os.path.exists(BasicInfoFilePath + "address.txt")):
            os.remove(BasicInfoFilePath + "address.txt")
            printtime()
            print('已清除%s目录下的旧文件（仓库）！' % BasicInfoFilePath)
    except IOError:

        printtime()
        print("出现一个不能处理的错误，终止程序：IOError!")

        # 函数不正常执行，返回1
        return 1

    # 读取urlList里的每一个URL网页里的智能合约地址
    for eachurl in urlList:
        time = 0
        while (1 == getSCAddress(eachurl, BasicInfoFilePath)):
            time += 1
            if (time == 10):
                break
            pass

    # 函数正常执行，返回0
    return 0


def main():
    # 更新要爬取的智能合约的地址
    updatescurl()

    # 根据智能合约的地址去爬取智能合约的代码
    getsccode()


main()



















