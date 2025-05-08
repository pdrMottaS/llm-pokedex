from fastapi import APIRouter
from model import PokemonAsk
from chain import generate_router_chain,generate_destination_chains

router = APIRouter(prefix="/pokemon")

prompt_infos, destination_chains, default_chain = generate_destination_chains()
chain = generate_router_chain(prompt_infos, destination_chains, default_chain)

@router.post("/")
def ask_pokemon(pokemon_ask:PokemonAsk):
    answer = chain.run(pokemon_ask.question)
    return {
        "answer":answer
    }
