# Create a dictionary by extracting the keys from a given dictionary.

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)

print(res.keys())