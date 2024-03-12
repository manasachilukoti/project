# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st
import warnings

# Load the model
loaded_model = pickle.load(open('E:/Manasa/trained_model.sav', 'rb'))

# Suppressing warnings related to feature names
warnings.filterwarnings("ignore", message="X does not have valid feature names")

def fraud_detection(step, Payment_type, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest):
    input_data = [step, Payment_type, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    print("Input data:", input_data_reshaped)  # Print input data for debugging
    prediction = loaded_model.predict(input_data_reshaped)
    print("Raw prediction:", prediction)  # Print raw prediction for debugging
    if prediction[0] == 1:
        return 'FRAUD'
    elif prediction[0] == 0:
        return 'Not FRAUD'
    else:
        return 'not working'

def main():
    st.title('Online Payment Fraud Detection')
    col1,col2=st.columns(2)
    with col1:
        step = st.number_input('step', step=1.0,format="%.0f")
    with col2:
        Payment_type = st.number_input('Payment_type',format="%.0f")
    with col1:
        amount = st.number_input('amount', step=1.0,format="%.2f")
    with col2:
        oldbalanceOrg = st.number_input('oldbalanceOrg',format="%.2f")
    with col1:
        newbalanceOrig = st.number_input('newbalanceOrig', step=1.0,format="%.1f")
    with col2:
        oldbalanceDest = st.number_input('oldbalanceDest', step=1.0,format="%.2f")
    with col1:
        newbalanceDest = st.number_input('newbalanceDest', step=1.0,format="%.2f") 
    
    pred = ''
    if st.button('Fraud Detection'):
        pred = fraud_detection(step, Payment_type, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest)       
    st.success(pred)

if __name__ == '__main__':
    main()
