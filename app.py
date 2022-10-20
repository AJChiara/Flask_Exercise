from datetime import date
from unicodedata import name
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails = "North Carolina"
studentOrganisationDetails = "New York"
studentOrganisationDetails = "South Carolina"
studentOrganisationDetails = "California"
studentOrganisationDetails = "Florida"

@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = datetime.datetime.now()
    print(currentDate)
    return render_template('index.html', currentDate=currentDate)
    


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')
    

@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    global result
    number = request.form['number']
    if(int(number) % 2) == 0:
        result = "Number is even"
    elif (int(number) % 2) != 0:
        result = "Number is odd"
    return render_template('result.html', num=number, result=result)
    # Write your to code here to check whether number is even or odd and render result.html page


@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')
    pass


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    studentName = request.form['organisation']
    # Append this value to studentOrganisationDetails
    
    # Display studentDetails.html with all students and organisations
    return render_template('studentDetails.html')