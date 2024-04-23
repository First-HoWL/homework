import random
spisok = 'records.txt'


def random_number():
    number = random.randint(int(1), int(100))
    return number


def game_over(player_count):
    print(f'Ваш Счёт: {player_count}')
    with open(spisok, mode='r', encoding='utf8') as file:
        records = file.read().split('\n')
    if len(records) < 5:
        name = input('Ваше ім\'я (для списку лідерів):')
        records.append(f'{name} {player_count}')
    elif player_count > int((records[4].split(' '))[1]):
        records.pop(4)
        name = input('Ваше ім\'я(для списку лідерів):')
        records.append(f'{name} {player_count}')
    if len(records) >= 5:
        records = sort(records)
    print('Таблиця Лідерів:')
    for i in range(len(records)):
        a_list = records[i].split(' ')
        print(f'{a_list[0]}: {a_list[1]}')
    with open(spisok, mode='w', encoding='utf8') as file:
        file.write('\n'.join(records))


def sort(lists):
    list_for = []
    for i in lists:
        list_for += (i.split(' '))
    sorted_list = bubble_sort(list_for)
    return sorted_list


def bubble_sort(list_for):
    list_name = [list_for[0], list_for[2], list_for[4], list_for[6], list_for[8]]
    list_numb = [int(list_for[1]), int(list_for[3]), int(list_for[5]), int(list_for[7]), int(list_for[9])]
    is_changed = True
    while is_changed:
        is_changed = False
        for i in range(len(list_numb) - 1):
            if list_numb[i] < list_numb[i + 1]:
                list_numb[i], list_numb[i + 1] = list_numb[i + 1], list_numb[i]
                list_name[i], list_name[i + 1] = list_name[i + 1], list_name[i]
                is_changed = True
    lists = [f'{list_name[0]} {list_numb[0]}', f'{list_name[1]} {list_numb[1]}', f'{list_name[2]} {list_numb[2]}',
             f'{list_name[3]} {list_numb[3]}', f'{list_name[4]} {list_numb[4]}']
    return lists


def take_anwer():
    player_answer = input(f'{first_number} + {second_number} = ')
    return player_answer


lives = 3
count = int()
while True:
    first_number = int(random_number())
    second_number = int(random_number())
    answer = take_anwer()
    while True:
        if answer.isnumeric() or answer.lower() in ['quit', 'q', 'вихід', 'повернутися', 'закінчити'] or lives <= 0:
            break
        else:
            print('Not Correct answer!')
            answer = take_anwer()
    if answer.lower() in ['quit', 'q', 'вихід', 'повернутися', 'закінчити'] or lives <= 0:
        game_over(count)
        break
    if int(answer) == first_number + second_number:
        print('Correct!')
        count += 1
    else:
        print(f'Not Correct! {first_number} + {second_number} = {first_number + second_number}')
        lives -= 1
    if lives <= 0:
        print('Game over!')
        game_over(count)
        break
    print(f'Жизней: {lives}')
    print(f'Счёт: {count}')
