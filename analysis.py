import streamlit as st
import pandas as pd
import plotly.express as px

# --- Streamlit Configuration ---
st.set_page_config(
    page_title="School GP15 Family Data",
    layout="wide"
)

st.header("GP15 Family Data Analysis 📊", divider="blue")

# ######################################################################
# --- 1. DATA LOADING FROM URL (Replaced Dummy Data) ---
url = 'https://raw.githubusercontent.com/nurinn-bot/Math25/refs/heads/main/student_math_clean%20(1).csv'

# Load data from the remote CSV file
# Consider using @st.cache_data for improved performance in a real Streamlit app
GP_df = pd.read_csv(url)

# --- 1️⃣ Distribution of Parental Education (Bar Chart) ---
mother_education_counts = GP_df['mother_education'].value_counts().sort_index()
father_education_counts = GP_df['father_education'].value_counts().sort_index()

education_counts = pd.DataFrame({
    'Mother': mother_education_counts,
    'Father': father_education_counts
}).reset_index().rename(columns={'index': 'Education Level'})

fig1 = px.bar(
    education_counts,
    x='Education Level',
    y=['Mother', 'Father'],
    barmode='group',
    title='Distribution of Parental Education (GP School)',
    labels={'value': 'Count', 'Education Level': 'Education Level'},
)
fig1.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig1, use_container_width=True)


# --- 2️⃣ Distribution of Family Size (Pie Chart) ---
family_size_counts = GP_df['family_size'].value_counts().sort_index()

fig2 = px.pie(
    names=family_size_counts.index,
    values=family_size_counts.values,
    title='Distribution of Family Size (GP School)',
)
fig2.update_traces(textinfo='percent+label')
st.plotly_chart(fig2, use_container_width=True)


# --- 3️⃣ Distribution of Extra Paid Classes (Donut Chart) ---
extra_paid_counts = GP_df['extra_paid_classes'].value_counts()

fig3 = go.Figure(
    data=[go.Pie(
        labels=extra_paid_counts.index,
        values=extra_paid_counts.values,
        hole=0.4,  # makes it a donut
        textinfo='percent+label'
    )]
)
fig3.update_layout(
    title='Distribution of Extra Paid Classes (GP School)',
    showlegend=True
)
st.plotly_chart(fig3, use_container_width=True)

