import requests

BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon(name:str):
    response = requests.get(f"{BASE_URL}/pokemon/{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        return {
            "nome": data["name"].title(),
            "altura": data["height"] / 10,
            "peso": data["weight"] / 10,
            "tipos": [t["type"]["name"] for t in data["types"]],
            "especie": data['species']['url'].strip('/').split('/')[-1]
        }
    return {"erro": "Pokémon não encontrado"}

def get_type(name:str):
    response = requests.get(f"{BASE_URL}/type/{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        return {
            "nome": data['name'],
            "pokemons": [t['pokemon']['name'] for t in data['pokemon']],
            "moves":[t['name'] for t in data['moves']]
        }
    return {"erro": "Tipo não encontrada"}