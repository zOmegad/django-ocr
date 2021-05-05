# 🍪 Petitbeurre OCR

**Petitbeurre** is a web app built with Django for an openclassroom project. The app finds healthier food after a search. You can create your account with email and username and save food as favorite. This app uses Openfoodfact API.

# Prerequisite

- Python3 & pip
- Virtualenv or something similar


## Installation

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
`coverage run --omit 'env/*' --source='.' manage.py test django_ocr`
