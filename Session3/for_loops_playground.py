#LOOPS
#performing an action multiple times
#for loops, while loops
#for loops: when you know how many times to repeat a task
#while loops: when you don't  know how many times to repeat the action

#for loops: sequence, strings, lists, dictionaries

# for num in range(1,11):
#     print(num, "hello")


# chilli_wishlist = ["igloo","chicken","donut","toy","cardboard box"]

# for item in chilli_wishlist:
#     print(f"Chilli wants: {item}")

#Nested Loops

numbers = [
    [1,2,3],
    [4],
    [5,6]
]

for num in numbers:
    # print(num)
    for n in num:
        print(n)