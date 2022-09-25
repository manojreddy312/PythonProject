import pickle 
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/Manoj Reddy/Desktop/pythonProject/saved models/heart_disease_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/Manoj Reddy/Desktop/pythonProject/saved models/heart_disease_model.sav','rb'))


#sidebar for navigate 

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
    ['Diabetes Prediction','Heart Disease Prediction'],
    icons = ['heart','activity'],
    default_index=1)

if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    

    age = st.number_input(label='Enter Age',format='%i',step=1)
    sex = st.number_input('Enter sex',format='%i',step=1)
    cp = st.number_input('Enter chest pain value',format='%i',step=1)
    trestbps = st.number_input('Enter trestbps',format='%i',step=1)
    chol = st.number_input('Enter chol',format='%i',step=1)
    fbs = st.number_input('Enter fbs',format='%i',step=1)
    restecg = st.number_input('Enter restecg',format='%i',step=1)
    thalach = st.number_input('Enter thalach',format='%i',step=1)
    exang = st.number_input('Enter exang',format='%i',step=1)
    oldpeak = st.number_input('Enter oldpeak',format='%f')
    slope = st.number_input('Enter slope',format='%i',step=1)
    ca = st.number_input('Enter ca',format='%i',step=1)
    thal = st.number_input('Enter thal',format='%i',step=1)
    heart_status = ''

    #creating a button for prediction

    if st.button('Heart test result'):
        heart_pred = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
        exang,oldpeak,slope,ca,thal]])

        if(heart_pred[0]==0):
            heart_status = 'Person doesnt has Heart Disease'
        else:
            heart_status = 'Person has Heart Disease'

        st.success(heart_status)
