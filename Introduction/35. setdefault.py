person = {
            {'name' : 'ali', 'family' : 'khalili' ,'age' : 16},
            {'name' : 'kian', 'family' : 'rokrok' ,'age' : 16},
            {'name' : 'shahbod', 'family' : 'delgoshaie' ,'age' : 15}
}

print(person.setdefault('city','tehran'))
print(person)

# answer =    {'name' : 'ali', 'family' : 'khalili' ,'age' : 16 , 'city' : 'tehran},
#             {'name' : 'kian', 'family' : 'rokrok' ,'age' : 16 , 'city' : 'tehran},
#             {'name' : 'shahbod', 'family' : 'delgoshaie' ,'age' : 15 , 'city' : 'tehran}