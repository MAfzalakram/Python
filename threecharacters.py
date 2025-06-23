def threecharacters(string):
    if len(string)> 6:
        new_string = string[:3] + string[-3:]
        return new_string
    else:
        print("String length is less than 6")
        return ""
    
print(threecharacters("Pakistan"))