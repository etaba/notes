# MySQL

## Install

`brew install mysql` - creates mysql server with no password
`mysql.server start`  - start server. server will be stopped on computer shutdown/restart
`brew services start mysql` - have background service keep service on so you dont have to manually restart it
`mysqladmin -u root&nbsp;password yourpassword` - optional, sets password
`mysql -u root` - open mysql shell
for accessing db on a host (for example run this on dreamhost server): `mysql -h eptaba.aeromembers.com -u eptaba -p aeromembersdb`

So that you dont have to use `sudo` every time, create a non root user is recommended:
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';

## Shell commands

`CREATE DATABASE <dbname> CHARACTER SET utf8;`
`SHOW DATABASES;`
`USE <db>;`
`SHOW TABLES;`
`DESCRIBE <table>;`
`DROP DATABASE`
`DELETE FROM <table>` -delete all rows
## For Django

will need to `pip install mysqlclient`
	NOTE: for some python versions this might not work. (2.7.14 for example) Instead, install the `pymysql` module instead. Then, in the `__init__.py` file located in your dango root folder (same folder that contains `settings.py`) add these lines:
	`import pymysql`
	`pymysql.install_as_MySQLdb()`
set database details in settings.py
once db created run `python manage.py makemigrations` followed by `python manage.py migrate` to set up tables

### Nuking your database (django)
I'm sure there are ways to avoid this. It's the database equivalent of deleting a git repository and recloning because you don't want to deal with merging conflicts lol. But because of the small size of our project it's often the easiest way:

1) Enter the Mysql command line tool by entering 'mysql -u root' in your command line (will be different if you used a password for your account)

2) now that you're in the mysql command line: `drop database <db>;` to delete the db

3) now recreate the database: `create database <db>`
4) `exit` to quit the mysql command line
5) now go to RipeSportsApp fodler, which should have a migrations folder within it
6) Delete all automatically created migration files. But if you made any custom migrations, such as to seed or initialize data, keep those. `rm 0*` should delete all auto created migration files unless custom ones were named that way. Also keep the init file in there
7) with a clean database and no records of migrations, you can recreate your database according to your django model schema
8) `python manage.py makemigrations`
9) if you had custom migrations, at this point you may have to edit its dependencies list to use the migration file just created.
10) `python manage.py migrate`
11) good to go. rerun the scraper to reload the renewed database.

