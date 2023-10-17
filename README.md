# Run Commands
### docker-compose.yaml
```
deploy:
    replicas: 3
```
### docker compose command
```
$ docker compose up --scale web=3
```
### add container with compose
```
$ docker compose up -d --scale web=2
```
### add container with docker run 
```
$ docker run -d --name  \
-e RAILS_ENV= \
-e POSTGRES_HOST= \
-e POSTGRES_DB= \
-e POSTGRES_USER= \
-e POSTGRES_PASSWORD= \
-e = \
--hostname=web
pims/web:v1 ./bin/rails server

$ docker network connect pims-z1-docker_default web2
```