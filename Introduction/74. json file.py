import json

with open('filling.py') as j:
    data = json.load(j)
print(data)

with open('new_filling.py', 'w') as j:
    json.dump(data,j,indent = 5, sort_keys=True)