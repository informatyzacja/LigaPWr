.PHONY: install, install-dev, lint, format, dev

install:
	@pipenv install $(package)

install-dev:
	@pipenv install --dev $(package)

lint:
	@pipenv run pylint ./**/*.py --output-format=colorized

format:
	@pipenv run black .

admin:
	@pipenv run python3.11 manage.py $(command)

dev:
	@pipenv run python3.11 manage.py migrate
	@pipenv run python3.11 manage.py runserver