___
Step 1 - Installing PostgreSQL

    sudo apt update
    sudo apt install postgresql postgresql-contrib

___

Step 2 - Using PostgreSQL Roles and Databases

    sudo -u postgres psql
    postgres=# \password postgres
    Enter new password for user "postgres": 
    Enter it again: 
    postgres=# 


sudo -u postgres psql -c 'alter user fox with fox_db' postgres

sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'fox';"