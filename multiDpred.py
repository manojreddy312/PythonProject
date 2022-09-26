import pickle 
import streamlit as st
st.set_page_config(layout="wide")
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd

# loading the saved models

diabetes_model = pickle.load(open('DiabP_model.sav','rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))


#sidebar for navigate 

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
    ['Diabetes Prediction','Heart Disease Prediction'],
    icons = ['gender-female','activity'],
    default_index=0)

if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction Using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input(label='Age',format='%i',step=1)
    with col2:
        sex = st.number_input('Sex',format='%i',step=1)
    with col3:
        cp = st.number_input('Chest Pain value',format='%i',step=1)
    with col1:
        trestbps = st.number_input('Resting BloodPressure',format='%i',step=1)
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl',format='%i',step=1)
    with col3:
        fbs = st.number_input('Fasting Blood Sugar',format='%i',step=1)
    with col1:
        restecg = st.number_input('Resting ECG results',format='%i',step=1)
    with col2:
        thalach = st.number_input('Max Heart Rate achieved',format='%i',step=1)
    with col3:
        exang = st.number_input('Exercise induced Angina',format='%i',step=1)
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise ',format='%f')
    with col2:
        slope = st.number_input('Slope of peak exercise ST segment',format='%i',step=1)
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy',format='%i',step=1)
    with col1:
        thal = st.number_input('Thal value',format='%i',step=1)

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

elif(selected == 'Diabetes Prediction'):
    st.title('Gestational Diabetes Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input(label='Pregnancy Count',format='%i',step=1)
    with col2:
        Glucose = st.number_input('Glucose Level',format='%i',step=1)
    with col3:
        BloodPressure = st.number_input('BloodPressure value',format='%i',step=1)
    with col1:
        SkinThickness = st.number_input('SkinThickness value',format='%i',step=1)
    with col2:
        Insulin = st.number_input('Insulin Level',format='%i',step=1)
    with col3:
        BMI = st.number_input('BMI value',format='%i',step=1)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function',format='%i',step=1)
    with col2:
        Age = st.number_input('Age of the Person',format='%i',step=1)
    
    diab_status = ''

    #creating a button for prediction

    if st.button('Diabetic test result'):
        diab_pred = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,
        Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if(diab_pred[0]==0):
            diab_status = 'Person is not Diabetic'
        else:
            diab_status = 'Person is Diabetic'

        st.success(diab_status)
