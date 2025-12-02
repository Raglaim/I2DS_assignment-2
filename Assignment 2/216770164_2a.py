import csv

sepalLengthCmSum = 0
sepalWidthCmSum = 0
petalLengthCmSum = 0
petalWidthCmSum= 0

with open('Iris.csv', mode ='r') as file:
    csvFile = csv.DictReader(file)
    for line in csvFile:
        sepalLengthCmSum += float(line['SepalLengthCm'])
        sepalWidthCmSum += float(line['SepalWidthCm'])
        petalLengthCmSum += float(line['PetalLengthCm'])
        petalWidthCmSum += float(line['PetalWidthCm'])

print(sepalLengthCmSum / 150)
print(sepalWidthCmSum / 150)
print(petalLengthCmSum/150)
print(petalWidthCmSum / 150)


