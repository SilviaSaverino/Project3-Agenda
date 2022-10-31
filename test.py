import csv

file = open('prova.csv')

type(file)

csvreader = csv.reader(file)
print(file.read())
file.close()

