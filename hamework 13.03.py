import requests
import random

page = random.randint(1, 7438)
url = f'https://api.disneyapi.dev/character?pageSize=1&page={page}'
response = requests.get(url)
currensies_data = response.json()['data']
if response.ok:
    print(f"Ім\'я: {currensies_data['name']}, фільми: {currensies_data['films']}, короткі фильми: {currensies_data['shortFilms']}, ТВ-шоу "
          f"{currensies_data['tvShows']}.".replace("[]", "---"))
else:
    print('Щось пішло не так...')
    print(f'{response.status_code=}')



