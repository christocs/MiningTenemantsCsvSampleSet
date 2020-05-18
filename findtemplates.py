import csv
import re

def printNoMatches(inputFileName, templatesFile):

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

def dumpUnmatchedRows(inputFileName, templatesFile, outputFileName):

    # read input headers
    try:
        with open(inputFileName, "r") as csvInput:
            reader = csv.reader(csvInput)
            headers = next(reader)
    except IOError:
        print("File not found: " + inputFileName)
        return 1

    # read input contents
    try:
        with open(inputFileName, "r") as csvInput:
            inputList = list(csv.DictReader(csvInput))
    except IOError:
        print("File not found: " + inputFileName)
        return 1

    # read templates
    try:
        with open(templatesFile, "r") as csvInput:
            templatesList = list(csv.DictReader(csvInput))
    except IOError:
        print("File not found: " + inputFileName)
        return 1

    regexExpressions = []
    for template in templatesList:
        regexExpressions.append(re.compile(template["Regex"]))

    # write
    with open(outputFileName, "w") as csvOutput:
        writer = csv.DictWriter(csvOutput, fieldnames=headers, quoting=csv.QUOTE_NONNUMERIC)

        writer.writeheader()

        count = 0
        for row in inputList:
            count += 1
            if count % 10000 == 0:
                print(count)
            matchFound = False
            for regex in regexExpressions:
                if regex.match(row["CondText"]):
                    matchFound = True
                    break

            if not matchFound:
                writer.writerow(row)

        print("Output: " + outputFileName)
