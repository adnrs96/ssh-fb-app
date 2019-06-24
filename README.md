# Social SweetHearts Assignment

Deauth functionality is missing since I have ran out of time. Though its quite easy to implement I guess just parsing the response from the the facebook and figuring out the user id to be marked inactive.

# Build Instructions.

You can do this with or without a venv but I am gonna try include usage of a venv in the instructions.

* Make sure you have python 3.6 installed.
* `pip3 install virtualenv`
* Extract the project zip I sent you and open up a terminal to the project folder location.
*  `virtualenv ssh-venv` This will create a virtual env.
*  `source ssh-venv/bin/activate`
*  `pip install -r requirements.txt`
* Migrate the database using `python manage.py migrate`.

We will also need to add specify environment variables for the app to run.
Here is the list of all the environment variables that need to be created.
I used environement variables instead of a secrets file due to possible ease in deploying with heroku.
```
SECRET_KEY = <specify key that django should use for making hashes>
FACEBOOK_APP_ID = <create a facebook app and add the app id here>
FACEBOOK_APP_SECRET = <add the app secret of the above facebook app here>
```

There is another variable called `PRODUCTION` which we will not be setting since I wasn't able to make it to the end of the assignment and you will have to probably try out the app in DEVELOPMENT mode only.

To start a web server run `python manage.py runserver`. A web server will start up at `localhost:8000`.

# Code Documentation.

So code is basically a standard Django app with standard places to find things.
Once you have setup the django app properly it should not give much issues with the straight forward execution at least.

There are various endpoints in the code:

`''`: This represents home or the login page.
`login/`: This handles making the initial redirec request to the facebook oauth.
`postlogin/`: This handles requests once they have been accepted or rejected at the facebook login dialog and proceeds accordingly.
'logout/': This logs users out of local session from the django app.

`/uploads/`: This acts as the media root for the profile pictrue requests.
