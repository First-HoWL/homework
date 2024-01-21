'''

1

a = int(input('Номер дня неділі'))

if a == 1:
    print('Понеділок')
elif a == 2:
    print('Вівторок')
elif a == 3:
    print('Середа')
elif a == 4:
    print('Четверг')
elif a == 5:
    print('П\'ятниця')
elif a == 6:
    print('Субота')
elif a == 7:
    print('Неділя')
else:
    print('Невірно введені дані')
'''


'''

2

a = int(input('Номер місяця'))

if a == 1:
    print('Січень')
elif a == 2:
    print('Лютий')
elif a == 3:
    print('Березень')
elif a == 4:
    print('Квітень')
elif a == 5:
    print('Травень')
elif a == 6:
    print('Червень')
elif a == 7:
    print('Липень')
elif a == 8:
    print('Серпень')
elif a == 9:
    print('Вересень')
elif a == 10:
    print('Жовтень')
elif a == 11:
    print('Листопад')
elif a == 12:
    print('Грудень')
else:
    print('Невірно введені дані')
'''

'''

3

a = float(input('Число'))

if a > 0:
    print('Number is positive')
elif a < 0:
    print('Number is negative')
else:
    print('Number is equal to zero')
    
'''

'''

4

a = float(input('Перше число'))
b = float(input('Друге число'))

if a == b:
    print('Числа рівні')
elif a < b:
    print(a, '<',  b)
else:
    print(b, '<', a)
'''