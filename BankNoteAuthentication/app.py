# Import required libraries
from flask import Flask,request
import pandas as pd 
import numpy as np
import pickle

# Initialize flask
app = Flask(__name__)

# Read trained model
with open('./model/classifier.pkl','rb') as pickle_in:
    clf = pickle.load(pickle_in)

# Function for home page
@app.route('/')
def welcome():
    return "Welcome Everyone!!"    

# Function for prediction using single input
@app.route('/predict')
def predict():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = clf.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is " + str(prediction)

# Function for prediction using test file
@app.route('/predict_file',methods=['POST'])
def predict_file():
    df = pd.read_csv(request.files.get('file'))
    prediction = clf.predict(df)
    return "The predicted values for the CSV is " + str(list(prediction))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)