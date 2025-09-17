# Bank Loan Prediction

Bank Loan Prediction is a web application designed to help financial institutions quickly evaluate loan applications. The application predicts whether a loan request is likely to be approved or rejected based on applicant income and requested loan amount.

The system is built using Flask for the backend and HTML/CSS for the frontend, with a pre-trained machine learning model (stored as model.pkl) powering the predictions. Users input their details through a clean, responsive web form, and the application returns an immediate approval or rejection decision.

# Key Features
Machine learning–based prediction of loan approvals

User-friendly, responsive web interface

Flask backend for handling form submissions and prediction logic

Real-time results display

# Technology Stack
Backend: Python, Flask

Frontend: HTML, CSS

Model Serialization: Joblib

Deployment: Compatible with any Flask-supported hosting environment

# How It Works
The user enters the applicant’s income and requested loan amount.

The backend passes this data to the trained model.

The model predicts whether the loan will be approved or rejected.

The result is displayed immediately on the webpage.

# Project Files
app.py – Flask application and backend logic

index.html – Frontend form and page layout

model.pkl – Pre-trained machine learning model
