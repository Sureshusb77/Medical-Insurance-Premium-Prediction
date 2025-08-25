

# 🏥 Medical Insurance Premium Predictor

## 📌 Overview
The **Medical Insurance Premium Predictor** is a machine learning web application built using **Python** and **Streamlit**.  
It predicts medical insurance premiums based on user inputs such as **age, gender, BMI, smoking habits, number of children, and region**.  

This project allows users to estimate insurance costs interactively and easily.

## ⚙️ Tech Stack
- Python 3.9+
- Streamlit
- scikit-learn
- pandas, numpy
- matplotlib

##  Features
- Predicts medical insurance premiums based on user inputs
- Interactive web interface using Streamlit
- Trained ML model for accurate predictions
- Optional data visualizations (BMI vs Charges, Age vs Charges)


##  Project Structure

medical_2/
├── Main/                   # Source code files
│   └── app.py              # Main Streamlit application
│
├── Data/                   # Dataset files
│   └── insurance.csv       # Insurance dataset used for model training
│
├── rf_model.pkl            # Trained Random Forest model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignore unnecessary files
└── LICENSE                 # MIT License

## Setup Instructions

 **Clone the repo**

git clone https://github.com/Sureshusb77/medical_2.git
cd medical_2

# Create environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the App
streamlit run app.py
