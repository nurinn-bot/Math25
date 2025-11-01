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

# Count address types
address_counts = GP_df['address_type'].value_counts().reset_index()
address_counts.columns = ['Address Type', 'Count']

st.write("1. To compare the relationship between sex and their Study Time and Final Grade):")

# Create bar chart
fig1 = px.bar(
    address_counts,
    x='Address Type',
    y='Count',
    title='Distribution of Address Type',
    text='Count',
    color='Address Type',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig1.update_traces(textposition='outside')
fig1.update_layout(
    xaxis_title='Address Type',
    yaxis_title='Count',
    uniformtext_minsize=8,
    uniformtext_mode='hide'
)

st.plotly_chart(fig1, use_container_width=True)

# Count school choice reasons
school_choice_counts = GP_df['school_choice_reason'].value_counts().reset_index()
school_choice_counts.columns = ['Reason', 'Count']

# Create pie chart
fig2 = px.pie(
    school_choice_counts,
    names='Reason',
    values='Count',
    title='Distribution of School Choice Reason (GP School)',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig2.update_traces(textinfo='percent+label', pull=[0.05]*len(school_choice_counts))

st.plotly_chart(fig2, use_container_width=True)

# Count travel time occurrences
travel_time_counts = GP_df['travel_time'].value_counts().sort_index().reset_index()
travel_time_counts.columns = ['Travel Time', 'Count']

# Create bar chart
fig3 = px.bar(
    travel_time_counts,
    x='Travel Time',
    y='Count',
    title='Distribution of Travel Time (GP School)',
    text='Count',
    color='Travel Time',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig3.update_traces(textposition='outside')
fig3.update_layout(
    xaxis_title='Travel Time',
    yaxis_title='Count',
    uniformtext_minsize=8,
    uniformtext_mode='hide'
)

st.plotly_chart(fig3, use_container_width=True)
