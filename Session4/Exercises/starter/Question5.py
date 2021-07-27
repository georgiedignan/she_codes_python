import csv

max_v = 0
min_v = float('inf')
planet_max = ''
planet_min = ''

with open("galaxies.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for i,line in enumerate(csv_reader):
        if i != 0:
            # print(type(line[1]))
            if int(line[1]) > max_v:
               max_v = int(line[1])
               planet_max = line[0]
            if int(line[1]) < min_v:
               min_v = int(line[1])
               planet_min = line[0]
            
    print(f"Galaxy {planet_min} has the min velocity of {min_v}km/s.")
    print(f"Galaxy {planet_max} has the max velocity of {max_v}km/s.")
    



# numbers = ['a','b','c']
# print(numbers.index('a'))
