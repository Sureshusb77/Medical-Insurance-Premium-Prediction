import numpy as np
import pickle as pkl
import streamlit as st
import pandas as pd 


rf_regressor = pkl.load(open('rf_model.pkl', 'rb'))
st.set_page_config(page_title="Insurance Premium Predictor", page_icon="💰", layout="centered")
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #dbeafe, #f0f9ff);
        color: #1e293b;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e40af, #1d4ed8);
        color: white;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Titles */
    h1, h2, h3 {
        color: #1e3a8a !important;
    }

    /* Success / Warning / Error boxes */
    .stSuccess {
        background-color: #dcfce7 !important;
        border: 1px solid #22c55e;
        border-radius: 10px;
        padding: 10px;
    }
    .stWarning {
        background-color: #fef9c3 !important;
        border: 1px solid #facc15;
        border-radius: 10px;
        padding: 10px;
    }
    .stError {
        background-color: #fee2e2 !important;
        border: 1px solid #ef4444;
        border-radius: 10px;
        padding: 10px;
    }

    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #1e3a8a;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏥 Medical Insurance Premium Predictor")
st.markdown("Predict your **Health Insurance Premium** and compare risk factors.")
st.sidebar.header("⚙️ Input Parameters")

gender = st.sidebar.selectbox('Choose Gender', ['Female', 'Male'])
smoker = st.sidebar.selectbox('Are you a smoker?', ['Yes', 'No'])
region = st.sidebar.selectbox('Choose Region', ['SouthEast', 'SouthWest', 'NorthEast', 'NorthWest'])
age = st.sidebar.slider('Enter Age', 5, 80, 25)
bmi = st.sidebar.slider('Enter BMI', 5.0, 50.0, 22.0)
children = st.sidebar.slider('Number of Children', 0, 5, 0)
if st.button('💡 Predict Premium'):
    gender = 0 if gender == 'Female' else 1
    smoker = 1 if smoker == 'Yes' else 0
    region_mapping = {'SouthEast': 0, 'SouthWest': 1, 'NorthEast': 2, 'NorthWest': 3}
    region = region_mapping[region]

    input_data = np.array([[age, gender, bmi, children, smoker, region]])
    prediction = rf_regressor.predict(input_data)
    st.success(f"💰 Estimated Insurance Premium: **${round(prediction[0], 2)} USD**")

    if prediction[0] < 5000:
        st.info("🟢 Risk Level: **Low** (Good health & lifestyle)")
    elif prediction[0] < 15000:
        st.warning("🟡 Risk Level: **Medium** (Moderate risk factors)")
    else:
        st.error("🔴 Risk Level: **High** (Consider lifestyle changes)")

    input_data_smoker = np.array([[age, gender, bmi, children, 1, region]])
    input_data_nonsmoker = np.array([[age, gender, bmi, children, 0, region]])

    smoker_pred = rf_regressor.predict(input_data_smoker)[0]
    nonsmoker_pred = rf_regressor.predict(input_data_nonsmoker)[0]

    st.markdown("### 🚬 Smoker vs Non-Smoker Premiums")
    col1, col2 = st.columns(2)
    col1.metric("Smoker", f"${round(smoker_pred, 2)}")
    col2.metric("Non-Smoker", f"${round(nonsmoker_pred, 2)}", 
                f"-${round(smoker_pred - nonsmoker_pred, 2)}")

    st.markdown("### 📊 Factor Sensitivity Analysis")
    factors = ["Age", "BMI", "Children", "Smoker"]
    impacts = [age*200, bmi*150, children*500, (smoker*10000)]

    impact_df = pd.DataFrame({"Factor": factors, "Impact": impacts})
    impact_df = impact_df.set_index("Factor")
    st.bar_chart(impact_df)

    st.markdown("### 💡 Health & Insurance Tips")
    st.write("- Maintain a healthy **BMI** to reduce long-term premiums.")
    st.write("- Avoid **smoking** – it heavily increases your insurance cost.")
    st.write("- Buying insurance at a **younger age** keeps premiums lower.")
    st.write("- Consider **family coverage** if you have children.")
