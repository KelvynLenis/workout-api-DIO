from src.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import  Field
from src.contrib.schemas import BaseSchema


class Categoria(BaseSchema):
  nome: Annotated[str, Field(description="Nome da categoria", examples='Scale', max_length=10)]
  