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
            "tipos": [t["type"]["name"] for t in data["types"]]
        }
    return {"erro": "Pokémon não encontrado"}

def get_species(name:str):
    response = requests.get(f"{BASE_URL}/pokemon-species/{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        flavor = next((entry for entry in data["flavor_text_entries"]
                       if entry["language"]["name"] == "pt"), None)
        return {
            "nome": data["name"].title(),
            "descricao": flavor["flavor_text"] if flavor else "Descrição não encontrada"
        }
    return {"erro": "Espécie não encontrada"}