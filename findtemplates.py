import csv
import re

def printNoMatches(inputFileName, templatesFile, inputColumn, printEveryMatch):

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
    for i in range(len(inputList)):
        if i % 1000 == 0:
            print(str(matches) + "/" + str(count))
        count += 1
        for j in range(len(regexExpressions)):
            if regexExpressions[j].match(inputList[i][inputColumn]):
                if (printEveryMatch):
                    print("Match", i, j)
                    if (i != j):
                        print("Match isn't exact index")
                matches += 1
                break

def selfMatchTemplateFile(templatesFile):
    # read
    try:
        with open(templatesFile, "r") as csvInput:
            templatesList = list(csv.DictReader(csvInput))
    except IOError:
        print("File not found: " + templatesFile)
        return 1

    regexExpressions = []
    for template in templatesList:
        regexExpressions.append(re.compile(template["Regex"]))

    matches = 0
    count = 0
    for i in range(len(templatesList)):
        count += 1
        if (regexExpressions[i].match(templatesList[i]["Text"])):
            matches += 1
            print(i, "Match", str(matches) + "/" + str(count))
        else:
            print(i, "No match", str(matches) + "/" + str(count))
            print(templatesList[i]["Text"], templatesList[i]["Regex"])

def selfMatchTemplateFileFindOverlappingTemplates(templatesFile):
    # read
    try:
        with open(templatesFile, "r") as csvInput:
            templatesList = list(csv.DictReader(csvInput))
    except IOError:
        print("File not found: " + templatesFile)
        return 1

    regexExpressions = []
    for template in templatesList:
        regexExpressions.append(re.compile(template["Regex"]))

    count = 0
    multipleIdentifiers = 0
    for i in range(len(templatesList)):
        duplicates = []

        for j in range(len(templatesList)):
            if (regexExpressions[i].match(templatesList[j]["Text"]) and templatesList[j]["Identifier"] != templatesList[i]["Identifier"] and templatesList[j]["Version No"] != templatesList[i]["Version No"]):
            # if (regexExpressions[i].match(templatesList[j]["Text"]) and templatesList[j]["Identifier"] != templatesList[i]["Identifier"]):
                duplicates.append(templatesList[j])

        if len(duplicates) < 0:
            print("No matches", templatesList[i])
        elif len(duplicates) > 1:
            count += 1
            print("Multiple matches", templatesList[i]["Identifier"], templatesList[i]["Version No"])
            takenIdentifiers = []
            for duplicate in duplicates:
                print("\t", duplicate["Identifier"], duplicate["Version No"], duplicate["Text"])
                identifierTaken = False
                for takenIdentifier in takenIdentifiers:
                    if takenIdentifier == duplicate["Identifier"]:
                       identifierTaken = True
                if not identifierTaken:
                    takenIdentifiers.append(duplicate["Identifier"])
            if len(takenIdentifiers) > 1:
                multipleIdentifiers += 1
            print()

    print("Overlapping items", count, multipleIdentifiers)


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

def dumpMatchedRows(inputFileName, templatesFile, outputFileName):

    # read input headers
    try:
        with open(inputFileName, "r") as csvInput:
            reader = csv.reader(csvInput)
            headers = next(reader)
    except IOError:
        print("File not found: " + inputFileName)
        return 1

    if ("RegexId" not in headers):
        headers.append("RegexId")

    if ("RegexVer" not in headers):
        headers.append("RegexVer")

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

            for i in range(len(regexExpressions)):
                if regexExpressions[i].match(row["CondText"]):
                    regexId = templatesList[i]["Identifier"]
                    regexVer = templatesList[i]["Version No"]
                    row["RegexId"] = regexId
                    row["RegexVer"] = regexVer
                    writer.writerow(row)
                    break

        print("Output: " + outputFileName)

def dumpMatchedRowsWhichOnlyMatchGreedyRegex(inputFileName, templatesFile, outputFileName):

    # read input headers
    try:
        with open(inputFileName, "r") as csvInput:
            reader = csv.reader(csvInput)
            headers = next(reader)
    except IOError:
        print("File not found: " + inputFileName)
        return 1

    if ("RegexId" not in headers):
        headers.append("RegexId")

    if ("RegexVer" not in headers):
        headers.append("RegexVer")

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

    greedyExpressions = []
    for template in templatesList:
        greedyExpressions.append(re.compile(template["Regex"]))

    converativeExpressions = []
    for template in templatesList:
        converativeExpressions.append(re.compile(template["Regex Conservative"]))

    # write
    with open(outputFileName, "w") as csvOutput:
        writer = csv.DictWriter(csvOutput, fieldnames=headers, quoting=csv.QUOTE_NONNUMERIC)

        writer.writeheader()

        count = 0
        for row in inputList:
            count += 1
            if count % 10000 == 0:
                print(count)

            for i in range(len(greedyExpressions)):
                greedyMatch = greedyExpressions[i].match(row["CondText"])
                conservativeMatch = converativeExpressions[i].match(row["CondText"])
                if greedyMatch and not conservativeMatch:
                    regexId = templatesList[i]["Identifier"]
                    regexVer = templatesList[i]["Version No"]
                    row["RegexId"] = regexId
                    row["RegexVer"] = regexVer
                    writer.writerow(row)
                    break

        print("Output: " + outputFileName)