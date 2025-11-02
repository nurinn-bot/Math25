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

# Load data from the remote CSV file
# Consider using @st.cache_data for improved performance in a real Streamlit app
GP_df = pd.read_csv(url)

# Count address types
address_counts = GP_df['address_type'].value_counts().reset_index()
address_counts.columns = ['Address Type', 'Count']

st.write("2.  To identify factors that may impact attendance and academic engagement")

st.write("### 📝 Summary")
st.write(
    """
    These visualizations concerning geographic and logistical factors reveal that the student sample is overwhelmingly urban-based (approximately 4 out of 5 students reside in urban areas) and faces minimal logistical burdens, as the vast majority of students report a travel time of less than 15 minutes to school. Despite this low travel time, the primary motivators for school choice are academic and reputational ('course' and 'reputation' account for over 64% of reasons), rather than simple proximity ('home' is third at 28.1%). Therefore, this initial exploration suggests that travel time and geographic location are unlikely to be primary drivers of issues related to attendance or engagement for the average student in the sample.
    """
)

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

st.write(
    """
    The majority of students, 286 counts, reside in Urban areas, while only 63 counts reside in Rural areas.
    """
)
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
st.write(
    """
   The two dominant reasons for school choice are 'course' 35.5% and 'reputation' 28.7%, which collectively form the largest share, with 'home' 28.1% being a close third.
    """
)
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
st.write(
    """
    The largest bar is the <15 min category, containing 240 students. Few students fall into the longer commute times 30 min to 1 hour or >1 hour.
    """
)

