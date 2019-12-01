## Description

This is a full stack React-Django pet project. It shortens a url address and keeps it valid within the defined period of time (up to 1 year).

### Installation (Windows)

Before getting started with the app, you might need to install [Python](https://www.python.org/downloads/) and pipenv (run `pip install pipenv`), if they are not already in place. Otherwise, skip directly to the app instalation:

- Inside a terminal navigate to the _backend_ folder and create/activate a virtual environment with `pipenv shell` command
- Install the project requirements using `pip install -r requirements.txt`
- Go to _url_shortener_ project: `cd url_shortener` and execute `python manage.py runserver`
- Open additional terminal, navigate to the _frontend_ folder, and install the dependencies using `npm i`
- Run the server with `npm start` and go to http://localhost:3000 to see the app

### Testing

In order to test the app locally, you'll need to prefix the shortened url with `http://localhost:8000/api`. For example, `http://localhost:8000/api/25t52`.

### Other API features:

- path/api/ - to see the whole database;
- path/api/create/ - to create a new record;
- path/api/delete_expired/ - to delete all expired links (executed with every page update for testing purpose).
