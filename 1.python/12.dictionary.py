student = {'name': 'Johna', 'course': 'BBA'}

# print(student['name'])

#if the key does not exist 
# student['phone'] = 44444
# print(student.get('phone', 'Not found'))


#1. update the values 

# student.update({'name': 'Khan'})


#2. delete the value and key

# del student['name']
# print(student)


#3. show keys and values 

# print(student.keys())
# print(student.values())
# print(student.items())

#4. print all 

for key, value in student.items():

	print(key, value)


