import os
import csv

def getFilePaths(basePath):
    files = []

    with os.scandir(basePath) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.path)

    return files


def getSampleName(filePath: str):
    return filePath.split('/')[-1].split('_', 1)[0]


def getPeakAreasFromTsv(tsvFile):
    peakAreas = {}
    csvReader = csv.reader(tsvFile, delimiter='\t')

    areaRowIndex = -1
    i = 0

    for row in csvReader:
        if len(row) > 0 and row[0] == '[area]':
            areaRowIndex = i

        if areaRowIndex != -1 and i >= areaRowIndex + 2:
            if len(row) == 0:
                break
            print(row[0], ': ', row[-2])
            peakAreas[row[0]] = row[-2]

        i += 1
    
    return peakAreas


basePath = 'data/H3_04_15_27'
files = getFilePaths(basePath)

results = {}

for filePath in files:
    with open(filePath, 'r') as f:
        sampleName = getSampleName(filePath)
        results[sampleName] = getPeakAreasFromTsv(f)

print("RESULTS:\n-----\n", results)

# TODO: Standardise sample name lengths and sort samples
# TODO: Implement TSV Output layer