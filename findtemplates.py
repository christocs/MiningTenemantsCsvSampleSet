import csv
import re

def printMatches(inputFileName, templatesFile):

    # read contents
    try:
        with open(inputFileName, "r") as csvInput:
            inputList = list(csv.DictReader(csvInput))
    except IOError:
        print("File not found: " + inputFileName)
        return 1

    # read
    try:
        with open(templatesFile, "r") as csvInput:
            templatesList = list(csv.DictReader(csvInput))
    except IOError:
        print("File not found: " + inputFileName)
        return 1

    regexExpressions = []
    for template in templatesList:
        regexExpressions.append(re.compile(template["Regex"]))

    matches = 0
    count = 0
    for input in inputList:
        print(matches, "/", count)
        count += 1
        for regex in regexExpressions:
            if regex.match(input["CondText"]):
                matches += 1
                break
