all: demo

demo:
	docker-compose up \
		--build \
		--exit-code-from app \
		--abort-on-container-exit

logs:
	docker-compose logs app

stop:
	docker-compose stop

clean_db:
	rm -rf data
