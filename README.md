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

To run all docker containers(may need elevated privilege first time running):

```
docker compose up -d
```
