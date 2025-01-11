# Project on user authentication #

## stack python, streamlit library, postgres, docker ##

1. app.py --> for frontend 
2. db.py --> for authentication against postgres db
3. user-creation.py --> for new user creation in postgres

## installation of python 3.10 version on windows. #
-> https://www.python.org/downloads/

## installation of docker in windows. #
-> https://docs.docker.com/desktop/setup/install/windows-install/#start-docker-desktop

## setup of postgres on docker. #
-> docker run -d --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=admin123 -e POSTGRES_DB=auth -e PGDATA=/var/lib/postgresql/data/pgdata -v C:/Downloads/:/var/lib/postgresql/data -p 5432:5432 postgres

-> docker ps -a 

-> docker inspect postgres & docker logs postgres

-> docker exec -it postgres /bin/bash 

-> psql -h localhost -U postgres 

-> CREATE DATABASE auth;

-> GRANT ALL PRIVILEGES ON DATABASE auth TO postgres;

-> \c auth      # to switch to auth database

-> CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
    );

->\du # to list the users

->\l  # to list the databases

->\dt # to list the tables


