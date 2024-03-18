import random



def bot_chosse():
    bot_choose = random.randint(1, 3)
    if bot_choose == 1:
        bot_choose = 'к'
    elif bot_choose == 2:
        bot_choose = 'н'
    elif bot_choose == 3:
        bot_choose = 'п'
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
    elif a == 'н':
        return 'Ножиці'
    elif a == 'p':
        return 'Player'
    elif a == 'b':
        return 'Bot'


def chosse(a, b):
    if a == b:
        return 'нічія'
    elif a == 'к' and b == 'н':
        return 'p'
    elif a == 'п' and b == 'к':
        return 'p'
    elif a == 'к' and b == 'п':
        return 'b'
    elif a == 'п' and b == 'н':
        return 'b'
    elif a == 'н' and b == 'к':
        return 'p'
    elif a == 'к' and b == 'п':
        return 'b'
    elif a == 'п' and b == 'к':
        return 'p'
    elif a == 'н' and b == 'п':
        return 'p'
    else:
        return None


people = people_chosse()
bot = bot_chosse()
whos = full_name(chosse(people, bot))
print(f'Ваш вибір: {full_name(people)}')
print(f'Вибір бота: {full_name(bot)}')
print(f'{whos} - Win!') # Якщо буде нічия буде написано None - Win!
