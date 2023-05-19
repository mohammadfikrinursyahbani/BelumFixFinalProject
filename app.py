import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model_xgb.pkl')

# Define the predict function
def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    data = {'Pregnancies': [Pregnancies],
            'Glucose': [Glucose],
            'BloodPressure': [BloodPressure],
            'SkinThickness': [SkinThickness],
            'Insulin': [Insulin],
            'BMI': [BMI],
            'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
            'Age': [Age]}
    
    features = pd.DataFrame(data)
    
    prediction = model.predict(features)
    return prediction[0]

# Create a Streamlit app
def app():
    st.title('Diabetes Prediction')

    st.write('Enter the following details to predict whether you have diabetes or not.')

    # Create input fields for the user to enter the details
    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=17, step=1, value=0)
    glucose = st.number_input('Glucose', min_value=0, max_value=199, value=70)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=122, value=70)
    skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=99, value=20)
    insulin = st.number_input('Insulin', min_value=0, max_value=846, value=79)
    bmi = st.number_input('BMI', min_value=0.0, max_value=67.1, value=20.0)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.078, max_value=2.42, value=0.3725)
    age = st.number_input('Age', min_value=21, max_value=81, value=33)

    # Check if any input field is empty
    if glucose == 0 or blood_pressure == 0 or skin_thickness == 0 or insulin == 0 or bmi == 0.0 or diabetes_pedigree_function == 0.0 or age == 0:
        st.write('Not allowed to enter a value of 0 except for pregnancies.')
    else:# Check if any input field is empty
        if st.button('Predict'):
            result = predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)
            if result == 1:
                st.write('You have diabetes.')
            else:
                st.write('You do not have diabetes.')

if __name__ == '__main__':
    app()
