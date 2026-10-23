import json
import os

from dotenv import load_dotenv

first_name = "Test"
last_name = "Last name"
years = 20
float_test = 20.3
abscense_of_value = None
bolean = False

range(10)  # Represents an immutable sequence of numbers

# f-strings (formatted string literals)
print(f"Hi, my name is {first_name} {last_name} and I'm {years} old")

# list
list_test = [1, 2, 3, 4]
list_test[5] = "Test"
print(len(list_test))

# dictionaries = same as objects in js with key values pairs
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}
print(thisdict["brand"])

# basic error handling
try:
    file = open("data.txt", "r")
    content = file.read()
except ValueError as e:
    print(f"Invalid input recorded: {e}")
else:
    print("File read successfully!")
    print(content)
finally:
    print("Cleaning up resources...")
    # This block executes even if the code crashes or succeeds


# JSON
# 1. Parse JSON string to a Python Dict (Deserialization)
json_string = '{"name": "Alice", "age": 30, "is_student": false}'
data = json.load(json_string)
print(data["test"])  # Data type is now a dictionarie


food_ratings = {"organic dog food": 2, "human food": 10}
json.dumps(food_ratings)

# Reading and writing
# The most efficent and safest way to do this is using with as context manager, it is higly recommended because it closes the file after the block finish
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # Outputs: ['Line 1\n', 'Line 2\n']

# Open the JSON file in read mode ('r')
with open("data.json", "r") as file:
    # Load the JSON data into a Python variable (usually a dictionary or list)
    data = json.load(file)

user_profile = {
    "name": "Alice Smith",
    "age": 30,
    "skills": ["Python", "Data Analysis"],
    "is_active": True,
}

# Open a file in write mode ('w')
with open("output.json", "w") as file:
    # Save the dictionary as a JSON file with nice formatting (4-space indentation)
    json.dump(user_profile, file, indent=4)

# Envs
load_dotenv()
api_key = os.environ.get("API_KEY")

# Pip and Environments
# By default, running pip install installs packages globally across your entire computer. If Project A needs Django 3.0 and Project B needs Django 5.0, a global install will break one of them.
# To fix this, always create an isolated virtual environment for each project before using pip
# python3 -m venv folder_name => source folder/bin/activate => pip install
# The requirements.txt is the same as package.json

# UV
# uv is an extremely fast, modern Python package and project manager
# uv is designed to be a single, all-in-one replacement for pip, pip-tools, virtualenv, and pyenv.
