## E2E UI Selenium tests
    Run all commands from source code root directory

## Simple commands to install virtual environment, required python libraries and run all tests
    Install python 3.10.6
    pip install virtualenv
    virtualenv venv
    .\venv\Scripts\activate.bat
    pip install -r requirements.txt
    pytest tests -v

## Install Python version 3.10.6
    https://www.python.org/downloads/

## Install virtual environment:
    pip install virtualenv
## harcnel Mherin
    pip3 install virtualenv 

## Create and Activate virtual environment:
    virtualenv venv

## For Deactivate virtual environment run following command:
    deactivate

## For Activate virtual environment:
### Windows: 
    .\venv\Scripts\activate.bat


## Install all required libraries from requirements.txt:
### Windows: 
    pip install -r requirements.txt


## To get and save to file all required libraries from pip:
    pip freeze -> requirements.txt

## Install all required libraries manually:
    pip install selenium
    pip install webdriver_manager
    pip install pytest
    pip install flake8
## harcnel Mherin
    pip install allure-pytest

## harcnel Mherin
## Install allure
### Windows:
    1. Open PowerShell as admin user 
    2. Run follwowing commands
        Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
        Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
        Scoop install allure


### Environment variables on Mac:
#### List All Environment Variables:
    printenv

#### Set env variable:     
    export [variable_name]='variable_value'

#### Check A Specific Environment Variable:
    echo $[variable name]

## Run tests: From 'tests' dir run following commands

### To run all test (on default browser, chrome and firefox):
        pytest -v
        pytest -vs --browser chrome
        pytest -vs --browser firefox
        pytest -k file name

### Run one test
    pytest tests/{{test_file}}.py::{{TestClass}}::{{test_method}}

### To run only smoke tests
        pytest -v -m smoke

### To run regression tests
        pytest -v -m regression

### To rerun failed tests for example. 2 times use the following:
        pytest -reruns 2

### To skip test case: add following decorator on test function
        @pytest.mark.skip("Some reason")

#### Run tests with allure report:
    pytest -vs tests --browser chrome --alluredir=allure-results

#### Generate allure result:
    cd /path_where_allure-results_are_generated
    allure serve allure-results

### Parallel run with 2 or more threads:
        pytest tests -n 2

### Run linters before opening PR.
        flake8
