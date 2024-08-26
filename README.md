# 🛍️ Customer Segmentation Web App

Welcome to the Customer Segmentation Web App! This application allows users to enter their details and get predictions on their spending score, along with visualizations of customer segments.

## 🚀 Features

- **Dynamic User Input**: Enter age, annual income, and spending score to get predictions.
- **Real-time Visualization**: View 3D scatter plots of customer segments.
- **Personalized Recommendations**: Receive tailored recommendations based on predicted customer segments.

## 🛠️ Technologies Used

- **Flask**: Backend framework for handling requests and responses.
- **Pandas**: Data manipulation and analysis.
- **Plotly**: Interactive visualizations.
- **Scikit-learn**: Machine learning model for predictions.
- **HTML/CSS/JavaScript**: Frontend for user interaction and dynamic updates.

## 📦 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Thorne-Musau/Consumer-Segmentation-Analysis.git
    cd customer-segmentation-webapp
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python webapp/app.py
    ```

5. **Open your browser** and navigate to `http://127.0.0.1:5000/`.

## 📊 Visualizations

The app provides interactive 3D scatter plots to visualize customer segments based on age, annual income, and spending score.

## 🤖 Machine Learning Model

The app uses a pre-trained Logistic Regression model to predict customer segments. The model is loaded from a `.joblib` file.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👥 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## 📧 Contact

For any inquiries, please contact [thornemusau.com](mailto:thornemusau@gmail.com).

---

<p align="center">
    Made with ❤️ by [Thorne Musau](https://github.com/Thorne-Musau)
</p>