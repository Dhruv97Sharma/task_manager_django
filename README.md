# Django Fullstack Todo Application

Building a todo app using django in the backend and html, css, bootstrap and htmx in the frontend.

## Features

- Django 3.0+
- Uses [venv](https://docs.python.org/3/library/venv.html) - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with New Relic's Python agent.
- Bootstrap 5 for UI [bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/).
- Using SQLite managed DB [sqlite](https://www.sqlite.org/).


## How to install

```bash
$ cd todo_app
$ python -m venv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Access the UI of the Todo:

You can head to `http://localhost:8000/` to access the todo app list, add items in the list using the form, mark items as done or delete them.

## Deployment

It is possible to deploy to services such as [render](https://render.com/) or to your own server.


## License

The MIT License (MIT)