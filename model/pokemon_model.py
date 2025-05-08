from pydantic import BaseModel

class PokemonAsk(BaseModel):
    question: str