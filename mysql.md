# MySQL

## Install

`brew install mysql` - creates mysql server with no password
`mysql.server start`  - start server. server will be stopped on computer shutdown/restart
`brew services start mysql` - have background service keep service on so you dont have to manually restart it
`mysqladmin -u root&nbsp;password yourpassword` - optional, sets password
`mysql -u root` - open mysql shell

## Shell commands

`CREATE DATABASE <dbname> CHARACTER SET utf8;`
`SHOW DATABASES;`
`USE <db>;`
`SHOW TABLES;`
`DESCRIBE <table>;`
`DROP DATABASE`

## For Django

will need to `pip install mysqlclient`
set database details in settings.py
once db created run `python manage.py makemigrations` followed by `python manage.py migrate` to set up tables

### Nuking your database
I'm sure there are ways to avoid this. It's the database equivalent of deleting a git repository and recloning because you don't want to deal with merging conflicts lol. But because of the small size of our project it's often the easiest way:

1. Enter the Mysql command line tool by entering 'mysql -u root' in your command line (will be different if you used a password for your account)

2) now that you're in the mysql command line: `drop database <db>;` to delete the db

3) now recreate the database: `create database <db>`
4) `exit` to quit the mysql command line
5) now go to RipeSportsApp fodler, which should have a migrations folder within it
6) `rm 0*` to delete all migration files but keep the init file in there
7) with a clean database and no records of migrations, you can recreate your database according to your django model schema
8) `python manage.py makemigrations`
9) `python manage.py migrate`
10) good to go. rerun the scraper to reload the renewed database.

