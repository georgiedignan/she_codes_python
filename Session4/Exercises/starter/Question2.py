import csv

with open("colours_20_simple.csv",mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
    #print(csv_reader)
    for i,line in enumerate(csv_reader):
        if i != 0:
            print(f"{line[2]} {line[1]} {line[1]}")
 
