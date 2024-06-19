install:
	poetry install

lint:
	poetry run flake8

pytest:
	poetry run pytest