from flask import Flask, render_template, request, jsonify
from sklearn.linear_model import LogisticRegression
from joblib import load
import os
import pandas as pd
import plotly.express as px

app = Flask(__name__,template_folder='templates')

df = pd.read_csv(r'C:\Users\Thorne\Desktop\Projects\csdraft\Mall_Customers.csv')

# Load the saved model
model = load(r'C:\Users\Thorne\Desktop\Projects\csdraft\spending_score_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input from the form
        new_age = float(request.form['age'])
        new_annual_income = float(request.form['annual_income'])
        new_spending_score = float(request.form['spending_score'])

        # Create a DataFrame with the user input
        new_customer_features = pd.DataFrame({
            'Age': [new_age],
            'Annual Income (k$)': [new_annual_income],
            'Spending Score (1-100)': [new_spending_score]
        })

        # Make predictions for the new customer
        predicted_cluster = model.predict(new_customer_features)

        # Render the result on the web page
        return render_template('result.html', cluster=predicted_cluster[0])

@app.route('/visualize')
def visualize():
    # Create a scatter plot to visualize the clusters
    fig = px.scatter(df, x='Annual Income (k$)', y='Spending Score (1-100)', color='Cluster',
                     title='Customer Segmentation', labels={'Cluster': 'Cluster Membership'})

    return render_template('visualize.html', plot=fig.to_html())

if __name__ == '__main__':
    app.run(debug=True)
