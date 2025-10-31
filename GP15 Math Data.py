import streamlit as st
import pandas as pd
import plotly.express as px

# --- Streamlit Configuration ---
st.set_page_config(
    page_title="Arts Faculty Gender Visualization",
    layout="wide"
)

st.header("Arts Faculty Data Analysis and Visualization 📊", divider="blue")

# ######################################################################
# --- 1. DATA LOADING FROM URL (Replaced Dummy Data) ---
url = 'https://raw.githubusercontent.com/nurinn-bot/EC2024/refs/heads/main/arts_df_exported.csv'
col1, col2, col3, col4 = st.columns(4)
    
col1.metric(label="PLO 2", value=f"3.3", help="PLO 2: Cognitive Skill", border=True)
col2.metric(label="PLO 3", value=f"3.5", help="PLO 3: Digital Skill", border=True)
col3.metric(label="PLO 4", value=f"4.0", help="PLO 4: Interpersonal Skill", border=True)
col4.metric(label="PLO 5", value=f"4.3", help="PLO 5: Communication Skill", border=True)
# Load data from the remote CSV file
# Consider using @st.cache_data for improved performance in a real Streamlit app
arts_df = pd.read_csv(url)

# Calculate the counts and reset the index to create a Plotly-friendly DataFrame
# Assumes the loaded CSV has a column named 'Gender'
gender_counts_df = arts_df['Gender'].value_counts().reset_index()
gender_counts_df.columns = ['Gender', 'Count']

st.write("Data summary (Counts):")
st.dataframe(gender_counts_df, hide_index=True)

# ----------------------------------------------------------------------
## Bar Chart (Plotly Express)

st.subheader("Gender Distribution: Bar Chart")

# Create the Plotly Bar Chart
fig_bar = px.bar(
    gender_counts_df,
    x='Gender',
    y='Count',
    title='Distribution of Gender in Arts Faculty (Bar Chart)',
    color='Gender', # Color bars by gender
    labels={'Count': 'Number of Students', 'Gender': 'Student Gender'},
    template='plotly_white'
)

# Customize the layout
fig_bar.update_layout(
    xaxis={'categoryorder':'total descending'}, # Order bars by count
    margin=dict(t=50, l=0, r=0, b=0) # Adjust margins
)

# Display the chart in Streamlit
st.plotly_chart(fig_bar, use_container_width=True)

# ----------------------------------------------------------------------
## Pie Chart (Plotly Express)

st.subheader("Gender Distribution: Pie Chart")

# Create the Plotly Pie Chart
fig_pie = px.pie(
    gender_counts_df,
    names='Gender',
    values='Count',
    title='Distribution of Gender in Arts Faculty (Pie Chart)',
    hole=0.4, # Creates a donut chart (optional)
    color='Gender'
)

# Customize the traces for better text display
fig_pie.update_traces(
    textposition='inside',
    textinfo='percent+label', # Shows percentage and label (gender)
    marker=dict(line=dict(color='#000000', width=1)),
)

# Update layout for a better circular appearance
fig_pie.update_layout(
    margin=dict(t=50, l=0, r=0, b=0)
)

# Display the chart in Streamlit
# Note: use_container_width=False is often better for preserving the circular shape
st.plotly_chart(fig_pie, use_container_width=False)

# Count the occurrences of each academic year
academic_year_counts = arts_df['Bachelor  Academic Year in EU'].value_counts().reset_index()
academic_year_counts.columns = ['Academic Year', 'Count']

# Create a bar chart using Plotly
fig = px.bar(
    academic_year_counts,
    x='Academic Year',
    y='Count',
    title='Distribution of Bachelor Academic Year in Arts Faculty',
    text='Count',
    color='Academic Year',  # optional: adds color variation by category
    color_discrete_sequence=px.colors.qualitative.Pastel  # optional: soft color palette
)

# Customize layout and labels
fig.update_traces(textposition='outside')
fig.update_layout(
    xaxis_title='Academic Year',
    yaxis_title='Count',
    xaxis_tickangle=-45,  # rotate x-axis labels
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    margin=dict(l=20, r=20, t=60, b=60)
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)


# Create a box plot using Plotly
fig = px.box(
    arts_df,
    x='Gender',
    y='H.S.C (GPA)',
    title='Comparison of H.S.C (GPA) by Gender in Arts Faculty',
    color='Gender',  # optional: gives each gender a different color
    color_discrete_sequence=px.colors.qualitative.Pastel  # optional nice color palette
)

# Customize layout
fig.update_layout(
    xaxis_title='Gender',
    yaxis_title='H.S.C (GPA)',
    boxmode='group',
    margin=dict(l=20, r=20, t=60, b=60)
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Calculate the average H.S.C (GPA) for each gender
average_hsc_gpa_by_gender = arts_df.groupby('Gender')['H.S.C (GPA)'].mean().reset_index()

# Create a bar chart using Plotly
fig = px.bar(
    average_hsc_gpa_by_gender,
    x='Gender',
    y='H.S.C (GPA)',
    title='Average H.S.C (GPA) by Gender in Arts Faculty',
    text='H.S.C (GPA)',
    color='Gender',  # optional: distinct color per gender
    color_discrete_sequence=px.colors.qualitative.Pastel  # optional: soft colors
)

# Customize layout
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')  # show GPA to 2 decimals
fig.update_layout(
    xaxis_title='Gender',
    yaxis_title='Average H.S.C (GPA)',
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    margin=dict(l=20, r=20, t=60, b=60)
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Count the occurrences of each academic year
academic_year_counts = arts_df['Bachelor  Academic Year in EU'].value_counts().reset_index()
academic_year_counts.columns = ['Academic Year', 'Count']

# Create a pie chart using Plotly
fig = px.pie(
    academic_year_counts,
    names='Academic Year',
    values='Count',
    title='Distribution of Bachelor Academic Year in Arts Faculty',
    color_discrete_sequence=px.colors.qualitative.Pastel  # optional: soft color palette
)

# Optional: show percentages directly on slices
fig.update_traces(textinfo='percent+label', pull=[0.05]*len(academic_year_counts))

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Create a count plot (bar chart) using Plotly
fig = px.histogram(
    arts_df,
    x='Bachelor  Academic Year in EU',
    color='Gender',
    title='Distribution of Bachelor Academic Year by Gender in Arts Faculty',
    barmode='group',  # use 'stack' for stacked bars if preferred
    color_discrete_sequence=px.colors.qualitative.Pastel  # optional: soft color palette
)

# Customize layout for readability
fig.update_layout(
    xaxis_title='Academic Year',
    yaxis_title='Count',
    xaxis_tickangle=-45,  # rotate x-axis labels
    margin=dict(l=20, r=20, t=60, b=60),
    bargap=0.15
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
