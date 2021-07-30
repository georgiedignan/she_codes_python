groceries = {
    "Spinach": 2.78,
    "Hot Choc": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Orange": 3.08
}

# print(groceries)
# print(groceries["Spinach"])

# groceries["Avo"] = 1.00
# print(groceries)

# del groceries["Bacon"]

# print(groceries)

for item in groceries:
    print(f"{item}: ${groceries[item]}")

for item, price in groceries.items():
    print(f"{item}: ${price}")