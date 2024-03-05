import requests
import random

page = random.randint(1, 7438)
url = f'https://api.disneyapi.dev/character?pageSize=1&page={page}'
response = requests.get(url)
currensies_data = response.json()['data']
if response.ok:
    print(f"Ім\'я: {currensies_data['name']}")
    print('Фільми:')
    for i in range(len(currensies_data['films'])):
        print("  -", currensies_data['films'][i].replace("[]", "---"))
    print('Короткі фильми:')
    for i in range(len(currensies_data['shortFilms'])):
        print("  -", currensies_data['shortFilms'][i].replace("[]", "---"))
    print('ТВ-шоу:')
    for i in range(len(currensies_data['tvShows'])):
        print("  -", currensies_data['tvShows'][0].replace("[]", "---"))
    print('Ігри:')
    for i in range(len(currensies_data['videoGames'])):
        print("  -", currensies_data['videoGames'][i].replace("[]", "---"))
else:
    print('Щось пішло не так...')
    print(f'{response.status_code=}')



