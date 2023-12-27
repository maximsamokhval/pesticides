.PHONY: build up down rebuild

build:
	docker-compose build
up:
	docker-compose up -d
down:
	docker-compose down
clean: down
	docker-compose rm -f
	docker-compose down --rmi all

rebuild: clean build up