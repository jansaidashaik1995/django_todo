# django_todo

# Steps to follow to deploy django app on Heroku

# 1) install the required modules / libraries
    ---> ~$ pip install gunicorn
    ---> ~$ pip install whitenoise

# 2) setup the requirements.txt (i.e the libraries need to make the app works)
    ---> ~$ pip freeze > requirements.txt (this command will write the required libraries to requirements.txt)

# 3) create runtime.txt

# 4) create a Procfile
    ---> and include a statement as  web: gunicorn <todo_postgresql>wsgi --log-file - (the folder(todo_postgresql) name in which the wsgi.py file resides)

# 5) update settings.py file
    ---> update ALLOWED_HOSTS = [] as ALLOWED_HOSTS = ['django-todo-app-01.herokuapp.com', '127.0.0.1:8000']
    ---> set DEBUG = False

# 6) select deployment method as Github