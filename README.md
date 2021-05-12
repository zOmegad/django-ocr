# 🍪 Petitbeurre OCR

**Petitbeurre** is a web app built with Django for an openclassroom project. The app finds healthier food after a search. You can create your account with email and username and save food as favorite. This app uses Openfoodfact API.

# Prerequisite

- Python3 & pip
- Virtualenv or something similar


## Installation
- Clone the repo
`git clone https://github.com/zOmegad/django-ocr.git && cd django-ocr`

- Create environment
`virtualenv env && source env/bin/activate`

- Create your environment and then
`pip install -r requirements.txt`

- Run migrations
`./manage.py migrate`

## Database injection

Python script that uses **Openfoodfacts** API to create data. You can find it at 'food/management/commands/inject.py'
`./manage.py inject`

## Testing
To run tests files :
`./manage.py test tests/`

To check pep8 :
`flake8 --exclude env`

Coverage :
(Run `./manage.py runserver` before running the following command..)

`coverage run --source='.' manage.py test tests.unit.food.tests_units_food tests.unit.favorite.tests_units_favorite tests.unit.profile.tests_units_profile tests.integration.search.tests_search_integration tests.functional.test_saved_food.tests_saved_food`


Report :
`coverage report --omit=*/apps.py,env/*,*/migrations/*,*/asgi.py,*/wsgi.py,manage.py,tests/*`
