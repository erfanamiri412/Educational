person = {
    'name' : 'ali',
    'family' : 'ahmadi',
    'age' : 20
    }
for key in person:
    print(key)
print('..........')

for key in person:
    print(person[key])
print('..........')

for key in person.keys():
    print(key)
print('..........')

for value in person.values():
    print(value)
print('..........')

for key, value in person.items():
    print(key, value)

# answer =  # name
            # family    
            # age       
            # ..........
            # ali       
            # ahmadi    
            # 20        
            # ..........
            # name      
            # family    
            # age       
            # ..........
            # ali       
            # ahmadi    
            # 20        
            # ..........
            # name ali
            # family ahmadi
            # age 20