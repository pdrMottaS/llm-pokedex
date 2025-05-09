from fastapi import APIRouter
from model import PokemonAsk
from agent import agent_pokemon

router = APIRouter(prefix="/pokemon")

@router.post("/")
def ask_pokemon(pokemon_ask:PokemonAsk):
    answer = agent_pokemon(pokemon_ask.question)
    return {
        "answer":answer
    }
