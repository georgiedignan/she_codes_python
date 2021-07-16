#Ask the user to continually enter
#names until a blank string is entered

#Ask the user continually enter
#password until a password that you set
#has been given


#names = "georgie"
#names = input("What is your name: ")

# while names != "":
#     names = input("Please enter a name: ")
#     print("sorry wrong name")

password = input("Enter password: ")

while password != "password":
    password = input("Enter password: ")
    if password == "password":
        print("Correct password!")
    else:
        print("Incorrect password.")