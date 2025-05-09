from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from controller import pokemon_router

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pokemon_router)

uvicorn.run(app, port=5000, host="0.0.0.0")
