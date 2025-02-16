static:
	sh static.sh

up:
	docker-compose --env-file .env up --build

down:
	docker-compose down

pexp:
	poetry export --without-hashes --without-urls --output requirements.txt -f requirements.txt

lint:
	flake8 .
	isort --check-only .

format:
	isort .
