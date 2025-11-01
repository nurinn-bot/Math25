import streamlit as st
import pandas as pd
import plotly.express as px

# --- Streamlit Configuration ---
st.set_page_config(
    page_title="School GP15 Math",
    layout="wide"
)

st.header("GP15 Gender Data Analysis 📊", divider="blue")

# ######################################################################
# --- 1. DATA LOADING FROM URL (Replaced Dummy Data) ---
url = 'https://raw.githubusercontent.com/nurinn-bot/Math25/refs/heads/main/student_math_clean%20(1).csv'

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

# Boxplot: Final Grade by Sex
fig1 = px.box(
    GP_df,
    x='sex',
    y='final_grade',
    color='sex',
    title='Final Grade Distribution by Sex',
    color_discrete_sequence=px.colors.qualitative.Pastel  # optional: soft colors
)

fig1.update_layout(
    xaxis_title='Sex',
    yaxis_title='Final Grade',
    boxmode='group',
    margin=dict(l=20, r=20, t=60, b=60)
)

st.plotly_chart(fig1, use_container_width=True)

# Boxplot: Study Time by Sex
fig2 = px.box(
    GP_df,
    x='sex',
    y='study_time',
    color='sex',
    title='Study Time Distribution by Sex (GP School)',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig2.update_layout(
    xaxis_title='Sex',
    yaxis_title='Study Time',
    boxmode='group',
    margin=dict(l=20, r=20, t=60, b=60)
)

st.plotly_chart(fig2, use_container_width=True)
