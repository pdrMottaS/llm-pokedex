from fastapi import FastAPI
import uvicorn
from controller import pokemon_router

app = FastAPI()
app.include_router(pokemon_router)

uvicorn.run(app, port=5000)
