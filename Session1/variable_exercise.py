#EXERCISE 1
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#print(int(num1)+int(num2))

#EXERCISE 2
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
print(num1 + ' * ' + num2 + ' =', int(num1)*int(num2)) 

#EXERCISE 3
#km = input("How many kilometrers? ")
#print(km + ' km' + ' =', int(km)*10**3, "m")
#print(km + ' km' + ' =', int(km)*10**5, "cm")






#EXERCISE 4
name = input("What is your name? ")

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        height = input("How tall are you? ")
    except ValueError:
        print("Sorry, please give height in cm.")
        #better try again... Return to the start of the loop
        continue
    else:
        #cm was successfully parsed!
        #we're ready to exit the loop.
        break
if int(height) <= 40: 
    print("Please give your height in cm")
else:
    print(f"{name} is {height}cm tall.")