#!/bin/sh
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
gunicorn --bind 0.0.0.0:8000 --access-logfile acc.log --error-logfile err.log ask.wsgi:application
mysql -u root -p
CREATE DATABASE ask;

pip install django-twitter-bootstrap==3.3.0

# settings.py:

python manage.py loadtestdata qa.Question:20
sudo pip install django-autofixture
NSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active,	date_joined) VALUES('123', '2009-06-04 18:13:56', 1, 'simple', 'surname', 'first', 'me@example.com', 1, 1,'2009-06-04 18:13:56')
