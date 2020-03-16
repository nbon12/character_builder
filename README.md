# character_builder
Character Builder System for the Lands of Exile LARP

# Developer Instructions

## Installation
1. Install Python 3.7+ https://www.python.org/downloads/
2. Install pipenv https://github.com/pypa/pipenv
3. Clone the repo
4. From within the repo, run `pipenv shell` - any time you run the server, you should remain in this shell. When you install new dependencies, run `pipenv install package` instead of `pip install package`
5. Run `pipenv install --dev` to install the dependencies locally.
6. Apply migrations ``
7. Run the development server `python manage.py runserver`
8. Go to localhost:8000 in your browser, you should see a web app running.


