import streamlit as st
import pandas as pd
import plotly.express as px

# --- Streamlit Configuration ---
st.set_page_config(
    page_title="School GP15 Math",
    layout="wide"
)

st.header("GP15 Data Analysis and Visualization 📊", divider="blue")

# ######################################################################
# --- 1. DATA LOADING FROM URL (Replaced Dummy Data) ---
url = 'https://raw.githubusercontent.com/nurinn-bot/Math25/refs/heads/main/student_math_clean%20(1).csv'
col1, col2, col3, col4 = st.columns(4)
    
col1.metric(label="PLO 2", value=f"3.3", help="PLO 2: Cognitive Skill", border=True)
col2.metric(label="PLO 3", value=f"3.5", help="PLO 3: Digital Skill", border=True)
col3.metric(label="PLO 4", value=f"4.0", help="PLO 4: Interpersonal Skill", border=True)
col4.metric(label="PLO 5", value=f"4.3", help="PLO 5: Communication Skill", border=True)
# Load data from the remote CSV file
# Consider using @st.cache_data for improved performance in a real Streamlit app
GP_df = pd.read_csv(url)

# Calculate the counts and reset the index to create a Plotly-friendly DataFrame
# Assumes the loaded CSV has a column named 'sex'
sex_counts_df = GP_df['sex'].value_counts().reset_index()
sex_counts_df.columns = ['sex', 'Count']

st.write("Data summary (Counts):")
st.dataframe(sex_counts_df, hide_index=True)


# Count the occurrences of each sex
sex_counts = GP_df['sex'].value_counts().reset_index()
sex_counts.columns = ['Sex', 'Count']

# Create a pie chart using Plotly
fig = px.pie(
    sex_counts,
    names='Sex',
    values='Count',
    title='Distribution of Sex',
    color_discrete_sequence=px.colors.qualitative.Pastel  # optional: soft color palette
)

# Optional: show labels and percentages directly on slices
fig.update_traces(textinfo='percent+label', pull=[0.05]*len(sex_counts))

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
