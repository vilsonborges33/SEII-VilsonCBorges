import numpy as np
#import matplotlib.pyplot as plt

a1 = np.array([2, 4, 5, 6, 10])
print(a1)
print(a1[2])
print(a1[2:])
print(a1[:-2])
print(a1[1:-2])
print(a1>3)
print(a1[a1>3])


names = np.array(['Jin', 'Luke', 'Josh', 'Pete'])
print(names)

fist_letter_j = np.vectorize(lambda s: s[0])(names)=='j'
f = lambda s: s[0]
print(f('animal'))



names = np.array(['Jin', 'Luke', 'Josh', 'Pete'])
fist_letter_j = np.vectorize(lambda s: s[0])(names)=='j'
d = np.vectorize(lambda s: s[0])(names)
print(d)



names = np.array(['Jin', 'Luke', 'Josh', 'Pete'])
fist_letter_j = np.vectorize(lambda s: s[0])(names)=='J'
d = np.vectorize(lambda s: s[0])(names) =='J'
print(d)
print(fist_letter_j)
print(names[fist_letter_j])

print(a1)
print(a1%4)
print(a1%4 == 0)
print(a1[a1%4 == 0])