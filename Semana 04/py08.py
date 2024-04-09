def hello_func():
    pass
hello_func()


def hello_func():
    print('Hello functon')
hello_func()


def hello_func():
    print('Hello functon')
print('Hello functon')
print('Hello functon')
print('Hello functon')
print('Hello functon')


def hello_func():
    print('Hello functon')
print('Hello functon.')
print('Hello functon.')
print('Hello functon.')
print('Hello functon.')


def hello_func():
    print('Hello functon!')
hello_func()
hello_func()
hello_func()
hello_func()


def hello_func():
    return 'Hello function.'
print(hello_func())


def hello_func():
    return 'Hello function.'
print(len('Test'))


def hello_func():
    return 'Hello function.'
print(hello_func().upper())


def hello_func(greeting):
    return '{} Funtion.'.format(greeting)
print(hello_func('Hi'))


def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)
print(hello_func('Hi'))


def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)
print(hello_func('Hi', name = 'Corey'))



def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Mat', 'Art', name='John', age=22)



def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ('Mat', 'Art')
info = {'name': 'John', 'age': 22, }

student_info(courses, info)



def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ('Mat', 'Art')
info = {'name': 'John', 'age': 22, }

student_info(*courses, **info)



month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days(month)
print(is_leap(2017))


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days(month)
print(is_leap(2020))


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days(month)
print(days_in_month(2017, 2)) 