import json
file_name = 'numbers.json'
with open(file_name) as j_obj:
    numbers = json.load(j_obj)
print(numbers)
