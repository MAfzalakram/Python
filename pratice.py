import json

obj = {
    "name" : "abc",
    "age" : 35
}
# Trying to open file for writing
try :
    with open("data.json", "w") as f:
        json.dump(obj,f,indent=4)
except: 
    print("There was an error loading file")

# Trying to open file for reading 
try:
    with open("data.json", "r") as f:
        data = json.load(f)
        print(data)
except:
    print("Unable to open the file")



