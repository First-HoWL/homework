
'''

1

a = int(input('число в діапазоні від 1 до 100'))

if a < 1 or a > 100:
    print('Не підходить!')
elif a % 3 == 0 and a % 5 == 0:
    print('Fizz Buzz')
elif a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')
else:
    print(a)

'''
'''

2

a = int(input('Число'))

b = int(input('Степень від 0 до 7:'))

if b < 0 or b > 7:
    print('Не вірний степінь')
else:
    print(a ** b)

'''
'''

3

print('Ваш оператор Vodafon')
print('Оператори:')
print('1.Vodafone безкоштовно')
print('2.Kievstar 1хв 2грн')
print('3.lifecell 1хв 2.50грн')

a = int(input('На якого оператора дзвонити?'))
b = int(input('Скільки хвилин розмова?'))
if a == 1:
    print('Безкоштовно')
elif a == 2:
    print('Коштує', b * 2, 'грн')
elif a == 3:
    print('Коштує', b * 2.5, 'грн')
else:
    print('Не правильно вибраний оператор!!!')


'''

'''

4

a = int(input('продажі першого менеджера'))
b = int(input('продажі другого менеджера'))
c = int(input('продажі третього менеджера'))

zarplata_a = 300
zarplata_b = 300
zarplata_c = 300



if a > b and a > c:
    zarplata_a += 200
elif b > a and b > c:
    zarplata_b += 200
elif c > a and c > b:
    zarplata_c += 200

if a < 0:
    print('продажі першого менеджера не вірні')
elif a < 500:
    zarplata_a += (a / 100) * 3
elif a < 1000:
    zarplata_a += (a / 100) * 5
else:
    zarplata_a += (a / 100) * 8

if b < 0:
    print('продажі другого менеджера не вірні')
elif b < 500:
    zarplata_b += (b / 100) * 3
elif b < 1000:
    zarplata_b += (b / 100) * 5
else:
    zarplata_b += (b / 100) * 8

if c < 0:
    print('продажі третього менеджера не вірні')
elif c < 500:
    zarplata_c += (c / 100) * 3
elif c < 1000:
    zarplata_c += (c / 100) * 5
else:
    zarplata_c += (c / 100) * 8

if a > b and a > c:
    print('Перший менеджер кращий, його зарплата:', zarplata_a)
    print('Другий менеджер:', zarplata_b)
    print('Третій менеджер:', zarplata_c)
elif b > a and b > c:
    print('Другий менеджер кращий, його зарплата:', zarplata_b)
    print('Перший менеджер:', zarplata_a)
    print('Третій менеджер:', zarplata_c)
elif c > a and c > b:
    print('Третій менеджер кращий, його зарплата:', zarplata_c)
    print('Перший менеджер:', zarplata_a)
    print('Другий менеджер:', zarplata_b)
else:
    print('Ні хто не кращій')
    print('Перший менеджер:', zarplata_a)
    print('Другий менеджер:', zarplata_b)
    print('Третій менеджер:', zarplata_c)
    
    
'''


