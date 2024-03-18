import random



def new_funk(a, b):
    if b < 0:
        return None
    elif b == 0:
        return 1
    else:
        return a * new_funk(a, b - 1)

def sum_numb(a, b):
    if a > b:
        return None
    elif a == b:
        return a
    else:
        return a + sum_numb(a + 1, b)


def prnt_zirki(a):
    if a <= 0:
        print(None)
    elif a == 1:
        print('*')
        return ' '
    else:
        print('*', end = '')
        prnt_zirki(a - 1)




'''
1

print(new_funk(int(input('number: ')), int(input('stepen: '))))
'''
'''
2

print(sum_numb(int(input('first_number: ')), int(input('second_number: '))))
'''

'''
3

prnt_zirki(int(input('Скільки: ')))
'''




def bot_chosse():
    bot_choose = random.randint(1, 3)
    if bot_choose == 1:
        bot_choose = 'к'
    elif bot_choose == 2:
        bot_choose = 'н'
    elif bot_choose == 3:
        bot_choose = 'б'
    print(bot_choose)
    return bot_choose


def people_chosse():
    while True:
        a = input('к, н або п')
        if a in ['к', 'н', 'п']:
            return a


def full_name(a):
    if a == 'к':
        return 'Камінь'
    elif a == 'п':
        return 'Папір'
    elif a == 'б':
        return 'Бумага'



def chosse(a, b):
    if a == b:
        return 'нічія'
    elif a == 'к' and b == 'н':
        return 'Камінь виграв ножиці'
    elif a == 'б' and b == 'к':
        return 'Бумага виграла камінь '
    elif a == 'к' and b == 'б':
        return 'Бумага виграла камінь'
    elif a == 'б' and b == 'н':
        return 'Ножиці виграли бумагу'
    elif a == 'н' and b == 'к':
        return 'Камінь виграв ножиці'
    elif a == 'к' and b == 'б':
        return 'Бумага виграла камінь '
    elif a == 'б' and b == 'к':
        return 'Бумага виграла камінь'
    elif a == 'н' and b == 'б':
        return 'Ножиці виграли бумагу'
    else:
        return None



g = chosse(people_chosse(), bot_chosse())
print(full_name(people_chosse()))
print(g)