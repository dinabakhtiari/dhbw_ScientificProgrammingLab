import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- PAGE CONFIGURATION ---
# We use a wide layout to distinguish the ensemble model interface
st.set_page_config(page_title="Team 4 - Random Forest Predictor", layout="centered")

st.title("🌲 Sales Impact Predictor (Random Forest Model)")
st.write("Developed by **Team 4**: Aylin, Mariana, and Dina")
st.markdown("---")

# --- LOAD PRE-TRAINED MODEL ---
# Loading the Random Forest model which contains 100 decision trees
try:
    model = joblib.load('random_forest_model.pkl')
except FileNotFoundError:
    st.error("Error: 'random_forest_model.pkl' not found. Please ensure the file is in the same directory.")

# --- SIDEBAR: BUDGET CONTROLS ---
# These ranges are strictly based on the historical dataset limits
st.sidebar.header("🕹️ Simulation Dashboard")
st.sidebar.success("Random Forest Model Active")

tv = st.sidebar.slider("TV Budget ($)", 0.0, 300.0, 150.0)
radio = st.sidebar.slider("Radio Budget ($)", 0.0, 50.0, 25.0)
news = st.sidebar.slider("Newspaper Budget ($)", 0.0, 120.0, 40.0)

# --- PREDICTION LOGIC ---
# The model averages the results of 100 trees to give this final prediction
input_data = np.array([[tv, radio, news]])
prediction = model.predict(input_data)[0]

# --- MAIN DISPLAY: ENSEMBLE RESULT ---
st.subheader("Ensemble Sales Forecast")
# Using a green color theme for the Random Forest metric
st.metric(label="Predicted Sales Units (RF)", value=f"{prediction:.2f}")

# --- VISUALIZATION: BUDGET RANGE ANALYSIS ---
st.write("---")
st.subheader("📊 Budget Allocation (Scale: 0-300)")

channels = ['TV', 'Radio', 'Newspaper']
budgets = [tv, radio, news]

# Plotting with a 'Greens' palette to match the Random Forest theme
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=channels, y=budgets, palette="magma", ax=ax)

# Fixed Y-axis at 300 for visual consistency across all team projects
ax.set_ylim(0, 300) 
ax.set_ylabel("Budget ($)")
ax.set_title("Current Investment vs. 300 Scale")

# Adding value labels on top of the bars
for i, v in enumerate(budgets):
    ax.text(i, v + 5, f"${v}", ha='center', fontweight='bold')

st.pyplot(fig)

# --- STRATEGIC ANALYSIS SECTION ---
with st.expander("💡 Random Forest Insights"):
    st.write(f"**Total Combined Budget:** ${tv + radio + news:.2f}")
    st.write("How it works: This prediction is the **average of 100 decision trees**. "
             "It is highly effective at catching non-linear patterns that a simple "
             "linear model might miss.")