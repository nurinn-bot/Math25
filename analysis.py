import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

st.write("3. To analysis the socioeconomic influences on student performance")

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

st.write(
    """
    The most important finding is the high frequency of 'Higher education' among both parents. This suggests the student body, on average, benefits from strong educational and cultural capital in the home, which often correlates strongly with academic success. However, the differences between Mother's and Father's attainment (e.g., more fathers at lower levels) may necessitate treating these variables separately in the regression models.
    """
)
# --- 2️⃣ Distribution of Family Size (Pie Chart) ---
family_size_counts = GP_df['family_size'].value_counts().sort_index()

fig2 = px.pie(
    names=family_size_counts.index,
    values=family_size_counts.values,
    title='Distribution of Family Size (GP School)',
)
fig2.update_traces(textinfo='percent+label')
st.plotly_chart(fig2, use_container_width=True)

st.write(
    """
    The pie chart categorizes family size into two bins: 'Less than or equal to 3' and 'Greater than 3' (referring to family members/children). The vast majority of students, 72.2%, belong to families categorized as 'Greater than 3' members. This heavy skew towards larger family sizes is significant when considering the Resource Dilution Theory. A family with a greater number of children means that fixed resources—such as parental time, attention, financial investment (per child), and shared study space—are spread more thinly.
    """
)

# Count values
extra_paid_counts = GP_df['extra_paid_classes'].value_counts()

# Create a donut chart using Plotly
fig = go.Figure(
    data=[go.Pie(
        labels=extra_paid_counts.index,
        values=extra_paid_counts.values,
        hole=0.4,  # makes it a donut
        textinfo='percent+label',
        textfont=dict(size=14)
    )]
)

# Update layout
fig.update_layout(
    title='Distribution of Extra Paid Classes (GP School)',
    showlegend=True,
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.write(
    """
    This chart shows the direct financial investment parents make in their children's education. A substantial portion of students, 46.1%, report receiving Extra Paid Classes (tutoring), while the majority, 53.9%, do not. This finding highlights a clear socioeconomic split in access to supplemental resources. Receiving paid tutoring is often a form of socioeconomic advantage intended to boost performance.
    """
)

st.write("### 📝 Summary")
st.write(
    """
   These visualizations examining socioeconomic factors reveal that most students come from larger families but also benefit from significant academic investment and generally high parental educational capital. The Distribution of Family Size shows that a large majority of students (72.2%) come from families with more than three members (likely children), suggesting a high potential for resource dilution. However, this potential dilution is partially offset by high parental investment, as seen in the Distribution of Extra Paid Classes, where nearly half the students (46.1%) receive private tutoring. Crucially, the Distribution of Parental Education shows that the largest single cohort of parents has achieved 'Higher education', indicating a substantial level of educational capital in the home, although the father's education is slightly lower in the secondary and primary categories, highlighting a complex and varied socioeconomic landscape within the student body.
   """
)
