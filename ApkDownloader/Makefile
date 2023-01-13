lint:
	flake8 app
	mypy app

format:
	black app
	black main.py
	black migration
	isort app
	isort main.py

prepare:
	make lint
	make format
