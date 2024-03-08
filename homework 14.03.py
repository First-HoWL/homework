'''

1

def print_text():
    print('\"Don\'t compare yourself with anyone in this world…\nif you do so, you are insulting yourself.\" \nBill Gates')


print_text()



2

def chisla(a, b):
    if a % 2 != 0:
        a = a + 1
        for i in range(a, b, 2):
            print(i)
    else:
        for i in range(a, b, 2):
            print(i)

chisla(int(input('перше число'), int(input('Друге число'))



З


def funk(a, b, c):
    if a == 1: # це треба, без нього коли довжина = 1 видає 2 знаки замість одного
        print(c)
    elif b == 1:
        for n in range(a):
            for i in range((a - 1)):
                print(c, end='')
            print(c)
    else:
        for i in range(a):
            print(c, end='')
        print()
        for i in range((a - 2)):
            print(c, end = '')
            for n in range((a - 2)):
                print(' ', end = '')
            print(c)
        for i in range(a):
            print(c, end='')

funk(int(input('довжина')), int(input('Пустый чи повный(0 чи 1)')), input('знак'))


4

def fmin(a, b, c, d, e):
    if a < b and a < c and a < d and a < e:
        print(f'{a} - меньше всіх')
    elif b < a and b < c and b < d and b < e:
        print(f'{b} - меньше всіх')
    elif c < b and c < a and c < d and c < e:
        print(f'{c} - меньше всіх')
    elif d < a and d < b and d < c and d < e:
        print(f'{d} - меньше всіх')
    elif e < a and e < b and e < c and e < d:
        print(f'{e} - меньше всіх')


fmin(int(input('перше число')), int(input('друге число')), int(input('третє число')), int(input('четверте число')), int(input('п\'яте число')))



5

def ymnogenie(a, b):
    final_num = int(1)
    if a > b:
        a, b = b, a
    for i in range(a, b):
        final_num *= i
    print(final_num)



ymnogenie(int(input('перше число')), int(input('друге число')))



6

def fun(a):
    return len(str(a))



print(fun(int(input('число'))))



7

def fun(i):
    a = str(i)
    if (a[0], a[1], a[2]) == (a[5], a[4], a[3]):
        return True
    else:
        return False

print(fun(int(input('Шестизначне число'))))

'''
