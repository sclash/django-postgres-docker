# Django with PostgreSQL and Docker

This Repo is for testing Django DB management functionalities with a PostgresDB.
Both the Django application and the Postgres server instance are running from inside communicating Docker containers.
Check the `docker-compose.yml` and `settings.py` to understand how.

- [Building and runnign the Docker containers](#building-and-runnign-the-docker-containers)
    - [Stop and Clear Containers](#stop-and-clear-containers)
- [Network Availability](#network-availability)
- [Connect to Postgres](#connect-to-postgres)
    - [Credentials](#credentials)

## Building and runnign the Docker containers

cd in the project directory (the one containing `docker-compose.yml`)

```bash
sudo docker compose build
sudo docker compose up
```
or 
```bash
sudo docker compose up --build
```

### Stop and Clear Containers

```bash
sudo docker compsoe down --volumes
sudo docker image prune
sudo docker network prune
```


## Network Availability
Both Containers are exposed on the local network at the following ports:

- Django: `<ipv4>:1111` e.g. `http://172.26.25.20:1111`
- Postgres: `<ipv4>:5432` e.g. `http://172.26.25.20:5432`

`NOTE`: the `<ipv4>` address must be listed in the `ALLOWED_HOSTS` in the `settings.py` file. (In this case it set to `'*'` e.g. any host is allowed)

## Connect to Postgres
You can connect at the PostgreSQL server using the above address while connectedd to the local network.

### Credentials

```
DB_NAME=django_postgres
DB_USERNAME=asergi
DB_PASSWORD=abcde
```




