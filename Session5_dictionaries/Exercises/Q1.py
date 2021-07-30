groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
    }

quantity = {"Baby Spinach": 1,"Hot Chocolate": 3,"Crackers": 2,"Bacon": 1,"Carrots": 4,"Oranges": 2}


for item in groceries:
    print(f'{quantity[item]} {item} @ ${groceries[item]} = {quantity[item]*groceries[item]:.2f}')

