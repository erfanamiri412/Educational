person = {
    'name' : 'ali',
    'family' : 'ahmadi',
    'age' : 20
    }
print(person.keys())
print(person.values())
print(person.items())

# answer = dict_keys(['name', 'family', 'age'])
#          dict_values(['ali', 'ahmadi', 20])
#          dict_items([('name', 'ali'), ('family', 'ahmadi'), ('age', 20)])

person = {
    'name' : 'ali',
    'family' : 'ahmadi',
    'age' : 20
    }
for i in person:
    print(i)
print('..........................')
for i in person:
    print(person[i])

# answer = name
#          family
#          age
#          ..........................
#          ali
#          ahmadi
#          20

person = {
    'name' : 'ali',
    'family' : 'ahmadi',
    'age' : 20
    }
print(person['name'])
print(person['family'])
print(person['age'])

# answer = ali
#          ahmadi
#          20