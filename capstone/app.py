import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Page Header 
st.set_page_config(page_title="Team 4 - Sales Predictor")
st.title("📊 Advertising Sales Impact Predictor")
st.write("Team 4: Aylin, Mariana, and Dina")

# 2. Load the trained Linear Regression model 
try:
    model = joblib.load('advertising_model.pkl')
except:
    st.error("Model file not found. Make sure 'advertising_model.pkl' is in the 'capstone' folder.")

# 3. Create the Optimization Dashboard (Sliders) 
st.sidebar.header("Budget Simulation")
# These sliders allow users to simulate different ad spends to maximize sales [cite: 26]
tv = st.sidebar.slider("TV Budget ($)", 0.0, 300.0, 150.0)
radio = st.sidebar.slider("Radio Budget ($)", 0.0, 50.0, 25.0)
news = st.sidebar.slider("Newspaper Budget ($)", 0.0, 110.0, 40.0)

# 4. Predict Sales Units based on input 
input_data = np.array([[tv, radio, news]])
prediction = model.predict(input_data)[0]

# 5. Display Prediction [cite: 26]
st.header("Predicted Sales Result")
st.metric(label="Units to be Sold", value=f"{prediction:.2f}")

# 6. ROI Highlight (Coefficient visualization) 
st.write("---")
st.subheader("ROI Analysis - Marketing Impact")
# Using pairplot trends logic to show impact 
features = ['TV', 'Radio', 'Newspaper']
coeffs = model.coef_
fig, ax = plt.subplots()
sns.barplot(x=features, y=coeffs, ax=ax, palette="viridis")
ax.set_ylabel("Impact on Sales")
st.pyplot(fig)