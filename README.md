# aruba-ldmckeen-ap-scan

## Aruba AP Scan
This repository contains the codebase for a production ready, maintainable, testable service that accepts Wi-Fi access point (AP) scan result data and returns the latitude and longitude of the location at which the AP scan was performed.

## Tech Stack Details
Following is a full comprehensive list of all the requirements to use and setup this
application accordingly.
### Pre-requisites
When setting up a local environment for developing ensure you are using a local
virtual environment for optimal sand-boxing and testing to minimize clashes with
existing setups or environments on your machine.

####Virtual Environment Setup
######Pyenv
(Recommendation: Use Pyenv where possible to manage your python installations)

Useful pyenv commands:<br>
`pyenv install --list` - List all pyenv versions on offer<br>
`pyenv versions` - List pyenv versions on your machine<br>
`pyenv install <python version>` - Install python version eg. pyenv install 3.8.7<br>
`pyenv virtualenvs` - List virtualenv versions<br>
`pyenv virtualenv <python version> <venv-name>` - Create Pyenv Virtual Environment<br>
`pyenv activate <name>` - Activate Virtual Environment<br>
`pyenv deactivate`<br>-<br>Exit Virtual Environment<br>
`pyenv virtualenv-delete <venv-name>` - Delete Virtual Environment<br>

To note (On Mac):<br>
Make sure to add the envs to your bash or zsh profiles (.zshrc/.zprofile, .bashrc):<br>
`export PYENV_ROOT="$HOME/.pyenv"`<br>
`export PATH="$PYENV_ROOT/bin:$PATH"`<br>
`eval "$(pyenv init --path)"`<br>
`eval "$(pyenv init -)"`

###### Standalone virtualenv
`python3 -m pip install --user virtualenv`<br>
`python3 -m venv env`<br>
`source ./env/bin/activate`

##### Resources
https://github.com/pyenv/pyenv<br>
https://github.com/pyenv/pyenv-virtualenv<br>
*Tutorial* - https://realpython.com/intro-to-pyenv/

### Python Version
This application makes use of Python 3.8.7<br>
Please ensure you have the correct Python version installed.

### Git Config
In order to ensure that your local git structure mirrors that of the broader style
requirements, you must setup the use of git hooks. This is done via the `pre-commit`
application. If on a Mac, ensure you `brew install pre-commit` (Sometimes you need: `xcode-select --install`)

Run the following configuration in your local repo instance:<br>
`git config core.hooksPath .githooks`

Make sure all the dev requirements are installed by running:<br>
`pip install -r dev-requirements.txt`

Make sure all the application requirements are installed by running:<br>
`pip install -r requirements.txt`

Configure pre-commit
`pre-commit install`

###### Troubleshooting
* Pip - If you're Pip issues not installing packages correctly please take note you may need to upgrade your pip installation:
`pip install --upgrade pip`

###### Common git commands when pushing to repo :*<br>
* Checkout to new branch:
<br>* `git checkout -b "feature/<ticket-id>-<short-descriptor>"`
<br>* eg. `git checkout -b feature/SPAN-101-new-feature`
* Set upstream branch:
<br>* `git push --set-upstream origin feature/SPAN-101-new-feature`
*Stage all changed files in current directory for commit:
<br>* `git add .`
* Check status of current branch:
<br>* `git status`
* Commit changes:
<br>* `git commit -m "<descriptive-message>"`

*Git Tutorials*:
`https://guides.github.com/activities/hello-world/`

###Environment Variables:
This project makes use of environment variables.
Ensure you have a .env file in your root directory, mimic the .env.template file.
If using passwords or tokens store the passwords and secrets in a vault in the cloud
and reference the value from there in your builds
Also always backup these values on a web application such as lastpass or 1password
(Or any Web Password manager of your choice)<br>
https://www.lastpass.com/<br>
https://1password.com/

## Running the Python Application
### Usage
### Django Rest Framework
This application makes use of python and the Django Rest Framework.
To run the application:
`python manage.py runserver <port-number (defaults to 8000)>`
Migrate models to DB (If you want to make use of Object specific APScan data endpoints)
`python manage.py migrate`

### Making an API call
The apscan endpoint takes a zipfile as input and calls the Google’s geolocation API to
return the geolocation of the sensor from the apscan data list.


Reference: https://developers.google.com/maps/documentation/geolocation/overview

Login:
`admin@arubaapscan.com`
Password:
`Arubaapscan_1234`

The Aruba Index Python file (span_index.py) is the entrypoint for this application.<br>

Run this python file from your virtual environment (or hosted server with python installed)
with the python commands below:<br>
* For use with a file input:
<br>* `python aruba_ap.py`
<br>* i.e Sample Files to test are stored in ./sample_input
* For use with a command line input as comma and newline seperated text
<br>* `python aruba_ap.py`

#### Environment Variables
As mentioned above please make sure to add your own Environment Variable file with the
necessary Variables i.e .env
(see .env.template for an example of the env variables used)

To Note:<br>
Application code resides in the application folder and
testing code resides in the tests folder

### Unit Testing
This Application make use of the Pytest unit testing Library.<br>
To run the unit tests you can use the single command:<br>
`pytest` from the root directory of the repo.

For more information and resources on Pytest please see Pytest docs:
https://docs.pytest.org/en/7.2.x/
### Program Inputs and Outputs
* #### Input (Subset of Data in Sample Files Directory)<br>

* #### Output
