
'''

1

a = int(input('Число'))
b = int(input('Степень:'))

print(a ** b)
'''

'''

2

correctnumbers = 0
for i in range(100, 999):
    b = (i % 10)
    c = ((i //10 )% 10)
    d = (((i // 10) //10) % 10)
    if b == c or c == d or b == d:
        correctnumbers += 1
print(correctnumbers)

'''

'''

3

correctnumbers = 0
for i in range(100, 9999):
    b = (i % 10)
    c = ((i // 10) % 10)
    d = (((i // 10) // 10) % 10)
    e = ((((i // 10) // 10) // 10) % 10)
    if not b == c and not c == d and not d == e:
        correctnumbers += 1
print(correctnumbers)
'''
'''
4 

1 варіант

a = int(input('число'))
a1 = 0
b = str(a)
b1 = len(b)



for i in range(1, b1 + 1):
    c = ((a // 10 ** (b1 - i)) % 10)
    if c == 3 or c == 6:
        print(' ', end='')
    else:
        print(c, end='')



2 варіант

a = int(input('число'))
a1 = 0
b = str(a)
b1 = len(b)


for i in range(1, b1 + 1):
    c = ((a // 10 ** (b1 - i)) % 10)
    if not c == 3 and not c == 6:
        print(c, end='')
'''