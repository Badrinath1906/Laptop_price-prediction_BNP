# 💻 Laptop Price Predictor:-

An AI-powered web application that predicts the price of laptops based on user-selected specifications using Machine Learning.
The project combines data preprocessing, model training, and web deployment into a complete end-to-end solution.

🚀** Live Demo**

👉 https://laptopprice-predictionbnp-fdnbwhkekv8rfpzwmrs3bq.streamlit.app/


**📌 Project Objective

The goal of this project is to build a machine learning model that can accurately estimate laptop prices based on their specifications and provide users with an easy-to-use interface for prediction.

**🧠 Step-by-Step Technology Breakdown**

1️⃣ Python (Core Programming Language)

Python is used as the main programming language for this project because of its simplicity and powerful ecosystem for data science and web development.

✔ Used for:
- Data preprocessing
- Model training
- Backend logic
- Web app integration

2️⃣ Pandas (Data Handling & Analysis)
Pandas is used to load and manipulate the dataset.
✔ Tasks performed:
- Reading dataset (".csv" file)
- Handling missing values
- Cleaning data
- Feature transformation

3️⃣ NumPy (Numerical Computation)
NumPy is used for mathematical operations and array manipulation.
✔ Used for:
- Numerical calculations
- Feature engineering (PPI calculation)
- Handling model inputs

4️⃣ Feature Engineering
Important features were created to improve model performance:

✔ PPI (Pixels Per Inch):
- Calculated using screen resolution and size
- Helps represent display quality

✔ Encoding:
- Converted categorical features into machine-readable format

5️⃣ Scikit-learn (ML Utilities)
Scikit-learn is used for preprocessing and building ML pipelines.

✔ Used for:
- Train-test split
- Encoding
- Model evaluation
  
6️⃣ XGBoost (Machine Learning Model)
XGBoost Regressor is used as the main model for prediction.

✔ Why XGBoost?
- High accuracy
- Handles complex relationships
- Works well with structured data

✔ Task:
- Predict laptop price

7️⃣ Log Transformation (Important Step)
To improve accuracy, the target variable (price) was log-transformed:

✔ Why?
- Reduces skewness
- Improves prediction stability

✔ During prediction:
price = np.exp(prediction)

8️⃣ Model Saving (Pickle)
The trained model is saved using Pickle so it can be reused in the web app.
✔ File:
model.pkl

9️⃣ Streamlit (Web Application)
Streamlit is used to build the interactive web interface.

✔ Features:
- Dropdown inputs
- Sliders for weight & screen size
- Real-time prediction
- Attractive UI design

✔ Run command:
streamlit run app.py

🔟 UI/UX Enhancements

✔ **Features added:**
- Gradient background
- Laptop image background
- Price category (Budget / Mid / Premium)
- Prediction confidence
- Configuration summary

1️⃣1️⃣ Deployment (Streamlit Cloud)
The app is deployed using Streamlit Cloud.

✔ Steps:
- Upload code to GitHub
- Connect repo to Streamlit
- Deploy app
  
1️⃣2️⃣ Version Control (GitHub)

GitHub is used to store and manage the project.

✔ Benefits:
- Code sharing
- Version tracking
- Portfolio showcase

📁 Project Structure

Laptop_price-prediction_BNP/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
├── train.ipynb
├── laptop_data.csv

📊 Features of the Application

✔ Predict laptop price instantly
✔ Real-world input ranges
✔ Interactive UI
✔ Clean and modern design
✔ ML-based prediction

🔮 Future Improvements

- Add more features (battery, processor speed)
- Improve model accuracy
- Add comparison between laptops
- Integrate database

👨‍💻 Author
(BNP)
--⭐ Support!!


