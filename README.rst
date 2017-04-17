This is a proof of concept for the idea of form signals, as discussed here: https://groups.google.com/forum/#!topic/django-developers/SviNiWy3Bjc

It uses a fork of Django from here:
https://github.com/seddonym/django/tree/ticket_27923

Installation
============

.. code::

    git clone git@github.com:seddonym/formsignals.git
    cd formsignals
    mkvirtualenv -ppython3 formsignals
    pip install -r requirements.pip
    python manage.py migrate
    python manage.py runserver
    
