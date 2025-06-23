import json

DATA_FILE = "students.json"

def read_file():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
        print("Data has been added successfully")

def display_data():
    data = read_file()
    for roll, value in data.items():
        print(f"Roll: {roll}, name: {value['name']}, age:{value['age']}")

students = read_file()
roll = "Ab12"
students[roll] = {"name": "Afzal", "age" : 30, "class": 12}
save_data(students)
roll = "Ab13"
students[roll] = {"name": "Afzal", "age" : 30, "class": 12}
save_data(students)

display_data()

