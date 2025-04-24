my_dict = {}
my_dict = {
             "name": "Aalim",
             "age": 13,
             "grade": 8,
             "course": "Coding"
}
print(my_dict['name'])
print(my_dict.get('age'))
my_dict['age'] = 13
print(my_dict)
my_dict['address'] = 'Downtown'
print(my_dict)
my_dict.pop('age')
print(my_dict)
print(f"Address : {my_dict.get('address')}")
my_dict.clear()
print(my_dict)