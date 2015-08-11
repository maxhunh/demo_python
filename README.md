INSTALL DJANGO

sudo pip install Django==1.8.3
-> install django (use pip)

Test: python -c "import django; print(django.get_version())"
-> test status setup

django-admin startproject mysite
-> create project

python manage.py migrate

python manage.py runserver
-> run server