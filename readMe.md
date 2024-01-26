This project was started to help a friend keep tabs on a really important email that's time sensitive.
The code repeatedly checks gmail for a specific email, once it's detected it sends an sms notification. This' where Twilio comes in.
Project will be expanded to better visualize email data.
Starting code was forked from "thepythoncode.com/article/use-gmail-api-in-python". Use this link as a resource for setting up and connection to the gmail api.
Sign up for an account with free starting credit at "twilio.com" and setup their api
Note: I am not affiliated with twilio or google.
"thepythoncode.com" and "Bala Iganus" must be cited when forking this code.
Created by Bala Iganus.

Authenticate with google and download google token file, rename to "credentials.json". Add credentials.json file to working dir.

0. Create and activate virtual environment for the project. Note -> this is for a windows environment, linux and mac will vary slightly.
    - Navigate to project working directory on terminal
    $ "path\to\python3\installation\without\the\outside\quotes\" -m venv chosenVenvName
    $ chosenVenvName\Scripts\activate.bat

1. Run the following commands to install dependencies
    pip3 install -r requirements.txt

2. Populate config.cfg file

3. Run using command 
    $ py main.py configFileName 

If you run into problems with the google authorization after verification, delete the token.pickle file and re-run / re-authorize the app