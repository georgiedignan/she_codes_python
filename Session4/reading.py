import csv

#mode="r" is a default value for this function
#mode="r" is read

georgie_said = []

with open("dog.txt", mode = 'r', encoding = "utf-8") as csv_file:
    #creates the reader object
    #delimiter is default to a comma
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        if line != []:
            georgie_said.append(line)
    print(georgie_said)

with open("georgie.csv,",mode='w',newline="") as csv_file:
    csv_writer = csv.writer(csv_file) #creates the writer object
    for item in georgie_said:
        csv_writer.writerow(item)
