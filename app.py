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
st.image('fish.jpg')
#DataFrame
st.header("DataFrame")
st.write(df.head())

def user_input():
    inputter={}
    for i in feature:
        inputter[i] = st.sidebar.slider(i,df[i].min(),df[i].max())
    inputter = pd.DataFrame([inputter])
    return inputter

input = user_input()

#Input Section
st.subheader("Input")
st.write(input)

if st.button('predict'):
    prediction = model.predict(input)
    
    if prediction == 1:
        prediction = 'Fish Can life in this water environment'
    else:
        prediction = 'Fish Can\'t life in this water environment'
    
    st.header(prediction)