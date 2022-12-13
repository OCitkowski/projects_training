Activate

    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip


python-dotenv

    pip install python-dotenv


SQLAlchemy

    pip install SQLAlchemy

Faker

    pip install Faker

Save to requirements.txt

    pip freeze > requirements.txt

**********************************
postgresql


    sudo -u postgres psql -c "\l"
    sudo apt-get install postgresql postgresql-contrib    
    postgres --version    
    psql -V
    psql postgres (для выхода из интерфейса используйте \q)    
    postgres=# create database db;