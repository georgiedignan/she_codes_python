#Question 1

# def conv(temp_in_f):
#     return (temp_in_f-32)*5/9

# print(conv(32))
# print(conv(0))
# print(conv(50))

#Question 2

# def even_or_odd(num):
#     if num%2 == 0:
#         return False
#     else:
#         return True

# print(even_or_odd(2))
# print(even_or_odd(7))
# print(even_or_odd(-1))

#Question 3
#need to download numpy to use np.mean

# def func(numbers):
#     count = 0
#     for i in numbers:
#         count +=1
#     return sum(numbers)/count

# print(func([4,3,2,6]))
# print(func([10,5,6]))

#Question 4

def cost(price,num):
    return f"${price*num}"

print(cost(4.25,3))
print(cost(3.79,1))
print(cost(1.49,7))
