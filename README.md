## Description

Full stack React-Django pet project. Shortens url address and keeps it valid within the selected period (up to 1 year).

### Installation (Windows)

- Inside a terminal navigate to the 'backend' folder, create/activate a virtual environment with `pipenv shell`
- install the project requirements using `pip install -r requirements.txt`
- Go to url_shortener project `cd .\url_shortener\` and execute `python manage.py runserver`.
- In another terminal navigate to the 'frontend\gui' folder, install the dependencies using `npm i`
- Run the server with `npm start` script and go to http://localhost:3000 to see the app.

### Testing

In order to test the app locally, you'll need to prefix the shortened url with `http://localhost:8000/api`. For example, `http://localhost:8000/api/6vyv6` is a valid link.

### Other API features:

- path/api/ - to see the whole database
- path/api/create/ - to create a new record
- path/api/delete_expired/ - to delete all expired links (executed with every page update for testing purpose)
