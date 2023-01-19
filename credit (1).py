

import numpy as np
import pickle
import streamlit as st
from PIL import Image

filename = 'trained_loan.sav'

loaded_model= pickle.load(open(filename,"rb"))

#creating a prediction

def card_pred(input_data):
    
    #changing the input data as numpy array
    input_data_as_numpy_array= np.asarray(input_data)
    
    #reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if(prediction[0]==1):
        return "Oopps!!!! Fraud"
    else:
        return "Not Fraud"
    
    

def main():
    
    img1 = Image.open("C:/Users/hp/Desktop/deployment/img/f.png")
    img1 = img1.resize((506,305))
    st.image(img1,use_column_width=False)
    #giving the iyle
    st.title("Credit Card Fraud Transaction Prediction System")
    st.text("𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 𝐁𝐫𝐞𝐚𝐤-𝐨𝐮𝐭 𝟏")
    
    
    #getting the input data rom user
    
    
    
    Time= st.text_input("enter the time")
    V1= st.text_input("V1 conidential information")
    V2= st.text_input("V2 conidential information")
    V3= st.text_input("V3 conidential information")
    V4= st.text_input("V4 conidential information")
    V5= st.text_input("V5 conidential information")
    V6= st.text_input("V6 conidential information")
    V7= st.text_input("V7 conidential information")
    V8= st.text_input("V8 conidential information")
    V9= st.text_input("V9 conidential information")
    V10= st.text_input("V10 conidential information")
    V11= st.text_input("V11 conidential information")
    V12= st.text_input("V12 conidential information")
    V13= st.text_input("V13 conidential information")
    V14= st.text_input("V14 conidential information")
    V15= st.text_input("V15 conidential information")
    V16= st.text_input("V16 conidential information")
    V17= st.text_input("V17 conidential information")
    V18= st.text_input("V18 conidential information")
    V19= st.text_input("V19 conidential information")
    V20= st.text_input("V20 conidential information")
    V21= st.text_input("V21 conidential information")
    V22= st.text_input("V22 conidential information")
    V23= st.text_input("V23 conidential information")
    V24= st.text_input("V24 conidential information")
    V25= st.text_input("V25 conidential information")
    V26= st.text_input("V26 conidential information")
    V27= st.text_input("V27 conidential information")
    V28= st.text_input("V28 conidential information")
    Amount= st.text_input("nter the Amount")
    
    
    
    
    #code prediction
    card_fraud= ""
    
    #creating button
    
    if st.button("result"):
        card_fraud=card_pred([Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount])
        
    st.success(card_fraud)
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
        
    
    
