import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#PAGE CONFIGURATION
# Set the page title and layout for the dashboard
st.set_page_config(page_title="Team 4 - Sales Impact Predictor", layout="centered")

st.title("📈 Sales Impact Predictor (Linear Model)")
st.write("Developed by **Team 4**: Aylin, Mariana, and Dina")
st.markdown("---")

#LOAD PRE-TRAINED MODEL
# Loading the serialized linear regression model saved from the notebook
try:
    model = joblib.load('linear_model.pkl')
except FileNotFoundError:
    st.error("Error: 'linear_model.pkl' not found. Please ensure the file is in the same directory.")

#SIDEBAR: BUDGET CONTROLS
# Sliders are capped based on actual historical dataset maximums for accuracy
st.sidebar.header("🕹️ Budget Controls")
st.sidebar.info("Sliders are limited to historical dataset maximums.")

# TV range remains up to 300, while Radio and Newspaper are adjusted to their data limits
tv = st.sidebar.slider("TV Budget ($)", 0.0, 300.0, 150.0)
radio = st.sidebar.slider("Radio Budget ($)", 0.0, 50.0, 25.0)
news = st.sidebar.slider("Newspaper Budget ($)", 0.0, 120.0, 40.0)

#PREDICTION LOGIC
# Transform input into a 2D array for the scikit-learn model
input_data = np.array([[tv, radio, news]])
prediction = model.predict(input_data)[0]

#MAIN DISPLAY: PREDICTION RESULT
# Displaying the final forecast as a prominent metric
st.subheader("Sales Forecast")
st.metric(label="Predicted Sales Units", value=f"{prediction:.2f}")

#VISUALIZATION: COMPARATIVE BUDGET ANALYSIS
st.write("---")
st.subheader("📊 Budget Allocation (Scale: 0-300)")

# Preparing data for the visualization
channels = ['TV', 'Radio', 'Newspaper']
budgets = [tv, radio, news]

# Plotting using Seaborn for professional aesthetics
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=channels, y=budgets, palette="Set2", ax=ax)

# Fix the Y-axis range to 300 for visual comparison consistency
ax.set_ylim(0, 300) 
ax.set_ylabel("Budget ($)")
ax.set_title("Current Investment vs. 300 Scale")

# Add numerical labels on top of each bar for clarity
for i, v in enumerate(budgets):
    ax.text(i, v + 5, f"${v}", ha='center', fontweight='bold')

# Render the plot in the Streamlit interface
st.pyplot(fig)

#STRATEGIC ANALYSIS SECTION
# Expandable section for deeper insights and budget summaries
with st.expander("💡 Strategic Analysis"):
    st.write(f"**Total Combined Budget:** ${tv + radio + news:.2f}")
    st.write("Strategic Note: The chart uses a fixed scale of 300 to help managers visualize "
             "the relative weight of each channel's investment compared to the TV ceiling.")