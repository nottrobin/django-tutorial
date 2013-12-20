Polls
=====

This is the Polls application that you create in the [djangoproject.net tutorial](https://docs.djangoproject.com/en/1.6/intro/tutorial01/).

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Demo
---

<http://django-polls-tutorial.herokuapp.com>

Running locally
---

If you have the dependencies:

``` bash
$ python3 manage.py syncdb
$ python3 manage.py runserver
```

### Dependencies

- Python > 3
- Django > 1.6
- django-extensions

    sudo apt-get install python3 python3-pip && pip3 install django django-extensions