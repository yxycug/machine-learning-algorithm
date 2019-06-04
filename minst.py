
# coding: utf-8


def loadData(fileName,data_bin=0,label_bin=0):
    '''
    加载文件
    :param fileName:要加载的文件路径
    :param data_bin:data是否二值化
    :param label_bin:label是否二值化
    :return: 数据集和标签集
    '''
    print('start read file')
    #存放数据及标记
    dataArr = []; labelArr = []
    #读取文件
    fr = open(fileName)
    #遍历文件中的每一行
    for line in fr.readlines():          #获取当前行，并按“，”切割成字段放入列表中
        curLine = line.strip().split(',')
        if data_bin==0:
            dataArr.append([int(num) for num in curLine[1:]])
        if data_bin==1:
            dataArr.append([int(int(num) > 128) for num in curLine[1:]])
        if label_bin==0:
            labelArr.append(int(curLine[0])) 
        if label_bin==1:
            if int(curLine[0]) == 0: 
                labelArr.append(1)
            else:
                labelArr.append(0)
    return dataArr, labelArr
