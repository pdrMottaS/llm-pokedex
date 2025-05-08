from fastapi import APIRouter
from model import TranslateRequest
from langchain_groq import ChatGroq

router = APIRouter()
llm = ChatGroq(api_key="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",model="meta-llama/llama-4-scout-17b-16e-instruct")