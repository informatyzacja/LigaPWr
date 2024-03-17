# Liga PWr
Web app for PWr Sports League

[Data base diagram](https://dbdiagram.io/d/Liga-PWr-65df5266cd45b569fb210bfd)

# Getting Started (Development)

## Prerequisites

- pipenv
- make

## Recommended
- pyenv (for easy handling different python versions)
    
## Startup

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/informatyzacja/LigaPWr
    $ cd LigaPWr

To start or create python environment:

```
pipenv shell --python 3.11 # to create
pipenv shell # to start
```

To install packages from Pipfile:

```
make install
```

To start development server:

```
make dev
```

You can also adjust environmental variables in compose.yaml file, mainly DEBUG and ADD_DUMMY_DATA, both of which take True/False as an input.

To run app via docker compose with nginx, certbot and postgres (may need elevated privilege first time running):

```
docker compose up -d
```

The above pulls needed docker images, and builds one with this django app, and second one with nginx with custom setup. Then it runs all containers as one app in one shared virtual network.

You can access app on localhost:80.

## Other commands

To add package:

```
make install package=[package name]
make install-dev package=[package name] # for development only
```

To lint code:

```
make lint
```

To format code:

```
make format
```
To add dummy data to database:

```
python3 manage.py add_dummy_data
```


