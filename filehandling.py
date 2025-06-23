with open("mytext.txt", "w") as file:
    option = int(input("Enter a number?"))
    while(option != 0):
        file.write(str(option))
        option = int(input("Enter a number?"))

file.close()

