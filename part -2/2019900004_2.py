import re
import itertools as itr
import sys

readLinesData = []
dataBaseDir = {}
comptrans = []
outputFile = open("2019900004_2.txt", "w+")

def readInputData(inputFile):
    with open(inputFile, 'r') as fileData:
        for ele in fileData:
            ele = re.sub(" ?(,|\\(|\\)) ?", " \\1 ", ele)
            ele = re.sub(' +', ' ', ele)
            ele = ele.strip("\n").strip(" ").strip("<").strip(">")
            readLinesData.append(ele)
        #print(readLinesData)

def configureDbElements():
    allDatabaseElements = readLinesData[0].split(" ")
    #print(allDatabaseElements)
    for i in range(0, len(allDatabaseElements), 2):
        dataBaseDir[allDatabaseElements[i]] = int(allDatabaseElements[i + 1])
    pass

def printData():
    flag  = False
    readLinesData.reverse()
    readLinesData.pop()
    readLinesData.pop()
    for ele in readLinesData :
        data = ele.split(" ")
        if data[0].lower() == 'end':
            flag = True
        elif data[0].lower() == 'start' and data[1].lower() == 'ckpt':
            if flag == True:
                break
        else:
            if data[0].lower() == 'commit':
                comptrans.append(data[1])
            elif data[0].lower() != 'start':
                if data[0] not in comptrans:
                    index = data[2]
                    locValue = data[4]
                    dataBaseDir[index] = locValue

    sortData = sorted(dataBaseDir)
    dataElements = len(sortData)
    for i in range(dataElements):
        if i == dataElements - 1:
            outputFile.write(sortData[i]+' ')
            outputFile.write(str(dataBaseDir[sortData[i]]) + ' ')
        else:
            outputFile.write(sortData[i] + ' ')
            outputFile.write(str(dataBaseDir[sortData[i]]) + ' ')

    outputFile.write('\b\b\n ')
    print()



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(" Please run 201990004_2.py as python 201990004_2.py <logging_file> ")
        exit(1)

    readInputData(sys.argv[1])
    configureDbElements()
    printData()



