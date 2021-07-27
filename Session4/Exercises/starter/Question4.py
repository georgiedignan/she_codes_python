import csv

english_name= []
red = 0
green = 0
blue = 0
yellow =0 

with open("colours_213.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for i,line in enumerate(csv_reader):
        if i != 0:
            english_name.append(line[4])
            if "red" in line[4]:
                red += 1
            if "green" in line[4]:
                green += 1
            if "blue" in line[4]:
                blue += 1
            elif "yellow" in line[4]:
                yellow +=1

    print(f"Red: {red}")
    print(f"Green: {green}")
    print(f"Blue: {blue}")
    print(f"Yellow: {yellow}")



    






# with open("colours_20.csv",mode="r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         colour_data.append(line)
#         print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")

# with open("colours_20.csv",mode="r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for i, line in enumerate(csv_reader):
#         if i != 0:
#             print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")
