from flask import Flask, render_template, request, jsonify
from sklearn.linear_model import LogisticRegression
from joblib import load
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


app = Flask(__name__, static_folder='static')

df = pd.read_csv('../Mall_Customers.csv')
df1 =pd.read_csv('../Labelled.csv') 
# Load the saved model
model = load( '../spending_score_model.joblib')

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

        # Get the recommendations based on the predicted cluster
        recommendations = get_recommendations(predicted_cluster)

        # Create a 3D scatter plot to visualize the clusters
        fig = px.scatter_3d(df1, x='Annual Income (k$)', y='Spending Score (1-100)', z='Age',
                            title='Customer Segmentation',
                            labels={'clusters': 'Cluster Membership', 'Age': 'Age'})

        # Add hover text with additional information
        fig.update_traces(hovertemplate='<br>Annual Income: %{x}k$<br>Spending Score: %{y}<br>Age: %{z}<br>Cluster: %{marker.color}')

        # Update layout for better visualization
        fig.update_layout(scene=dict(
                            xaxis_title='Annual Income (k$)',
                            yaxis_title='Spending Score (1-100)',
                            zaxis_title='Age'),
                          margin=dict(l=0, r=0, b=0, t=50))

        # Convert the figure to JSON
        plot_json = fig.to_json()

        return jsonify(cluster=int(predicted_cluster[0]), recommendations=recommendations, plot=plot_json)

@app.route('/visualize')
def visualize():
    # Create a 3D scatter plot to visualize the clusters
    fig = px.scatter_3d(df1, x='Annual Income (k$)', y='Spending Score (1-100)', z='Age',
                         title='Customer Segmentation',
                        labels={'clusters': 'Cluster Membership', 'Age': 'Age'})

    # Add hover text with additional information
    fig.update_traces(hovertemplate='<br>Annual Income: %{x}k$<br>Spending Score: %{y}<br>Age: %{z}<br>Cluster: %{marker.color}')

    # Update layout for better visualization
    fig.update_layout(scene=dict(
                        xaxis_title='Annual Income (k$)',
                        yaxis_title='Spending Score (1-100)',
                        zaxis_title='Age'),
                      margin=dict(l=0, r=0, b=0, t=50))

    # Convert the figure to HTML
    plot_html = fig.to_html(full_html=False)

    return render_template('visualize.html', plot=plot_html)

    return render_template('visualize.html', plot=fig.to_html())


# Recommendation system based on predicted cluster
def get_recommendations(predicted_cluster):
    if predicted_cluster[0] == 0:  # Miser
        recommendations = [
            "Explore our budget-friendly product selection.",
            "Join our loyalty program for exclusive discounts.",
            "Refer friends and earn additional rewards."
        ]
    elif predicted_cluster[0] == 1:  # General
        recommendations = [
            "Discover a variety of products catering to different preferences.",
            "Check out our ongoing promotions for special deals.",
            "Share your feedback with us to help us improve."
        ]
    elif predicted_cluster[0] == 2:  # Target
         recommendations = [
        "Explore our premium product range and personalized services.",
        "Consider joining our exclusive membership for additional perks.",
        "Enjoy VIP treatment as part of our customer loyalty program."
    ]

    elif predicted_cluster[0] == 3:  # Spendthrift
        recommendations = [
        "Indulge in luxury items and unique experiences.",
        "Take advantage of limited-time offers to enhance your shopping experience.",
        "Receive personalized recommendations based on your preferences."
    ]

    elif predicted_cluster[0] == 4:  # Careful
        recommendations = [
        "Discover cost-effective and durable product options.",
        "Benefit from discounts on essential items.",
        "Access informative content to make informed decisions."
    ]
    # Add the remaining conditions for other clusters
    else:
        recommendations = []

    return recommendations

@app.route('/result', methods=['POST'])
def result():
    # Get the predicted cluster from your model
    predicted_cluster = [...] # Replace with your code to get the predicted cluster

    # Get the recommendations based on the predicted cluster
    recommendations = get_recommendations(predicted_cluster)

    return render_template('result.html', cluster=predicted_cluster, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)