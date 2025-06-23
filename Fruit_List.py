fruit_list = []
with open("fruit_list.txt","r") as fp:
    fruits = fp.read()
    
fruit_list.append(fruits)
print(f"Cuurent Fruits availble {fruits} ")
fruit = input("Please enter a fruit name?")
fruit_list.append(fruit)

choice =  input("do you want to enter another fruit name? y/n")
while choice == 'y':
    fruit = input("Please enter a fruit name?")
    fruit_list.append(fruit)
    choice =  input("do you want to enter another fruit name? y/n")
with open("fruit_list.txt","a") as fp:
    for item in fruit_list:
        fp.write(f"{item}\n")
print(fruit_list)



