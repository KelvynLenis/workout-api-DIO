from fastapi import APIRouter
from src.atleta.controller import router as atleta
from src.categorias.controller import router as categorias

api_router = APIRouter()
api_router.include_router(atleta, prefix=['/atletas'], tags=['/atletas'])
api_router.include_router(atleta, prefix=['/categorias'], tags=['/categorias'])
