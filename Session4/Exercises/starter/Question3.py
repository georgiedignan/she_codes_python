import csv

colour_data = []

# with open("colours_20.csv",mode="r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         colour_data.append(line)
#         print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")

with open("colours_20.csv",mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for i, line in enumerate(csv_reader):
        if i != 0:
            print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")
