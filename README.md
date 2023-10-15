# pyjel
Apache python basic webapp for Jelastic with ASGI

## Deploy on Jelastic

1. Create a new Python environment on Jelastic, select a jelastic `apachepython` container, it's suggested to select the container `2.4.57-python-3.9.18` or `2.4.57-python-3.11.6` (other containers may not work)

2. Under `Deployments`, `Deploy from GIT / SVN` paste `https://github.com/danielemaddaluno/pyjel.git`, select `Check and auto-deploy updates` 

3. Then click on `Hooks` and then on `Post` and add this text:
   ```bash
   # run the setup script that will add all the required dependencies to the virtual env
   mv ./ROOT/requirements.txt .
   mv ./ROOT/setup.sh .
   sh ./setup.sh
   ```
   This will run the setup script that will add all the required dependencies to the virtual env.
   
   If something goes wrong, for debug purposes you could use something more complex, like this:
   ```bash
   pwd > /var/www/webroot/pwd.txt
   
   cd /var/www/webroot
   
   # run the setup script that will add all the required dependencies to the virtual env
   mv ./ROOT/requirements.txt .
   mv ./ROOT/setup.sh .
   sh ./setup.sh
   ```

5. Click `Deploy`

## Test Locally
To test locally with PyCharm:

1. Click on `Add New Interpreter`, `Add Local Interpreter...`, `Virtualenv Environment`, `New`.

2. Then add requirements with:
   ```bash
   sh ./setup.sh
   ```
   Sometimes a restart of PyCharm is required.

3. Then:
   - to test with a WSGI run:
     ```bash
     gunicorn wsgi:application
     ```
   - to test with a ASGI run (bypassing the WSGI):
     ```bash
     uvicorn app.app:app
     ```
     or
     ```bash
     python app/app.py
     ```
     or run it directly from the IDE launching the `app.py` file.