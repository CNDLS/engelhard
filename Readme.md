# Engelhard

* **Live Site URL** - http://engelhard.georgetown.edu/
* **Host Server** - To fill in
* **GitHub Repository** - https://github.com/CNDLS/engelhard


## Installation

### Installing Python
This site uses Python as it's server-side language. The version it uses is Python 2.7x.
To check the version of Python that is installed on your computer, do the following:
* Open a Terminal window. In Mac OS, use the Terminal application, which can be found in /Applications/Utilities/Terminal, or by opening spotlight with `Cmd+Space` and typing `Terminal`.
* In the Terminal window, type the following command, followed by Return (henceforth, if you see a terminal command, always hit Return at the end of the line):
```
python -V
```
* You should see something like this printed out:
```
Python 2.7.14
```
* If you see a version before 2.7 or nothing printed at all, please install version 2.7, by visiting the following url: https://www.python.org/downloads/, then clicking on the button 'Download Python 2.7.14', which should download the installer appropriate for your system. Once downloaded, run the installer, and retry the test above to make sure Python was successfully installed.

### Getting Access to the Git Repository
The code for this site is stored in a repository on CNDLS GitHub account. To be able to access the repository, follow these steps:
* Create a GitHub account at https://github.com.
* Get a CNDLS web administrator/developer to add your GitHub account as a contributor to the engelhard repository.
* If you have not previously done so, generate a private/public SSH key pair for your computer (this key will allow you to authenticate with the GitHub repository). Detailed instructions are here: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
I recommend not adding a password to your private key to make things easier.
* Add your public key to your GitHub account: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/

### Flask

This site was built using Flask. Flask is a web microframework for Python that uses the Jinja2 templating engine. You can read more about Flask and find documentation here:

[http://flask.pocoo.org/](http://flask.pocoo.org/ "Flask documentation")

* First, you'll need to set up a Python virtual environment. I usually do this in a directory called ``.src`` in my home directory.
* Alternatively, you can install a virtual environment folder in the repository folder and ignore it, to isolate the virtual environments from each other, e.g. in /Sites/itel/, you have a /Sites/itel/.venv/ directory which holds your virtual environment information. You can tell Git to ignore this using the .gitignore file.
* Create the virtual environment: ``virtualenv NAME_OF_ENV``
* Activate the virtual environment: ``source NAME_OF_ENV/bin/activate``
* Optional: Add an alias to your ``~/.bash_profile`` file that will let you just type ``NAME_OF_ENV`` at the prompt to activate the virtual environment: ``alias NAME_OF_ENV="source /Users/yourusername/.src/NAME_OF_ENV/bin/activate"`` Then close and reopen your shell. Now you should have the ``NAME_OF_ENV`` command available.

* If using Python 3, the command to install a virtual environment is:
  ```
  python3 -m venv <DIR>
  ```
  * Activation is a follows:
  ```
  source <DIR>/bin/activate
  ```

* Install Flask: ``pip install flask``
* Install Flask-FlatPages: ``pip install flask-flatpages``
* Install Frozen-Flask: ``pip install frozen-flask``

*For the Teaching Commons, you will also need:*
* Install flask-mysql: ``pip install flask-mysql``
* Download the repo


Fonts
------------
In addition to the application files, you will also need to download the following font files ([CNDLS fonts can be found in this Drive directory](https://drive.google.com/a/georgetown.edu/folderview?id=0B-kC8L5SdEE2LTVQZUpMY0RHdDA&usp=sharing#list)) to the project's static/css directory:

* Teaching Commons
  * DINOffcCondMedi
  * DinOffcLight
  * DinOffcMedi



Running the development server
------------------------------
In this example, we'll run a development server for the Teaching Commons which has teaching.py in the project root directory.

* In the project root: ``python teaching.py``
* To create the static build: ``python freeze.py``. This will create a directory called ``build``.
* Upload the build directory to the server & directory where the app is deployed:
  * Teaching Commons site is on lux at  ``/var/www/docroot-ocw/teaching``.
  * Engelhard site is on lux at: ``/var/www/docroot-ocw/engelhard``.
  * ITEL site is on halo at: ``/var/www/hosted/itel.georgetown``.
  
  
Updating the production server
------------------------------
We currently use FTP to update files, which necessitates fixing permissions. Here is how to set perms on nested files and folders:
* `find /path/to/your/dir -type d -exec chmod 775 {} \;`
* `find /path/to/your/dir -type f -exec chmod 664 {} \;`