import csv

dict = {}

with open("colours_20_simple.csv",encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next (csv_reader)
    for line in csv_reader:
        #add item to dict
        dict[line[1]] = line[2]

# print(dict)

#Q5

with open("colours_20_simple.csv",encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next (csv_reader)
    for line in csv_reader:
        dict[line[1]] =  [line[0],line[2]]


print(dict)