Moving to Production

#Add hosting to dreamhost

Basically go to 'manage domains' and select 'add hosting'. Select or create a user for the domain and note that this is the user which will be able to ssh and make changes to the server files. 
-Make sure 'passenger' box is checked, this will be used to enable python

#(Optional) add rsa key to host's trusted for easy logging in:
You may need to generate a new ssh key; if so, follow instructions to generate ssh key
`ssh-keygen -t rsa`
add authorized keys to dreamhost:
`cat ~/.ssh/id_rsa.pub | ssh [user]@[host] "mkdir ~/.ssh; cat >> ~/.ssh/authorized_keys"`
Note: you may need to modify permissions for the .ssh folder and authorized_keys file on the server:
`chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys`


#Create virtualenv 
-ssh user@yourdomain.com to start a session. from there cd into the domain itself.
-create virtualenv with appropriate python version: `virtualenv myEnv` or `virtualenv -p /path/to/python myEnv` if you need to specify a different python version
-this environment will be linked to the server through the passenger_wsgi.py file later

#Git 
-clone your repo into the domain directory

#git hook
There should already be a sample post-receive hook script in the server .git/hooks directory. Remove the .sample extension to enable it.
Then just add the server's repo as a remote repository on the local machine from which you want to update it:
`remote add production ssh://eptaba@aeromembers.com/~/aeromembers.com/AeroMembers/.git`
Now you can push updates directly there like so:
`git push production <branch>`

#passenger_wsgi.py
should look something like this:

import sys, os
from django.core.wsgi import get_wsgi_application


DOMAIN_ROOT = "home/eptaba/aeromembers.com/"
VENV = os.path.join(DOMAIN_ROOT,'AeroMembers_env')
INTERP = os.path.join(VENV,'bin','python3')
\#INTERP is present twice so that the new python interpreter knows the actual executable path 
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
sys.path.insert(0,os.path.join(VENV,'lib','python3.4','site-packages'))
os.environ['DJANGO_SETTINGS_MODULE'] = "AeroMembers.settings"
application = get_wsgi_application()

-note that the project is specified as well as the virtualenv python binary and sitepackages location

#static directory
-create directory called 'static' in the domains public directory. This will match the `STATIC_ROOT` you'll define later in your production settings.py

#mysql
-for dreamhost in the domain manager go to 'goodies>mysql database'
-set it up and note the host, user, password, you will en

#Production settings.py

- `ALLOWED_HOSTS` needs the actual websites. ie ['aeromembers.com','www.aeromembers.com']

- `SECRET_KEY` should be regenerated and stored as an environment variable on the server. Can then be called with `os.environ.get('AEROMEMBERS_SECRET_KEY')`
- note key environment variable must be set in server .bash_profile 

- `DEBUG` set to False

- `STATIC_ROOT`must be updated to reflect static file location on server. For dreamhost: os.path.dirname(BASE_DIR) + '/public/static/'

- line can be added at the bottom to override the production settings if an environment variable indicating development is set:
if os.environ.get('DJANGO_DEVELOPMENT') is not None:
    from settings_dev import *
This way original dev settings.py can be saved and renamed as settings_dev.py

#custom python version
[server]$ cd ~
[server]$ mkdir tmp
[server]$ cd tmp
[server]$ wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
[server]$ tar zxvf Python-3.6.2.tgz 
[server]$ cd Python-3.6.2 
[server]$ ./configure --prefix=$HOME/opt/python-3.6.2
[server]$ make
[server]$ make install

then add this to ~/.bash_profile:
export PATH=$HOME/opt/python-3.6.2/bin:$PATH

