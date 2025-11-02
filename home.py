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

st.write("1. To compare the relationship between sex and their Study Time and Final Grade")

# Add text below visualization
st.write("### 📝 summary:")
st.write(
    """
    These three visualizations reveal that the student population is demographically balanced (52.4% Female and 47.6% Male), but suggest a potential gender paradox in Mathematics performance and effort. The Final Grade distribution shows that Male students achieve a slightly higher median grade and exhibit a narrower interquartile range (less score variability) among the middle 50% of performers. Conversely, the Study Time distribution indicates that Female students report putting in more academic effort as evidenced by a visibly higher median study time category. This key finding—that higher self-reported effort among females does not translate to higher or equal median math scores compared to males—warrants further statistical investigation into potential mediating factors like confidence, teaching methodology, or specific socioeconomic variables
    """
)

# Create a pie chart using Plotly
# --- 1️⃣ Distribution of Sex (Pie Chart) ---
sex_counts = GP_df['sex'].value_counts().reset_index()
sex_counts.columns = ['Sex', 'Count']  # rename columns for clarity

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

st.write(
    """
    The pie chart shows a very balanced student demographic, with the student body split almost equally between Females (52.4%) and Males (47.6%).
    """
)

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

st.write(
    """
    The box for Male students is positioned higher on the grade scale than the box for Female students. The line representing the median grade for Males is visibly above the median line for Females.
     """
)
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

st.write(
    """
    The box plot shows that the median study time for Females is in a higher category (5 to 10 hours) than the median for Males, whose box center is lower (2 to 5 hours).
    """
)
