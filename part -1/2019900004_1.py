import re
import itertools as itr
import sys

transactioncount = 0
numberOfDbElements = 0
numberOfActions = 0
readLinesData = []
transactionsData = []
elements = {}
data = {}
secondaryData = {}
outputFile = open("2019900004_1.txt", "w+")


def readInputData(inputFile):
    with open(inputFile, 'r') as fileData:
        for ele in fileData:
            ele = re.sub(':=', '=', ele)
            ele = re.sub(" ?(=|,|\\(|\\)|\\+|\\*|\\-|/) ?", " \\1 ", ele)
            ele = re.sub(' +', ' ', ele)
            ele = ele.strip("\n").strip(" ")
            readLinesData.append(ele)

def configureActions(numberOfActions):
    for k, group in itr.groupby(readLinesData, lambda numberOfActions: numberOfActions == ''):
        if k == False:
            transactionsData.append(list(group))
    pass

def configureDbElements():
    numberOfDbElements = transactionsData[0][0].split(" ")
    for i in range(0, len(numberOfDbElements), 2):
        secondaryData[numberOfDbElements[i]] = int(numberOfDbElements[i + 1])
    numberOfDbElements = len(secondaryData)
    pass


def printData():
    sortData = sorted(data)
    sortSecondaryData = sorted(secondaryData)
    dataSize = len(sortData)
    secondaryDataSize = len(sortSecondaryData)
    # print(dataSize)
    # print(secondaryDataSize)

    for i in range(dataSize):
        if i == dataSize - 1:
            outputFile.write(sortData[i] + ' ')
            outputFile.write(str(data[sortData[i]]) + ' ')

        else:
            outputFile.write(sortData[i] + ' ')
            outputFile.write(str(data[sortData[i]]) + ' ')
    outputFile.write('\n')

    for i in range(secondaryDataSize):
        if i == secondaryDataSize - 1:
            outputFile.write(sortSecondaryData[i] + ' ')
            outputFile.write(str(secondaryData[sortSecondaryData[i]]) + ' ')
        else:
            outputFile.write(sortSecondaryData[i] + ' ')
            outputFile.write(str(secondaryData[sortSecondaryData[i]]) + ' ')
    outputFile.write('\n')
    pass


def configureProcessData(ins, trans):
    if ins[0].lower() == 'read':
        el = ins[2]
        var = ins[4]
        if el not in data:
            data[el] = secondaryData[el]
        elements[var] = data[el]
    elif ins[0].lower() == 'write':
        el = ins[2]
        var = ins[4]
        outputFile.write("<" + trans + ", " + el + ", " + str(data[el]) + ">")
        outputFile.write('\n')

        data[el] = elements[var]
        printData()
    elif ins[0].lower() == 'output':
        el = ins[2]
        secondaryData[el] = data[el]
    else:
        var1 = ins[0]
        var2 = ins[2]
        oper = ins[3]
        val = int(ins[4])
        if oper == '+':
            elements[var1] = elements[var2] + val
        elif oper == '-':
            elements[var1] = elements[var2] - val
        elif oper == '*':
            elements[var1] = elements[var2] * val
        elif oper == '/':
            elements[var1] = elements[var2] / val

    pass


def updateData():
    comptrans = 1
    currtrans = 1

    completed_ins = [0 for i in range(transactioncount)]
    flagForCompletion = [False for i in range(transactioncount)]
    name = [None for i in range(transactioncount)]
    ins_count = [0 for i in range(transactioncount)]

    while (True):
        if comptrans == transactioncount:
            break
        if flagForCompletion[currtrans]:
            currtrans = ((currtrans + 1) % transactioncount)
            if currtrans == 0:
                currtrans = 1
            continue
        if completed_ins[currtrans] == 0:
            line = transactionsData[currtrans][0].split(" ")
            name[currtrans] = line[0]
            ins_count[currtrans] = int(line[1])
            outputFile.write('<START ' + name[currtrans] + '>\n')
            printData()
            completed_ins[currtrans] += 1
        for i in range(numberOfActions):
            ins = transactionsData[currtrans][completed_ins[currtrans]]
            ins = ins.split(" ")
            configureProcessData(ins, name[currtrans])
            completed_ins[currtrans] += 1
            if completed_ins[currtrans] > ins_count[currtrans]:
                outputFile.write('<COMMIT ' + name[currtrans] + '>\n')
                printData()
                flagForCompletion[currtrans] = True
                comptrans += 1
                break
        currtrans = ((currtrans + 1) % transactioncount)
        if currtrans == 0:
            currtrans = 1
    pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(" Please run 201990004_2.py as ==>>>>   python 201990004_1.py <input_file> <actions_count> ")
        exit(1)

    readInputData(sys.argv[1])
    numberOfActions = int(sys.argv[2])
    configureActions(numberOfActions)
    transactioncount = len(transactionsData)
    configureDbElements()
    updateData()
    outputFile.close()

