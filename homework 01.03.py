'''

1

a = input('Ваш вираз:')

b = a.split('+')
if len(b) > 1:
    print(f' {b[0]} + {b[1]} = {int(b[0]) + int(b[1])}')

b = a.split('-')
if len(b) > 1:
    print(f' {b[0]} - {b[1]} = {int(b[0]) - int(b[1])}')

b = a.split('/')
if len(b) > 1:
    print(f' {b[0]} / {b[1]} = {int(b[0]) / int(b[1])}')

b = a.split('*')
if len(b) > 1:
    print(f' {b[0]} * {b[1]} = {int(b[0]) * int(b[1])}')


'''

'''

2 

import random

a = [random.randint(-20, 20) for i in range(20)]
print(a)  # для тестів
videmni = []
dodatni = []
nuls = []
i = 0

for i in range(len(a)):
    if a[i] < 0:
        videmni.append(a[i])
print(videmni, '=',len(videmni), 'від\'ємних', min(videmni), 'мінімальне число')

for i in range(len(a)):
    if a[i] > 0:
        dodatni.append(a[i])
print(dodatni, '=', len(dodatni), 'додатних', max(dodatni), 'максімальне число')

for i in range(len(a)):
    if a[i] == 0:
        nuls.append(a[i])
print(nuls, '=', len(nuls), 'нулів')

'''