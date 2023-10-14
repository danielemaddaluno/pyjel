# pyjel
Apachepython basic webapp for Jelastic with ASGI

## Setup

1. Create a new Python environment on Jelastic, select a jelastic `apachepython` container, it's suggested to select the container `2.4.57-python-3.9.18` (other containers may not work)

2. Under `Deployments`, `Deploy from GIT / SVN` paste `https://github.com/danielemaddaluno/pyjel.git`, select `Check and auto-deploy updates` 

3. Then click on `Hooks` and then on `Post` and add this text:
   ```bash
   # run the setup script that will add all the required dependencies to the virtual env
   sh ./ROOT/setup.sh
   ```
   This will run the setup script that will add all the required dependencies to the virtual env.
   
   If something goes wrong, for debug purposes you could use something more complex, like this:
   ```bash
   pwd > /var/www/webroot/pwd.txt
   
   # move inside webroot folder
   cd /var/www/webroot
   
   # run the setup script that will add all the required dependencies to the virtual env
   sh ./ROOT/setup.sh
   ```

5. Click `Deploy`
