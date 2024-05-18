from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat
from src.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
  nome: Annotated[str, Field(description="Nome do atleta", examples='João', max_length=50)]
  cpf: Annotated[str, Field(description="CPF do atleta", examples='123456789900', max_length=11)]
  idade: Annotated[int, Field(description="Idade do atleta", examples=25)]
  peso: Annotated[PositiveFloat, Field(description="Peso do atleta", examples=75.5)]
  altura: Annotated[PositiveFloat, Field(description="Altura do atleta", examples=1.70)]
  sexo: Annotated[str, Field(description="Sexo do atleta", examples='M', max_length=1)]

class AtletaIn(Atleta):
  pass
  
class AtletaaOut(Atleta, OutMixin):
  pass