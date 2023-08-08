# Flask with PostgreSQL using Docker Compose

## Create and fill in .env.dev values based on the .example.env

## Bring up the services with
```
$ docker compose -f docker-compose-dev.yml up -d --build
```

## the `--build` flag should only be used when you want to rebuild the images. If there weren't changes to the Dockerfile(s) or Docker compose file, there's no need to use `--build` beyond the first time you bring up the services.

## Bring down the services with
```
$ docker compose -f docker-compose-dev.yml down
```

## To connect to running Flask app container, get the container id:
```
$ docker ps
```
## Copy the Container ID of the Flask app and run an interactive terminal session in the running container:
```
$ docker exec -it <container id> /bin/sh
```

## To connect to the running Postgres container, get the container ID using the same command as earlier.

## Once in that container, access the postgres cli with
```
$ psql -U <the POSTGRES_USER from your .env.dev> <the POSTGRES_DB value from your .env.dev>
```

## You can tidy up your system if unused containers are present with:
```
$ docker system prune
```