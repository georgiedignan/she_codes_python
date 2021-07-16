#Exerise 1

# number = input("Please guess any number: ")

# while number != "":
#     number = input("Please guess any number: ")

#Exercise 2
number = int(input("Please enter a number: "))
#using a for loop

# for num in range(1,number+1):
#     if num%2!=0:
#         print(num)

#try using a while loop
i=1

while (i<=number):
    if i%2 != 0:
        print(i)
    i+=1

# N = int(input("Enter a number: "))
# i = 1
# while(i <= N):
#     if (i % 2) == 0:
#         print('EVEN')
#     else:
#         print('ODD')

#     i += 1
#Exercise 3

# number = 43
# guess = int(input("Guess my number: "))

# if guess > number:
#     print("Guess is too high!")
# else:
#     print("Guess is too low!")

# while guess != number:
#     guess = int(input("Guess my number: "))
#     if guess > number:
#         print("Guess is too high!")
#     elif guess < number:
#         print("Guess is too low!")
#     else:
#         print("That is correct!")

