
courses = ['His', 'Mat', 'Fis','Comp']
print(courses)
print(len(courses))
print(courses[0])
print(courses[1])
print(courses[2])
print(courses[3])
print(courses[-1])
#print(courses[4])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses.append('Art')
print(courses)

courses = ['His', 'Mat', 'Fis','Comp']
courses.insert(0, 'Art')
print(courses)

courses = ['His', 'Mat', 'Fis','Comp']
courses_2 = ['Art', 'Edu']
courses.insert(0, courses_2)
print(courses)
print(courses[0])

courses = ['His', 'Mat', 'Fis','Comp']
courses_2 = ['Art', 'Edu']
courses.extend(courses_2)
print(courses)

courses = ['His', 'Mat', 'Fis','Comp']
courses_2 = ['Art', 'Edu']
courses.append(courses_2)
print(courses)

courses = ['His', 'Mat', 'Fis','Comp']
courses.remove('Mat')
print(courses)

courses = ['His', 'Mat', 'Fis','Comp']
courses.pop()
print(courses)

courses = ['His', 'Mat', 'Fis','Comp']
popped = courses.pop()
print(popped)
print(courses)

courses = ['His', 'Mat', 'Fis','Comp']
courses.reverse()
print(courses)

courses = ['His', 'Mat', 'Fis','Comp']
courses.sort()
print(courses)

courses = ['His', 'Mat', 'Fis','Comp']
nums = [1, 5, 2, 4, 3]
courses.sort()
nums.sort()
print(courses)
print(nums)

courses = ['His', 'Mat', 'Fis','Comp']
nums = [1, 5, 2, 4, 3]
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

courses = ['His', 'Mat', 'Fis','Comp']
nums = [1, 5, 2, 4, 3]
sorted(courses)
print(courses)

courses = ['His', 'Mat', 'Fis','Comp']
nums = [1, 5, 2, 4, 3]
sourted_courses =sorted(courses)
print(sourted_courses)

nums = [1, 5, 2, 4, 3]
print(min(nums))
print(max(nums))
print(sum(nums))

courses = ['His', 'Mat', 'Fis','Comp']
print(courses.index('Comp'))
#print(courses.index('Art'))
print('Art' in courses)
print('Mat' in courses)

courses = ['His', 'Mat', 'Fis','Comp']
for iten in courses:
    print(iten)

courses = ['His', 'Mat', 'Fis','Comp']
for course in courses:
    print(course)

courses = ['His', 'Mat', 'Fis','Comp']
for index, course in enumerate(courses):
    print(index, course)

courses = ['His', 'Mat', 'Fis','Comp']
for index, course in enumerate(courses, start=1):
    print(index, course)

courses = ['His', 'Mat', 'Fis','Comp']
course_str = ', '.join(courses)
print(course_str)

courses = ['His', 'Mat', 'Fis','Comp']
course_str = ' - '.join(courses)
print(course_str)

courses = ['His', 'Mat', 'Fis','Comp']
course_str = ' - '.join(courses)
new_list = course_str.split(' - ')
print(course_str)
print(new_list)

list_1 = ['His', 'Mat', 'Fis','Comp']
list_2 = list_1
print(list_1)
print(list_2)

list_1 = ['His', 'Mat', 'Fis','Comp']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 'Art'
print(list_1)
print(list_2)

tuple_1 = ('His', 'Mat', 'Fis', 'Comp')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

#tuple_1 = ('His', 'Mat', 'Fis', 'Comp')
#tuple_2 = tuple_1
#print(tuple_1)
#print(tuple_2)
#tuple_1[0] = 'Art'
#print(tuple_1)
#print(tuple_2)

cs_courses = {'His', 'Mat', 'Fis', 'Comp'}
print(cs_courses)

cs_courses = {'His', 'Mat', 'Fis', 'Comp', 'Mat'}
print(cs_courses)

cs_courses = {'His', 'Mat', 'Fis', 'Comp', 'Mat'}
print('Mat' in cs_courses)

cs_courses = {'His', 'Mat', 'Fis', 'Comp'}
art_courses = {'His', 'Mat', 'Art', 'Des'}
print('Mat' in cs_courses)

cs_courses = {'His', 'Mat', 'Fis', 'Comp'}
art_courses = {'His', 'Mat', 'Art', 'Des'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

empty_list = []
empty_list = list()