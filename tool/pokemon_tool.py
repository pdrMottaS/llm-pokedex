from langchain.tools import Tool
from service import get_pokemon

def pokemon_route(question):
    name = question.split()[-1].strip("?")
    data = get_pokemon(name)
    if "erro" in data:
        return data["erro"]
    return f"O Pokémon {data['nome']} tem {data['altura']} m de altura, pesa {data['peso']} kg e possui os tipos: {', '.join(data['tipos'])}."

pokemons_tool = Tool(
    name = "pokemon_tool",
    func=pokemon_route,
    description="Retorna informações sobre o nome, altura, peso, id da especie e tipos do pokemon"
)