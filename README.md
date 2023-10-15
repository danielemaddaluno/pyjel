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
You can test locally: 
 - with a WSGI running:
   ```bash
   gunicorn wsgi:application
   ```
 - otherwise with a ASGI running (bypassing the WSGI):
   ```bash
   uvicorn app.app:app
   ```
   or running
   ```bash
   python app/app.py
   ```
   or directly from the IDE running the `app.py` file.