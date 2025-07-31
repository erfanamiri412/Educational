import json

myString = '''
{
    "people" : [
    {
        "name" : "taha",
        "family" : "sadeghi",
        "is_married" : "no",
        "vehicle" : "benz"
        },
        {        
        "name" : "parsa",
        "family" : "basafa",
        "is_married" : "yes",
        "vehicle" : "null" 
        }
    ]
}
'''
data = json.loads(myString)     # json string -> python dictionary : deserialization
print(data)

# answer = {'people': [{'name': 'taha', 'family': 'sadeghi', 'is_married': 'no', 'vehicle': 'benz'},
#                      {'name': 'parsa', 'family': 'basafa', 'is_married': 'yes', 'vehicle': 'null'}]}


newString = json.dumps(data)    # python dictionary -> json string : serialization
print(newString)

# answer = {"people": [{"name": "taha", "family": "sadeghi", "is_married": "no", "vehicle": "benz"},
#                      {"name": "parsa", "family": "basafa", "is_married": "yes", "vehicle": "null"}]}