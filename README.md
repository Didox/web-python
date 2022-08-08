
- https://docs.djangoproject.com/en/4.0/topics/install/
- https://docs.djangoproject.com/en/4.0/intro/tutorial01/
- https://docs.djangoproject.com/en/1.8/intro/tutorial02/
- https://docs.djangoproject.com/en/4.0/ref/databases/
- https://github.com/Didox/python-crud-django
- 

```python
python -m django --version

# criando app admin django
django-admin startproject mysite
cd mysite
python manage.py
python manage.py runserver
open http://127.0.0.1:8000/
open http://127.0.0.1:8000/admin

python manage.py migrate
python manage.py createsuperuser

# criando meu app
python manage.py startapp myapp

# install driver mysql
pip install mysqlclient
python manage.py migrate
python manage.py createsuperuser

```
