include .env
export $(shell sed 's/=.*//' .env)

up:
	docker compose up -d

stop:
	docker compose stop

build:
	docker compose down
	docker compose up -d --build

migrate:
	docker compose exec web sh -c 'python manage.py migrate'

pgsql:
	docker compose exec db bash -c 'psql -U $$POSTGRES_USER -d $$POSTGRES_DB'


shell:
	docker compose exec web bash

down:
	docker compose down

ps:
	docker compose ps
# seed:
# 	docker compose exec web sh -c 'python manage.py seed'
