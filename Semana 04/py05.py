
student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(student)
print(student['name'])
print(student['courses'])
print(student['age'])

student = {1: 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(student[1])

#student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
#print(student['phone'])

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(student.get('name'))

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(student.get('phone'))

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(student.get('phone', 'Not Found'))

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student)

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(student)

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
del student['age']
print(student)

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
age = student.pop('age')
print(student)
print(age)

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
for key in student:
    print(key)

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
for key, value in student.items():
    print(key, value)