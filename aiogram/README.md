Activate
===
---
1. python3 -m venv venv
2. source venv/bin/activate
3. python3 -m pip install --upgrade pip
4. sudo apt install python3.10-venv
---


python-dotenv
===
---

    pip install python-dotenv

aiogram
    
    pip install -U aiogram

SQLAlchemy

    pip install SQLAlchemy

Faker

    pip install Faker

Save to requirements.txt

    pip freeze > requirements.txt


update

    apt-get update
    apt-get upgrade
    sudo apt update 
    sudo apt upgrade -y

install

    sudo apt-get install package-name

clean

    sudo apt-get autoremove
    sudo apt autoclean

vboxsf

    sudo usermod -a -G vboxsf fox

kill
    
    sudo lsof -t -i tcp:8000 | xargs kill -9

venv

    python -m venv venv
    
    pip install virtualenv (mind)
    virtualenv venv

pip

    python -m pip install --upgrade pip

django

    pip install django
    django-admin startproject config .

    python manage.py migrate
    python manage.py makemigrations

    python manage.py createsuperuser
    python manage.py runserver    

    django-admin startapp blog  *****

    python manage.py shell
    python manage.py collectstatic

    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

tests 
    
    https://docs-djangoproject-com.translate.goog/en/4.1/topics/testing/overview/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en
    # for ran all tests
    $ ./manage.py test

    # Run all the tests in the animals.tests module
    $ ./manage.py test animals.tests
    
    # Run all the tests found within the 'animals' package
    $ ./manage.py test animals
    
    # Run just one test case
    $ ./manage.py test animals.tests.AnimalTestCase
    
    # Run just one test method
    $ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak

apps

    python -m pip install Pillow

requirements

    pip freeze > requirements.txt 
    pip install -r requirements.txt
    pip uninstall requirements.txt


token

    from rest_framework.authtoken.models import Token
        token = Token.objects.create(user=fox)
    print(token.key)

curl 

    curl -X POST -H “Authorization: Bearer 03e24877ffd959815a174a958a1673d21f37698d” -H “Content-Type: application/json” -H “Accepts: application/json” http://localhost:8000/api/token_auth/
    curl -H “Authorization: Bearer 03e24877ffd959815a174a958a1673d21f37698d”  http://localhost:8000/api/v1/