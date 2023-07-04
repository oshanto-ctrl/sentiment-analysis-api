Project: Sentiment Analysis API

Project Folder Structure:
------------------------------
Folder name: sentiment_analysis_api
Subfolder and files: 

-static
    - css
    | styles.css

-templates
    | home.html

app.py

read_me.txt

Instruction to run the project locally (with steps):
------------------------------------------------------
Open a command prompt and change your directory 
to the project directory.

# step 1: 
Set up an virutal environment (venv)

>>> python -m venv venv

You can change the name of your venv as you like.

# step 2:
Activate the created virtual environment.

>>> venv/Scripts/activate.bat 

This is for windows sytem.
For linux/mac

>>> source venv/bin/activate

# step 3:
After installing flask. Install transformers.

>>> pip install transformers

# step 4:
Install torch in project directory.

>>> pip install flask torch

# step 5:
Now, after the convenient codes are written in app.py file
set the flask app by writing following command.

>>> set FLASK_APP=app.py

If the file name changes, modify the 'app.py' name
with changed name of file.

# step 6:
Now, run the flask app by following command.

>>> flask run

Now open up the browser and write http://127.0.0.1:5000
you can modify your port number.
Open your app.py file 
go to app.run() section.
then set up like 
- app.run(debug=True, port=8080)
Then you will need to write in browser: http://127.0.0.1:8080

After all that. If you want to operate that program again
using your comand prompt
follow (step 2), and (step 6). 


Thank you.
- Md. Rejoan Siddiky.
siddikyrejoan@gmail.com













