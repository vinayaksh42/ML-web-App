"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request
from FlaskWebProject1 import app
# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Importing the dataset
def machine_model(train_data,test_data):
    dataset = pd.read_csv(train_data)
    X_train = dataset.iloc[:, [2, 3]].values
    y_train = dataset.iloc[:, 4].values

    dataset_test= pd.read_csv(test_data)
    X_test = dataset.iloc[:, [2, 3]].values
    y_test = dataset.iloc[:, 4].values

    # Feature Scaling
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Fitting Naive Bayes to the Training set
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Making the Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    
    total=cm[0][0]+cm[0][0]
    wrong=cm[0][1]+cm[1][0]
    return (((total-wrong)/total)*100)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact', methods = ['POST'])  
def contact():  
    if request.method == 'POST':  
        global f
        f = request.files['file']  
        f.save(f.filename)  
        training_data=f.filename
        return render_template('contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.', name = f.filename)  

@app.route('/contact1', methods = ['POST'])  
def contact1():  
    if request.method == 'POST':  
        x = request.files['file1']  
        x.save(x.filename)
        test_data=x.filename
        train_data=f.filename
        result=machine_model(train_data,test_data)
        return render_template('contact1.html',
        title='Contact1',
        year=datetime.now().year,
        message='Your contact page.', name = x.filename,results=result)  
