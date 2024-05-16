run:
	@uvicorn src.main:app --reload

crate-migrations:
	@PYTHONPATH=$PYTHONPATH:${pwd} alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:${pwd} alembic upgrade head
