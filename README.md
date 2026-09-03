Automated Data Science System

Project Overview

The Automated Data Science System is a Python-based platform that
automates major stages of the data science and machine learning
workflow, from dataset upload and preparation to model training,
evaluation, selection, and prediction.

Objectives

Upload and manage CSV datasets.

View and edit data before processing.

Profile data quality.

Clean and preprocess data.

Perform exploratory data analysis and visualization.

Train multiple machine learning models.

Compare model performance.

Automatically select the best model.

Generate predictions through a simple dashboard.

Workflow

Data Input → Data Storage → Data Editing → Data Profiling → Data
Cleaning → Data Preprocessing → EDA & Visualization → Task Detection →
Model Training → Model Evaluation → Best Model Selection → Prediction →
Report/Dashboard → Deployment → Monitoring & Retraining

Technologies

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Jupyter Notebook

Streamlit

Project Structure

Automated_Data_Science/
├── app.py
├── data/
│   └── sample_data.csv
├── notebook/
│   └── data_science.ipynb
└── README.md

Sample Dataset

The included customer dataset contains Customer_ID, Age, Income,
Website_Visits, Time_On_Site, and Purchase. The Purchase column is the
target for the initial classification example.

Installation

pip install jupyter pandas numpy matplotlib seaborn scikit-learn streamlit

Run Jupyter

jupyter notebook

Open notebook/data_science.ipynb.

Run Streamlit

From the project root:

streamlit run app.py

Upload data/sample_data.csv in the application.

Current Prototype

The first version supports CSV upload, dataset viewing, profiling, basic
cleaning, visualization, target selection, classification model
training, model comparison, best-model selection, and prediction.

Future Improvements

Automatic classification/regression detection

Regression and forecasting

Clustering

Hyperparameter tuning

Downloadable reports

Model saving/loading

Database/API support

Deployment

Monitoring and automatic retraining

Purpose

This project is intended for academic and educational use and
demonstrates how the data science lifecycle can be combined into a
single automated platform.
