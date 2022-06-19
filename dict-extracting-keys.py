# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.


# Dictionary comprehension
sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]
newDict = {k: sampleDict[k] for k in keys}
print(newDict)

# update() method and loop
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to extract
keys = ["name", "salary"]

# new dict
res = dict()

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)