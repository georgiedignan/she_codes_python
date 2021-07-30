colour_counts = {"blue": 0,"green": 0,"yellow": 0,"red": 0,"purple": 0,"orange": 0,}

colours = ["purple","red","yellow","blue","purple","orange","blue","purple","orange","green"]

for colour in colours:
    colour_counts[colour] += 1

print(colour_counts)
