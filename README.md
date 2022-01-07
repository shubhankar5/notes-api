# notes-api

## What is it?
An API that lets you add text notes and perform all CRUD operations on them.

## Key features
- Access to APIs restricted with proper permissions
- Throttling added to limit the number of times the API is accessed
- Pagination added for lists
- Filtering added with django-filters
- Ordering and searching
- Inheritable code with CBVs

## Tools used
Requirements have been added in [requirements.txt](/requirements.txt). The main components are:
- Django [Link](https://www.djangoproject.com/)
- Django REST Framework [Link](https://www.django-rest-framework.org)
- django-filters [Link](https://django-filter.readthedocs.io/en/stable/)

## How to use?
1. Install pip from this [link](https://pip.pypa.io/en/stable/installing/)
2. Install virtualenv from this [link](https://virtualenv.pypa.io/en/latest/installation.html)
3. Create a virtualenv and activate it. Refer [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)  
4. Create a directory called notes_app
5. Download all the files in the repository under this directory
6. Change the directory to notes_app
7. Run ```pip install -r requirements.txt```
8. Run ```python manage.py createsuperuser``` and create a superuser
9. Run ```python manage.py makemigrations```
10. Run ```python manage.py migrate```
11. Run ```python manage.py runserver```

## How to contribute?
Feel free to contribute to this repository and make this a better project. Thank you!
