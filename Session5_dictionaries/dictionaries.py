students = ['Angela','Gen','Bel']
# print(students[0])


students_dict = {'Angela':1,"Gen":2,"Bel": 3}

#Values don't need to be unique, can be any data type
#Keys need to be unique, keys can only be immutable
#Dictionaries are unordered

# students_dict['Asli'] = 4
# print(students_dict)

# students_dict['Gen'] = 10
# print(students_dict)

# del students_dict['Asli']
# print(students_dict)

# print(students_dict.keys())
# print(students_dict.items())

# for key in students_dict:
#     print(key)

print(students_dict.get('Asli'))
print(students_dict('Asli',15))