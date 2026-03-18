import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#PAGE CONFIGURATION
# We use a wide layout to distinguish the ensemble model interface
st.set_page_config(page_title="Team 4 - Random Forest Predictor", layout="centered")

st.title("🌲 Sales Impact Predictor")
st.write("Developed by **Team 4**: Aylin, Mariana, and Dina")
st.markdown("---")

# LOAD PRE-TRAINED MODEL
# Loading the Random Forest model which contains 100 decision trees
try:
    model = joblib.load('random_forest_model.pkl')
except FileNotFoundError:
    st.error("Error: 'random_forest_model.pkl' not found. Please ensure the file is in the same directory.")

#SIDEBAR: BUDGET CONTROLS
# These ranges are strictly based on the historical dataset limits
st.sidebar.header("🕹️ Simulation Dashboard")
st.sidebar.info("Input Scale: Budget in thousands ($1,000s)")


tv = st.sidebar.slider("TV Budget ($)", 0.0, 300.0, 150.0)
radio = st.sidebar.slider("Radio Budget ($)", 0.0, 50.0, 25.0)
news = st.sidebar.slider("Newspaper Budget ($)", 0.0, 120.0, 40.0)

#PREDICTION LOGIC
# The model averages the results of 100 trees to give this final prediction
input_data = np.array([[tv, radio, news]])
prediction = model.predict(input_data)[0]


#MAIN DISPLAY: ENSEMBLE RESULT
st.subheader("Ensemble Sales Forecast")
# Displaying the result
st.metric(label="Predicted Sales Units", value=f"{prediction:.2f} Units")
st.caption("Note: Based on the dataset, 1 Sales Unit represents $1,000,000 (Million) in Revenue.")

#VISUALIZATION: BUDGET RANGE ANALYSIS
st.write("---")
st.subheader("📊 Budget Allocation")

channels = ['TV', 'Radio', 'Newspaper']
budgets = [tv, radio, news]

# Plotting with a 'Greens' palette to match the Random Forest theme
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=channels, y=budgets, palette="magma", ax=ax)

# Fixed Y-axis at 300 for visual consistency across all team projects
ax.set_ylim(0, 300) 
ax.set_ylabel("Budget (in $1,000)")
ax.set_title("Marketing Investment Distribution")

# Adding value labels on top of the bars
for i, v in enumerate(budgets):
    ax.text(i, v + 5, f"${v}", ha='center', fontweight='bold')

st.pyplot(fig)

# STRATEGIC ANALYSIS SECTION
with st.expander("💡 Strategic Insights"):
    # Calculating values for context
    total_investment_dollars = (tv + radio + news) * 1000 
    estimated_revenue_dollars = prediction * 1000000 
    
    # Displaying clean metrics without the green/red boxes
    st.write(f"**Total Ad Spend:** ${total_investment_dollars:,.2f}")
    st.write(f"**Total Sales Revenue:** ${estimated_revenue_dollars:,.2f}")
    
    # Simple ROI Calculation to show effectiveness
    roi_ratio = estimated_revenue_dollars / total_investment_dollars if total_investment_dollars > 0 else 0
    st.write(f"**Revenue to Spend Ratio:** {roi_ratio:.1f}x")
    
    st.info("Every $1 spent in this scenario returns approximately " + f"${roi_ratio:.1f}" + " in revenue.")