from schemadict import schemadict

# ok new changes gonne
# La aba yo Samir ko laptop bata change vayo

data = {
    "name":"Sagar Neupane",
    "age": 24,
    "is_student": True,
}

schema = schemadict(
    {
        'name':{
                'type': str,
                'min_len': 3,
                'max_len': 20,
                },
        'age': {
                'type': int,
                '>=': 0,
                '<': 10,
                },            
    })

print(schema.validate(data))