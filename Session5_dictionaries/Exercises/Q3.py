names = ["Maddy", "Bel", "Elnaz", "Gia", "Izzy","Joy", "Katie", "Maddie", "Tash", "Nic","Rachael", "Bec", "Bec", "Tabitha", "Teagen","Viv", "Anna", "Catherine", "Catherine", "Debby","Gab", "Megan", "Michelle", "Nic", "Roxy","Samara", "Sasha", "Sophie", "Teagen", "Viv"]

# list_names = list(set(names))

names_dict = {}.fromkeys(names,0)

for name in names:
    names_dict[name] += 1

print(names_dict)