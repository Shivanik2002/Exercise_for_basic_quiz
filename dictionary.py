# Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print("All keys and values are in dictionary form !",)
dictionary = dict(zip(keys,values))
print(dictionary)

#  Using a loop and update() method of a dictionary

new_dict = dict()
for i in range(len(keys)):
    new_dict.update({keys[i]:values[i]})
print(new_dict)    

# Merge two Python dictionaries into one
print("__________________________________________")

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)

# Other way
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

print("__________________________________________")

# Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])

print("__________________________________________")

# Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = dict.fromkeys(employees,defaults)
print(result)

# Individual data
print(result["Kelly"])

print("__________________________________________")

# Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]
# dict = {k: sample_dict[k] for k in keys}
# print(dict)

result = dict()
for k in keys:
    result.update({k: sample_dict[k]})
print(result)    

print("__________________________________________")

# Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(result)  

print("__________________________________________")

# Check if a value exists in a dictionary

sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print("200 present in a dict")

print("__________________________________________")
    
# Rename key of a dictionary    

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

print("__________________________________________")

# Get the key of a minimum value from the following dictionary

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict,key = sample_dict.get))

print("__________________________________________")

# Change value of a key in a nested dictionary

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict["emp3"]["salary"] = 8500
print(sample_dict)