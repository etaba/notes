# VirtualEnv

virtualenv -p /path/to/python my_virtual_env
source my_virtual_env/bin/activate
deactivate

# VirtualEnvWrapper

pip install virtualenv
pip install virtualenvwrapper

cd /path/to/myproject

mkvirtualenv myproject
workon myproject
(myproject) pip install stuff
(myproject) pip freeze > requirements.txt
(myproject) pip install -r requirements.txt
(myproject) deactivate
rmvirtualenv myproject

lsvirtualenv #show all virtual envs

for python2.7 env:
mkvirtualenv -p /path/to/python2.7 myproject
use `which python2` to find python2.7 path


