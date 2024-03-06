# Liga PWr
Web app for PWr Sports League

[Data base diagram](https://dbdiagram.io/d/Liga-PWr-65df5266cd45b569fb210bfd)

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/informatyzacja/LigaPWr
    $ cd LigaPWr
    
**RECOMMENDED** Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

To build docker image(may need to use elevated privileges):

    $ docker build .

To run docker image with postgres container and postgres admin page, you can run(may need to use elevated privileges):
    
    $ docker-compose up -d

If no env variables are set, server defaults to db.sqlite3 db in main repo directory, example postgres config can be found in docker compose.
