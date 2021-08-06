people = [
    ["Alic",25,"pink"],
    ["Bob",33,"purple"],
    ["Ann",18,"red"]
    ]

vaccine = []

for data in people:
    if data[1] > 20:
        vaccine.append(data[0])

print(vaccine)


vaccination = [] 

for data in people:
    for item in data:
        if item.is_integer() == True:
            if item >= 20:
                vaccination.append(item)