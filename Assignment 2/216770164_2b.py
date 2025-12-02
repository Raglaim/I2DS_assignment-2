import csv
import math as m

sepalLengthCmSum1 = 0
sepalWidthCmSum1 = 0
petalLengthCmSum1 = 0
petalWidthCmSum1 = 0
sepalLengthCmSum2 = 0
sepalWidthCmSum2 = 0
petalLengthCmSum2 = 0
petalWidthCmSum2 = 0

with open('Iris.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    for line in csvFile:
        sepalLengthCmSum1 += float(line['SepalLengthCm'])
        sepalWidthCmSum1 += float(line['SepalWidthCm'])
        petalLengthCmSum1 += float(line['PetalLengthCm'])
        petalWidthCmSum1 += float(line['PetalWidthCm'])

sepalLengthCmSum1 = sepalLengthCmSum1 / 150
sepalWidthCmSum1 = sepalWidthCmSum1 / 150
petalLengthCmSum1 = petalLengthCmSum1 / 150
petalWidthCmSum1 = petalWidthCmSum1 / 150

with open('Iris.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    for line in csvFile:
        sepalLengthCmSum2 += (sepalLengthCmSum1 - float(line['SepalLengthCm'])) ** 2
        sepalWidthCmSum2 += (sepalWidthCmSum1 - float(line['SepalWidthCm'])) ** 2
        petalLengthCmSum2 += (petalLengthCmSum1 - float(line['PetalLengthCm'])) ** 2
        petalWidthCmSum2 += (petalWidthCmSum1 - float(line['PetalWidthCm'])) ** 2

print(m.sqrt(sepalLengthCmSum2 / 149))
print(m.sqrt(sepalWidthCmSum2 / 149))
print(m.sqrt(petalLengthCmSum2 / 149))
print(m.sqrt(petalWidthCmSum2 / 149))
