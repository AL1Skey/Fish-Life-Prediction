import streamlit as st
import pandas as pd
import joblib
import json

st.set_page_config(
    page_title="Fish Life Prediction Showcase Model"
)
#Data Loading
df = pd.read_csv('Realtime-env2.csv')
model = joblib.load('model.pkl')
feature = json.load(open('feature.json','r'))

# Title
st.header("Fish Life Prediction")

#DataFrame
st.header("DataFrame")
df.head()

def user_input():
    inputter={}
    for i in feature:
        inputter[i] = st.sidebar.slider(i,df.i.min(),df.i.max())
    inputter = pd.DataFrame([inputter])
    return inputter

input = user_input()