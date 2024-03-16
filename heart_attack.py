import streamlit as st
import pickle
import numpy as np  

model = pickle.load(open('/home/mary/other projects/heart_attack.pkl', 'rb'))

def heart():
    st.title("Heart Attack Prediction")

    col1, col2 = st.columns(2)  

    with col1:
        age=st.text_input("age")
        gender=st.text_input("sex")
        rbp = st.text_input("Resting Blood Pressure")
        chol = st.text_input("Cholesterol")
        fbs = st.text_input("Fasting Blood Sugar")
        rer = st.text_input("Resting Electrocardiographic Result")
       
    with col2:
        heart_rate = st.text_input("Heart Rate Achieved")
        exercise_induced = st.text_input("Exercise Induced")
        depression = st.text_input("Depression Induced")
        speech = st.text_input("speech language path")
        cor_artery_anomaly = st.text_input("Coronary Artery Anomaly")
        

    if st.button('Predict'):
        #Validating  gender input
        if gender not in ['0', '1']:
            st.error("gender can either be 0 or 1.")
            return
        
        # Converting input values to numeric types
        input_data = np.array([[float(age), float(gender), float(rbp), float(chol), float(fbs), float(rer),
                                float(heart_rate), float(exercise_induced), float(depression),float(speech),
                                float(cor_artery_anomaly) ]])
        
        # Making prediction
        make_prediction = model.predict(input_data)

        if make_prediction[0] == 1:
            st.success("You have a risk of heart attack.")
        else:
            st.success("You don't have a risk of heart attack.")
            

if __name__ == "__main__":
    heart()
