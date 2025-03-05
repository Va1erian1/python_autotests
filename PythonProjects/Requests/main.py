import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '18cb2f70665ed707f952cc745cc14a9c'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)

if response_create.status_code == 201:
    response_data = response_create.json()
    pokemon_id = response_data.get('id')  
    print(f'ID: {pokemon_id}')

    body_change = {
        "pokemon_id": pokemon_id, 
        "name": "generate",
        "photo_id": -1
    }

    response_change = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change)
    print(f'change: {response_change.text}')

    body_add = {
        "pokemon_id": pokemon_id 
    }

    response_add = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add)
    print(f'add: {response_add.text}')

else:
    print(f'fault: {response_create.text}')
