build:
	docker build -t registry.edmodo.io/party94-base . 
	
push:
	docker push registry.edmodo.io/party94-base

run:
	docker run -it -p 8083:8083 -p 8086:8086 -v $(shell pwd):/app/ registry.edmodo.io/party94-base:latest 

bash:
	docker run -it -p 5001:5001 -v $(shell pwd):/app/ registry.edmodo.io/party94-base:latest bash

launch:
	docker run -p 5001:5001 -d registry.edmodo.io/party94-base:latest

