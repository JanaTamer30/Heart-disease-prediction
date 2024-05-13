
import streamlit as st
import pickle
import pandas as pd


st.title('Heart disease prediction app')
st.info('Application for Heart disease prediction ')
st.sidebar.header('Feature Selection')


Age=st.text_input('age')
Sex=st.text_input('sex')
Chest_pain_type=st.text_input('cp')
Resting_blood_pressure =st.text_input('trestbps')
Serum_cholesterol_level =st.text_input('chol')
Fasting_blood_sugar =st.text_input('fbs')
Resting_electrocardiographic_results =st.text_input('restecg')
Maximum_heart_rate_achieved =st.text_input('thalach')
Exercise_induced_angina =st.text_input('exang')
ST_depression_induced_by_exercise_relative_to_rest =st.text_input('oldpeak')
Slope_of_the_peak_exercise_segment =st.text_input('slope')
Number_of_major_vessels_colored_by_fluoroscopy =st.text_input('ca')
Thalassemia_type =st.text_input('thal')


df=pd.DataFrame({'age':[Age],'sex':[Sex],
'cp':[Chest_pain_type], 'trestbps':[Resting_blood_pressure],
'chol':[Serum_cholesterol_level],'fbs':[Fasting_blood_sugar],'restecg':[Resting_electrocardiographic_results],
'thalach':[Maximum_heart_rate_achieved ],'exang':[Exercise_induced_angina],'oldpeak':[ST_depression_induced_by_exercise_relative_to_rest],'slope':[Slope_of_the_peak_exercise_segment],'ca':[Number_of_major_vessels_colored_by_fluoroscopy],
'thal':[Thalassemia_type]},index=[0])

model=pickle.load(open(r'C:\Users\ASUS\Downloads\Heart disease.sav','rb'))

Con=st.sidebar.button('confirm')
if Con:
    result=model.predict(df)
    st.write(result)
