import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('Customer_Churn_Prediction.pkl', 'rb'))

# Function to predict churn
def predict_churn(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography, Gender):
    # Preprocess input data
    if Geography == 'Germany':
        Geography_Germany = 1
        Geography_Spain = 0
        Geography_France = 0
    elif Geography == 'Spain':
        Geography_Germany = 0
        Geography_Spain = 1
        Geography_France = 0
    else:
        Geography_Germany = 0
        Geography_Spain = 0
        Geography_France = 1

    if Gender == 'Male':
        Gender_Male = 1
    else:
        Gender_Male = 0

    # Make prediction
    prediction = model.predict([[CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male]])

    if prediction == 1:
        return "The Customer will leave the bank"
    else:
        return "The Customer will not leave the bank"

# Streamlit app
def main():
    st.title("Customer Churn Prediction")

    st.write("Enter the Information Below and find if a Customer will Churn out or not")

    # Input fields
    CreditScore = st.number_input("Credit Score")
    Age = st.number_input("Age")
    Tenure = st.number_input("Tenure")
    Balance = st.number_input("Enter the Account Balance")
    NumOfProducts = st.number_input("Number of Products")
    HasCrCard = st.selectbox("Do the Customer have Credit Card?", ["1", "0"])
    IsActiveMember = st.selectbox("Is the Customer Active Member?", ["1", "0"])
    EstimatedSalary = st.number_input("Enter the Estimated Salary")
    Geography = st.selectbox("Enter The Location", ["Germany", "Spain", "France"])
    Gender = st.selectbox("Gender of Customer", ["Male", "Female"])

    # Predict button
    if st.button("Predict"):
        prediction = predict_churn(CreditScore, Age, Tenure, Balance, NumOfProducts, int(HasCrCard), int(IsActiveMember), EstimatedSalary, Geography, Gender)
        st.write(prediction)

if __name__ == "__main__":
    main()
