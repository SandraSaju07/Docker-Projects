# Import required libraries
import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Read saved model
with open('./model/classifier.pkl','rb') as pickle_in:
    clf = pickle.load(pickle_in)

# Predic Function
def predict(variance,skewness,curtosis,entropy):
    return clf.predict([[variance,skewness,curtosis,entropy]])

def main():
    st.title("Bank Authenticator")

    html_temp = """
    <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">
        Bank Authenticator App
        </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("Skewness","Type Here")
    curtosis = st.text_input("Curtosis","Type Here")
    entropy = st.text_input("Entropy","Type Here")

    result = ""

    if st.button("Predict"):
        result = predict(variance,skewness,curtosis,entropy)
    
    st.success("The output is {}".format(result))

    if st.button("About"):
        st.text("Let's Learn")
        st.text("Build with Streamlit")

if __name__ == "__main__":
    main()