import sys

# pipenv
activate_this = '/var/www/.venv/bin/activate_this.py'
with open(activate_this) as file_:
  exec(file_.read(), dict(__file__=activate_this))

# my application
sys.path.insert(0, '/var/www/app')

import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

from index import app
application = app.server
