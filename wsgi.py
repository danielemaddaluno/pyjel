import os, sys

dirpath = os.path.dirname(os.path.abspath(__file__))
virtenv = dirpath + '/venv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    if sys.version.split(' ')[0].split('.')[0] == '3':
        exec(compile(open(virtualenv, "rb").read(), virtualenv, 'exec'), dict(__file__=virtualenv))
    else:
        execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

sys.path.append(dirpath)

from app import app
from a2wsgi import ASGIMiddleware
application = ASGIMiddleware(app.app)
