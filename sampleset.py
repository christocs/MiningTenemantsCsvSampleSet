import random
import csv
import os

rawInputsFileName = "input/Conditions.csv"
outputFileName = "output/ConditionTextsWithMultipleCondTypes.csv"

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
        if simpText(testRow['CondText']) == simpText(row['CondText']):
            if (not row['CondType'] in types):
                types.append(row['CondType'])
                data.append(row)
    return data

def conditionTextMatches(text1, text2):
    return simpText(text1) == simpText(text2)

def simpText(text):
    return text.strip().lower()

def writeRow(writer, row):
    rowData = {}
    for fieldname in fieldnames:
        if fieldname == "CategoryId" and not "CategoryId" in row:
            rowData[fieldname] = 0
        else:
            rowData[fieldname] = row[fieldname]
    writer.writerow(rowData)

def generateSampleSet():
    # load all raw data into memory
    try:
        with open(rawInputsFileName, "r") as csvInput:
            rawList = list(csv.DictReader(csvInput))
    except IOError:
        print("Raw input file not found at: " + rawInputsFileName)
        exit(1)

    a = {"foo": "bar", "bax": "tax"}

    # make sure output directory exists
    if not os.path.exists('output'):
        os.makedirs('output')

    # write rows to file
    with open(outputFileName, "w") as csvOutput:
        writer = csv.DictWriter(csvOutput, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)

        writer.writeheader()

        checkedText = []
        for i in range(len(rawList)):
            if not simpText(rawList[i]['CondText']) in checkedText:
                types = getConditionTypesOfConditionText(rawList, rawList[i])
                checkedText.append(simpText(rawList[i]['CondText']))
                if len(types) > 1:
                    print(i)
                    print(types[0])
                    writeRow(writer, types[0])
                    print(types[1])
                    writeRow(writer, types[1])

            if i % 10000 == 0:
                print(i)
            del rawList[i]

    print("Sample set generated at: " + outputFileName)

if __name__ == '__main__':
    generateSampleSet()