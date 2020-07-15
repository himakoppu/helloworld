# A basic “Hello World” API

## Download application
Clone the Hello World application from the GitHub repository into a working directory.

```
    $ cd ~/Desktop
    $ mkdir helloworld    
    $ cd helloworld
    $ git clone -b master https://github.com/himakoppu/helloworld.git 
    $ cd helloworld_project
```

## Application Installation 

### Install initial python dependencies
Skip this step if you already have Python 3 and virtualenv on your machine.

##### For Linux users: 
Run below commands, use 'sudo' as required. 
```
    $ sudo apt update
    $ sudo apt install python3-dev python3-pip python3-virtualenv
```
##### For Mac users:
- Install Homebrew using [Install Homebrew]
- Install Python 3
```
    $ brew install python3
    $ python3 --version
    Python 3.7.5
```   
- Install virtualenv via pip
```
    $ pip install virtualenv
    $ virtualenv --version
    16.7.7
```
##### For Windows users
- Install Python, Django [Django on Windows]
- Jump to Enable logging step


### Install application requirements
- Create a new python virtual environment
```
    $ virtualenv -p python3 helloworld_venv --no-site-packages
    $ source helloworld_venv/bin/activate
```
- Install all application requirements, use 'sudo' as required


    $ pip install -r requirements.txt
    
- Confirm requirements are installed correctly
```
    $ pip list | grep Django
    Django     3.0.8
``` 


## Enable logging
By default, Hello World application logs of INFO level and higher will be sent to the console. In 
order to change the logging level 
- Go to helloworld_project/settings.py.
- Go to LOGGING section, under 'loggers' key find the 'helloworld' section. 
- Change the 'level' to DEBUG.
- We should see messages like below on the server terminal while accessing the application.
    - 2020-07-12 05:05:19: Received a POST request at URL: http://localhost:8000/
    - 2020-07-12 05:05:28: Received a GET request at URL: http://localhost:8000/

## Start application


    $ python manage.py runserver
    
Go to http://127.0.0.1:8000 in a browser you should see a Hello, World! message.

## Using the application from command line
- Open a new terminal and try out the below examples
- Example GET calls
```
    $ curl http://localhost:8000
    Hello, World
    
    $ curl http://localhost:8000 -H "Accept:"
    <p>Hello, World</p>
    
    $ curl http://localhost:8000 --H "Accept: application/json"
    {"message": "Hello, World"}
```
- Example POST calls
```
    $ curl http://localhost:8000 -d '{"username":"xyz"}'
    Post successful!
    
    $ curl http://localhost:8000 -d ''
    {"error": "Data cannot be empty"}
```
## Testing
- Open a new terminal
```
    $ cd ~/Desktop/helloworld/helloworld_project
    $ source helloworld_venv/bin/activate
```  

###### Note: Unit tests mock the API requests to the server, so they don't need the server to be running. We can stop the server by using Ctrl+C on the server terminal and continue to execute unit tests in the same terminal.

- Execute unit tests
```
    $ python manage.py test 
 ```    

[Install Homebrew]: https://osxdaily.com/2018/03/07/how-install-homebrew-mac-os
[Django on Windows]: https://docs.djangoproject.com/en/3.0/howto/windows