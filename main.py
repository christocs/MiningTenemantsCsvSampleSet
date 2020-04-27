import random
import csv
import os

rawInputsFileName = "input/Conditions.csv"
outputFileName = "output/SampleSetConditions.csv"

noRowsToAdd = 1000
fieldnames = ['Tenid', 'CondType', 'CondNo', 'Seq', 'CondText', 'CategoryId']

def getNewRowAtRandom(allRows, existingRows, checkedText):
    randNum = random.randrange(len(allRows))
    randRow = allRows[randNum]

    # check same condition doesn't already exist
    exists = False
    for existingRow in existingRows:
        if existingRow['CondText'].strip().lower() == randRow['CondText'].strip().lower():
            exists = True
            del existingRow
            break
    if not exists:
        return randRow
    else:
        return getNewRowAtRandom(allRows, existingRows)

def getConditionTypesOfConditionText(allRows, testRow):
    types = []
    data = []
    for row in allRows:
        # print(simpText(testRow['CondText']), simpText(row['CondText']), simpText(testRow['CondText']) == simpText(row['CondText']))
        if simpText(testRow['CondText']) == simpText(row['CondText']):
            if (not row['CondType'] in types):
                types.append(row['CondType'])
                data.append(row)
            # del allRows[allRows.index(row)]
    # print(types)
    return data

def conditionTextMatches(text1, text2):
    return simpText(text1) == simpText(text2)

def simpText(text):
    return text.strip().lower()

def main():
    # load all raw data into memory
    try:
        with open(rawInputsFileName, "r") as csvInput:
            rawList = list(csv.DictReader(csvInput))
    except IOError:
        print("Raw input file not found at: " + rawInputsFileName)
        exit(1)

    a = {"foo": "bar", "bax": "tax"}

    checkedText = []
    for i in range(len(rawList)):
        if not simpText(rawList[i]['CondText']) in checkedText:
            types = getConditionTypesOfConditionText(rawList, rawList[i])
            checkedText.append(simpText(rawList[i]['CondText']))
            if len(types) > 1:
                print(i)
                print(types[0])
                print(types[1])

        if i % 100 == 0:
            print(i)
        del rawList[i]

if __name__ == '__main__':
    main()