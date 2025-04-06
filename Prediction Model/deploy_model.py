import joblib
import pandas as pd
import streamlit as st

# Load the trained model from the joblib file
model = joblib.load('ckd_model.pkl')

# Define a function to make predictions
def predict_ckd(input_data):
    """
    Make a prediction using the loaded model.

    Args:
        input_data (list): Input features for the prediction.

    Returns:
        str: The predicted result (CKD or No CKD).
    """
    # Ensure the number of columns matches the input data
    df_input = pd.DataFrame([input_data], columns=['Age', 'Blood Pressure', 'Specific Gravity', 'Albumin', 'Sugar', 
                                                   'Red Blood Cells', 'Pus Cell', 'Pus Cell Clumps', 'Bacteria', 
                                                   'Blood Glucose Random', 'Blood Urea', 'Serum Creatinine', 
                                                   'Sodium', 'Potassium', 'Hemoglobin', 'Packed Cell Volume', 
                                                   'White Blood Cell Count', 'Red Blood Cell Count', 'Hypertension', 
                                                   'Diabetes Mellitus', 'Coronary Artery Disease', 'Appetite', 
                                                   'Pedal Edema', 'Anemia', 'Smoking Status'])  # 25 columns

    # Preprocess input data (Categorical Encoding)
    df_input['Red Blood Cells'] = df_input['Red Blood Cells'].map({'normal': 1, 'abnormal': 0})
    df_input['Pus Cell'] = df_input['Pus Cell'].map({'normal': 1, 'abnormal': 0})
    df_input['Pus Cell Clumps'] = df_input['Pus Cell Clumps'].map({'present': 1, 'notpresent': 0})
    df_input['Bacteria'] = df_input['Bacteria'].map({'present': 1, 'notpresent': 0})
    df_input['Hypertension'] = df_input['Hypertension'].map({'yes': 1, 'no': 0})
    df_input['Diabetes Mellitus'] = df_input['Diabetes Mellitus'].map({'yes': 1, 'no': 0})
    df_input['Coronary Artery Disease'] = df_input['Coronary Artery Disease'].map({'yes': 1, 'no': 0})
    df_input['Appetite'] = df_input['Appetite'].map({'good': 1, 'poor': 0})
    df_input['Pedal Edema'] = df_input['Pedal Edema'].map({'yes': 1, 'no': 0})
    df_input['Anemia'] = df_input['Anemia'].map({'yes': 1, 'no': 0})
    df_input['Smoking Status'] = df_input['Smoking Status'].map({'yes': 1, 'no': 0})  # Encoding new feature

    # Make prediction
    prediction = model.predict(df_input)

    # Return prediction (1 = CKD, 0 = No CKD)
    if prediction[0] == 1:
        return "The patient is likely to have Chronic Kidney Disease (CKD)."
    else:
        return "The patient is not likely to have Chronic Kidney Disease (CKD)."

def main():
    st.title('Chronic Kidney Disease (CKD) Prediction')

    # Collecting user input via Streamlit widgets
    age = st.number_input('Age', min_value=1, max_value=100, value=25)
    blood_pressure = st.number_input('Blood Pressure', min_value=50, max_value=200, value=80)
    specific_gravity = st.selectbox('Specific Gravity', options=[1.005, 1.010, 1.015, 1.020, 1.025])
    albumin = st.number_input('Albumin', min_value=0, max_value=5, value=0)
    sugar = st.number_input('Sugar', min_value=0, max_value=5, value=0)
    red_blood_cells = st.selectbox('Red Blood Cells', options=['normal', 'abnormal'])
    pus_cell = st.selectbox('Pus Cell', options=['normal', 'abnormal'])
    pus_cell_clumps = st.selectbox('Pus Cell Clumps', options=['present', 'notpresent'])
    bacteria = st.selectbox('Bacteria', options=['present', 'notpresent'])
    blood_glucose_random = st.number_input('Blood Glucose Random', min_value=50, max_value=300, value=100)
    blood_urea = st.number_input('Blood Urea', min_value=5, max_value=150, value=30)
    serum_creatinine = st.number_input('Serum Creatinine', min_value=0.1, max_value=20.0, value=1.2)
    sodium = st.number_input('Sodium', min_value=120, max_value=150, value=135)
    potassium = st.number_input('Potassium', min_value=2.0, max_value=8.0, value=4.5)
    hemoglobin = st.number_input('Hemoglobin', min_value=3.0, max_value=18.0, value=15.0)
    packed_cell_volume = st.number_input('Packed Cell Volume', min_value=20, max_value=60, value=44)
    white_blood_cell_count = st.number_input('White Blood Cell Count', min_value=2000, max_value=15000, value=7800)
    red_blood_cell_count = st.number_input('Red Blood Cell Count', min_value=2.0, max_value=10.0, value=5.2)
    hypertension = st.selectbox('Hypertension', options=['yes', 'no'])
    diabetes_mellitus = st.selectbox('Diabetes Mellitus', options=['yes', 'no'])
    coronary_artery_disease = st.selectbox('Coronary Artery Disease', options=['yes', 'no'])
    appetite = st.selectbox('Appetite', options=['good', 'poor'])
    pedal_edema = st.selectbox('Pedal Edema', options=['yes', 'no'])
    anemia = st.selectbox('Anemia', options=['yes', 'no'])
    smoking_status = st.selectbox('Smoking Status', options=['yes', 'no'])

    # Store the input data in a list
    input_data = [age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, 
                  pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, 
                  potassium, hemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count, 
                  hypertension, diabetes_mellitus, coronary_artery_disease, appetite, pedal_edema, anemia, 
                  smoking_status]

    # Predict CKD when the user clicks the button
    if st.button('Predict'):
        result = predict_ckd(input_data)
        st.success(result)

if __name__ == "__main__":
    main()
