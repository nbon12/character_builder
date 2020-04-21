# character_builder
Character Builder System for LARP games.

This character builder allows you to construct a character for your favorite LARP.
The skill builder lets LARP admins define skill dependencies on other skills, descriptions, cost.
Users can build characters with a pool of character points. The system remembers how many skill points you have.
The system tracks attendance of characters. After each event, each character gains an additional skill point to spend.

This LARP builder is specificially designed for the Lands of Exile LARP at landsofexile.com

# Developer Instructions

## Installation
1. Install Python 3.7+ https://www.python.org/downloads/
2. Install pipenv https://github.com/pypa/pipenv
3. Clone the repo
4. From within the repo, run `pipenv shell` - any time you run the server, you should remain in this shell. When you install new dependencies, run `pipenv install package` instead of `pip install package`
5. Run `pipenv install --dev` to install the dependencies locally.
6. Rename the file .env.example to .env
7. Run the development server `docker-compose up`
8. Apply migrations, run `make run-migrations`
9. Go to localhost:8000 in your browser, you should see a web app running.
10. Create a super user: change directories (cd) to character_builder/character_builder/manage.py file, and run `python manage.py createsuperuser`
11. go to localhost:8080/admin and enter the credentials you used.

## Deployment
1. Set the environment variables by renaming .env.example to .env
2. Set the SECRET_KEY environment variable `export SECRET_KEY=...`
3. Run `docker-compose up`. This should build the two containers (web server and database).


