import csv

def readFile():
    data = []

    with open('history_data.csv', newline='') as history_data:
        reader = csv.reader(history_data)
        for row in reader:
            data.append(row)

    data_sorted = sorted(data, key=lambda x: x[0])
    data_sorted = [el[:-1] for el in data_sorted]  # excluding price for now

    return data_sorted

def returnProportion(column, colValue):  # column is integer
    selected = [val for val in architectDetails if val[column] == colValue]
    count = len(list(filter(lambda x: x[4] == "Yes", selected)))  # ie the impos value is yes
    return count / len(selected)

architectDetails = readFile()
possibleValues = []
for column, col in enumerate(architectDetails):
    if column == 4: break
    allValues = set([item[column] for item in architectDetails])
    possibleValues.append(allValues)

proportions = []
howProminent = []
for column in range(4):
    prop = {colValue: round(returnProportion(column, colValue), 3) for colValue in possibleValues[column]}
    total = 0
    for value in prop.values():
        total += abs(0.5 - value)

    howProminent.append((column, round(total / len(prop), 3)))
    proportions.append(prop)

howProminent.sort(key=lambda x: x[1])

total = 0
for el in howProminent:
    total += el[1]
w = [round(el[1] / total, 3) for el in howProminent]

weightings = [0, 0, 0, 0]

for i, el in enumerate(howProminent):
    weightings[el[0]] = w[i]

def analyseArchitect(testData):
    total = 0
    for i in range(4):
        # print (proportions[i][testData[i]])
        total += weightings[i] * proportions[i][testData[i]]
    return total

testDataItems = []

howBad = 0
testDataItems = [['Architect A', 'Apprenticed under R. Penrose', 'Maze', 'Glass and Dreams', 'Deceptively Ordinary'], ['Architect B', 'Apprenticed under R. Penrose', 'Gateway', 'Silver and Dreams', 'Hastily Sketched'], ['Architect C', 'Apprenticed under M. Escher', 'Library', 'Glass and Silver', 'Obsessively Detailed'], ['Architect D', 'Apprenticed under P. Stamatin', 'Uncategorizable Thing', 'Steel and Nightmares', 'Deceptively Ordinary'], ['Architect E', 'Apprenticed under R. Penrose', 'Gateway', 'Glass and Dreams', 'Deceptively Ordinary'], ['Architect F', 'Self-Taught', 'Maze', 'Wood and Dreams', 'Deceptively Ordinary'], ['Architect G', 'Apprenticed under R. Penrose', 'Tower', 'Silver and Nightmares', 'Hastily Sketched'], ['Architect H', 'Apprenticed under M. Escher', 'Gateway', 'Steel and Wood', 'Deceptively Ordinary'], ['Architect I', 'Apprenticed under T. Geisel', 'Uncategorizable Thing', 'Silver and Glass', 'Hastily Sketched'], ['Architect J', 'Apprenticed under R. Penrose', 'Maze', 'Silver and Dreams', 'Obsessively Detailed'], ['Architect K', 'Apprenticed under P. Stamatin', 'Tower', 'Steel and Wood', 'Deceptively Ordinary'], ['Architect L', 'Apprenticed under M. Escher', 'Gateway', 'Steel and Dreams', 'Deceptively Ordinary'], ['Architect M', 'Apprenticed under T. Geisel', 'Mechanism', 'Silver and Glass', 'Hastily Sketched'], ['Architect N', 'Apprenticed under T. Geisel', 'Uncategorizable Thing', 'Silver and Dreams', 'Hastily Sketched'], ['Architect O', 'Self-Taught', 'Mechanism', 'Steel and Silver', 'Deceptively Ordinary']]
results = []

for testData in testDataItems:
    result = round(analyseArchitect(testData[1:]), 4)
    results.append((testData[0], result))

results.sort(key = lambda x : x[1], reverse=True)
print (results)
