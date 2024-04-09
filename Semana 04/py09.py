
import sys
sys.path.append('/Users/User/Desktop/My-Modules')

from my_module import find_index, test


courses = ['His', 'Mat', 'Fis', 'Comp']

index = find_index(courses, 'Mat')



print(sys.path)




import random
courses = ['His', 'Mat', 'Fis', 'Comp']
random_course = random.choice(courses)
print(random_course)



import math
courses = ['His', 'Mat', 'Fis', 'Comp']
rads = math.radians(90)
print(rads)




import math
courses = ['His', 'Mat', 'Fis', 'Comp']
rads = math.radians(90)
print(math.sin(rads))



import datetime
import calendar
courses = ['His', 'Mat', 'Fis', 'Comp']
today = datetime.date.today()
print(today)



import datetime
import calendar
courses = ['His', 'Mat', 'Fis', 'Comp']
today = datetime.date.today()
print(today)
print(calendar.isleap(2017))


import datetime
import calendar
courses = ['His', 'Mat', 'Fis', 'Comp']
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))



import os
courses = ['His', 'Mat', 'Fis', 'Comp']
print(os.getcwd())


import os
courses = ['His', 'Mat', 'Fis', 'Comp']
print(os.__file__)


import antigravity