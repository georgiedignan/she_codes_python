import csv


# with open("colours_20_simple.csv",mode="r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     #print(csv_reader)
#     headers = next(csv_reader)
#     for line in headers:
#         print(f"{line[0]} {line[1]} {line[2]}")


with open("colours_20_simple.csv",mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
    #print(csv_reader)
    for i,line in enumerate(csv_reader):
        if i != 0:
            print(f"{line[0]} {line[1]} {line[2]}")
