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
    Such a residential profile dominates the bar chart, with the vast majority of the students residing in Urban areas-286 students-heavily outweighing those from Rural areas-63 students. This split is critical for context since it suggests that this dataset primarily captures the dynamics of students in an urban setting of education in which resources, commuting infrastructure, and academic opportunities differ significantly from rural settings.
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
   This pie chart reveals the core motivations behind students choosing this specific school, categorized into four reasons: 'course' (35.5%), 'reputation' (28.7%), 'home' (28.1%), and 'other' (7.7%). The finding that academic factors ('course' and 'reputation') collectively account for over 64% of school choice reasons is highly significant. This suggests that students enrolling in this high school are generally a self-selected group who are academically strategic and motivated by the school's specific offerings or quality. The choice is primarily based on academic merit rather than simply being the nearest convenient option ('home' is a close third, but not the dominant reason).
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
    This bar chart represents the frequency of students across four categorical travel time bins. The results are overwhelmingly concentrated in the shortest category, with around 240 students reporting a travel time of less than 15 minutes. Only small fractions report commutes of 15 to 30 minutes, 30 minutes to 1 hour, or longer than 1 hour. The minimal travel time for the vast majority of the sample is a key finding for the attendance and engagement objectives.
    """
)

