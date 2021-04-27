# django-ocr

coverage run --omit 'env/*' --source='.' manage.py test django_ocr

to inject db from openfoodfacts

./manage.py inject

flake8 --exclude env

./manage.py test tests/
