import requests
date = input('Дата у форматі YYYY.M.D:')

address = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/'
first_url = f"{address}currencies.json"
currensies_response = requests.get(first_url)
currensies_list = list(currensies_response.json().keys())
stop_program = 0
while True:
    currency_from = str(input('Перша валюта'))
    for i in range(len(currensies_list)):
        if currency_from == currensies_list[i]:
            break
        elif i == len(currensies_list) - 1:
            print('NOT CORRECT!!!!!!')
            stop_program = 1
            break
    if stop_program == 1:
        break
    currency_to = str(input('Друга валюта'))
    for i in range(len(currensies_list)):
        if currency_to == currensies_list[i]:
            break
        elif i == len(currensies_list) - 1:
            print('NOT CORRECT!!!!!!')
            stop_program = 1
            break
    if stop_program == 1:
        break

    amount = int(input('Скільки?'))
    url = f'{address}currencies/{currency_from}.json'
    response = requests.get(url)

    if response.ok:
        as_json = response.json()[currency_from]
        rate = as_json[currency_to]

        print(f"{amount} {currency_from} = {round(rate * amount, 2)} {currency_to}")
