from langchain.tools import Tool
from service import get_type

def type_route(question):
    name = question.split()[-1].strip("?")
    data = get_type(name)
    if "erro" in data:
        return data["erro"]
    return f"O tipo {data['nome']} possui os movimentos: {', '.join(data['moves'])} e os pokemons que são desse tipos são: {', '.join(data['pokemons'])}"


types_tool = Tool(
    name = "type_tool",
    func=type_route,
    description="Retorna informações sobre o tipo de pokemon, seus movimentos e pokemons que possuem esse tipo"
)