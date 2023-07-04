# Sentiment Analysis API

## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Project Folder Structure](#project-folder-structure)
* [Installation](#installation)

## Introduction
Building a backend service that exposes a RESTful API endpoint for sentiment analysis. 
The API will accept text input and return the sentiment analysis result using a pre-trained model
Implemented a web server using Python web framework Flask. Created a single endpoint
/analyze that accepts POST requests. Text of user input “Text to be analyzed” for sentiment
analysis performed by using a pre-trained machine learning model form Hugging Face
Transformers Library.
Then the sentiment analysis returns a JSON response a results with structure

{
‘sentiment’: “Positive/Negative/Neutral”
}

## Technologies
Project is created with:
* Python version: 3.10.6
* Flask Framework version: 2.2.2
* HuggingFace Sentiment analysis model (pre-trained): https://huggingface.co/StatsGary/setfit-ft-sentinent-eval
* HTML5
* CSS3

## Project Folder Structure
Folder name: sentiment_analysis_api
Subfolder and files: 

-static
    - css
    | styles.css

-templates
    | home.html

app.py

## Installation
### Instruction to run the project locally (with steps):
------------------------------------------------------
Open a command prompt and change your directory 
to the project directory.

#### step 1: 
Set up an virutal environment (venv)

>>> python -m venv venv

You can change the name of your venv as you like.

#### step 2:
Activate the created virtual environment.

>>> venv/Scripts/activate.bat 

This is for windows sytem.
For linux/mac

>>> source venv/bin/activate

#### step 3:
After installing flask. Install transformers.

>>> pip install transformers

#### step 4:
Install torch in project directory.

>>> pip install flask torch

#### step 5:
Now, after the convenient codes are written in app.py file
set the flask app by writing following command.

>>> set FLASK_APP=app.py

If the file name changes, modify the 'app.py' name
with changed name of file.

#### step 6:
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


Thank you. :)


