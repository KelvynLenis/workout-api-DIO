from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4

from src.categorias.schemas import CategoriaIn, CategoriaOut
from src.categorias.model import CategoriaModel
from src.contrib.dependencies import DataBaseDependency
from sqlalchemy.future import select

router = APIRouter()

@router.post('/', summary='Criar uma nova categoria', status_code=status.HTTP_201_CREATED, response_model=CategoriaOut)
async def post(db_session: DataBaseDependency, categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:
  categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
  categoria_model = CategoriaModel(**categoria_out.model_dump())
  
  db_session.add(categoria_model)
  await db_session.commit()

  return categoria_out

@router.get('/', summary='Consultar todas as categorias', status_code=status.HTTP_200_CREATED, response_model=list[CategoriaOut])
async def query(db_session: DataBaseDependency) -> list[CategoriaOut]:
  categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
  
  return categorias


@router.get(
  '/{id}', 
  summary='Consultar uma categoria', 
  status_code=status.HTTP_200_CREATED, 
  response_model=CategoriaOut
)
async def query(id: UUID4, db_session: DataBaseDependency) -> CategoriaOut:
  categoria: CategoriaOut = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()

  if not categoria:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Categoria não encontrada')
  
  return categoria

