Overview
================================

This is a sample project to demonstrate how to configure a heroku hosted django app to use s3 for static files.  It uses the twitter bootstrap project to provide some boilerplate content.


You can read a description of the process in this blog post:
http://iknuth.com/2011/10/deploying-a-django-app-to-heroku-with-easy-static-files-on-s3/


Instructions
================================

Setup your environment.
--------------------------------

* virtualenv --no-site-packages . -p /usr/local/bin/python2.7
* source bin/activate
* pip install -r requirements.txt
* createdb blogdemo

Run the project locally.
------------------------

* python om/manage.py syncdb
* python om/manage.py runserver
And open http://localhost:8000

Deploy the project to heroku.
-----------------------------

*  heroku create --stack cedar
*  git push heroku master
*  heroku run python om/manage.py syncdb

Create an s3 bucket and add your AWS keys and info to settings.py.

Deploy your static files
------------------------

*  python om/manage.py collectstatic

This command is run locally.  No need to involve heroku.

And you are ready to go
-----------------------

*  heroku open
