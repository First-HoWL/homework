
import random
import time

start = time.time()
a = random.randint(1, 500)
sprob = 0
print(a)  # потрібно для тестів
while True:
    sprob += 1
    b = int(input('Яке число?'))
    if a == b:
        print('Вгадав')
        break
    elif b == 0:
        print('Гру завершено')
        break
    else:
        if a - b < 20 and a - b > -20:
            print('Гаряче,', end=' ')
            if b < a:
                print('Більше')
            else:
                print('Меньше')
        elif a - b < 50 and a - b > -50:
            print('Тепло,', end=' ')
            if b < a:
                print('Більше')
            else:
                print('Меньше')
        elif a - b < 100 and a - b > -100:
            print('Холодно,', end=' ')
            if b < a:
                print('Більше')
            else:
                print('Меньше')
        else:
            print('Дуже холодно,', end=' ')
            if b < a:
                print('Більше')
            else:
                print('Меньше')
end = time.time()
print(f'витрачено часу {round(end - start, 2)} сек')
print(f'витрачено спроб: {sprob}')
