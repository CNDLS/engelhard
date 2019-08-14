# Engelhard

* **Live Site URL** - http://engelhard.georgetown.edu/
* **Host Server** - CNDLS Georgetown Domains account (cndls@georgetown.edu)
* **Site Root on Server** - /public_html/hosted-sites/engelhard.georgetown.edu
* **GitHub Repository** - https://github.com/CNDLS/engelhard


## Installation

### Getting Access to the Git Repository
The code for this site is stored in a repository on CNDLS GitHub account. To be able to access the repository, follow these steps:
* Create a GitHub account at https://github.com.
* Get a CNDLS web administrator/developer to add your GitHub account as a contributor to the engelhard repository. Once you are added, you should receive an email from GitHub asking you to confirm that you have been given access to the repository. Please follow the email's instructions and confirm.
* Install GitKraken, which is a GUI for Git: https://www.gitkraken.com/
* Once GitKraken is downloaded and installed, log into it using your GitHub credentials.
* You may be prompted to install the XCode command line developer tools. If so, go ahead.
* We will use GitKraken to clone (make a local copy of) the repository on GitHub.
* In GitKraken, click on the the folder icon in the top left corner to open the Repository Management window.
* In the Repository Management window, click Clone on the left sidebar.
* Select the Clone with URL option.
* Under "Where to clone to", choose a suitable folder on your machine. For me, this is /Users/brianblosser/Sites.
* Next, switch to your browser and go to the projects GitHub repo URL (see above).
* Click the green button on the right "Clone or download".
* If the resulting dialog box says "Clone with SSH", click the link in the top right corner of the dialog box which says "Use HTTPS", which should change the dialog box heading to "Clone with HTTPS".
* Copy the link in the dialog box (should be https://github.com/CNDLS/engelhard.git).
* Switch back to GitKraken, and paste the link into the URL field.
* Click the button "Clone the repo!". This should create a copy of the repo on your computer in the folder you specified.

### Installing Python
This site uses Python as it's server-side language. You can use the latest version of Python (3.x.x)
To check the version of Python that is installed on your computer, do the following:
* Open a Terminal window. In Mac OS, use the Terminal application, which can be found in /Applications/Utilities/Terminal, or by opening spotlight with `Cmd+Space` and typing `Terminal`.
* In the Terminal window, type the following command, followed by Return (henceforth, if you see a terminal command, always hit Return at the end of the line):
```
python3 -V
```
* You should see something like this printed out:
```
Python 3.7.2
```
* If you see nothing printed at all, please install version 3.x.x, by visiting the following url: https://www.python.org/downloads/, then clicking on the button 'Download Python 3.x.x', which should download the installer appropriate for your system. Once downloaded, run the installer, and retry the test above to make sure Python was successfully installed.

### Creating a Virtual Environment in the Project
* It's good practice to use "virtual environments" in Python which encapsulate the Python interpreter and any Python packages that you use for the project. I usually do this in a directory called `.venv` in the project root directory. Type the following commands in a Terminal window:
* Navigate to the project root: `cd /path/to/engelhard`
* If using Python 3, the command to install a virtual environment is: `python3 -m venv <NAME_OF_ENV>`
* Once the virtual environment is created, you must activate it so that any Python packages for the project are installed inside the virtual environment and not globally on your computer: `source <NAME_OF_ENV>/bin/activate`
* If the virtual environment was successfully activated, you should see the name of the virtual environment in parentheses to the left of the your user name on the command prompt, for example: `(.venv) Brians-MacBook-Pro-2:engelhard brianblosser$`
* Now that the virtual environment is activated, you can install the Python modules necessary for the site, and they
will be installed in the site's virtual environment.


### Flask and Associated Plugins

This site was built using Flask. Flask is a web microframework for Python that uses the Jinja2 templating engine. You can read more about Flask and find documentation here:

[http://flask.pocoo.org/](http://flask.pocoo.org/ "Flask documentation")

* Install Flask: ``pip install flask``
* Install Flask-FlatPages: ``pip install flask-flatpages``
* Install Frozen-Flask: ``pip install frozen-flask``

## Running the development server
* Once the site is installed and the virtual environment is activated, from within the project root directory, type: `python engelhard.py`
* This should start the Flask development server, and print out the site url in the terminal window. You should see something like the following:
```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Restarting with stat
Debugger is active!
Debugger PIN: 321-214-230
```
* Copy the URL and paste it into your browser's address bar to view the site.
* Optional: Add an alias to your `~/.bash_profile` file that will let you just type `engelhard` at the prompt, to save yourself form having to repeat all the steps everytime you want to run the site:
  * In Terminal, type nano ~/.bash_profile to open up that file in the Nano editor.
  * Pasted the below line in the bottom of the file.
  ```
  alias engelhard="cd ~/Sites/engelhard; source .venv/bin/activate; python3 engelhard.py"
  ```
  * Press Ctl+X to write the changes to disk.
  * Then close and reopen Terminal (also called the shell).
  * Now you should be able to type `engelhard` and hit enter, and it will start the development server for you.

## Workflow When Non-developer Updates Site
* The editor edits the Jinja2 template, verifies that the changes look good on her local development environment, then commits those changes to Git and pushes the commits to "origin" (GitHub).
* The developer pulls the changes, compiles the static files, then uses FTP to transmit the changed files.
* The developer can alternatively use the provided shell script located in ./deploy-scripts/deploy.sh. The script requires a config.sh file (not version-controlled) to enter some of the required variables.

## Compiling the Site As A Static Site
* The plugin frozen-flask allows you to compile the dyamic Flask site to a static site (converting the Python templates to HTML). To compile to a static site, run the following:
```
python3 freeze.py
```
* This will create a directory called "build" in the project root, which will contain html files. The HTML files will still reference the "static" project folder.
* It is SUPER IMPORTANT TO USE THE JINJA2 TEMPLATE FUNCTION `url_for()` IN THE PAGE TEMPLATES. This is because Frozen Flask looks for all internal pages that are linked to using the `url_for()` function, and only compiles these pages (from what I can tell). It's also just a good idea to use `url_for()` for your internal links for the portability of the site from one domain to the next, so please use it!

