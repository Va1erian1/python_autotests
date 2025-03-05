import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '18cb2f70665ed707f952cc745cc14a9c'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '23074'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]["trainer_name"] == 'Валериан'