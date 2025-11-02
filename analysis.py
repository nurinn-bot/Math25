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
# --- 1. DATA LOADING ---
url = 'https://raw.githubusercontent.com/nurinn-bot/Math25/refs/heads/main/student_math_clean%20(1).csv'
GP_df = pd.read_csv(url)

st.write("3. To analyse the socioeconomic influences on student performance")

st.write("### 📝 Summary")
st.write(
    """
   These visualizations examining socioeconomic factors reveal that most students come from larger families but also benefit from significant academic investment and generally high parental educational capital. The Distribution of Family Size shows that a large majority of students (72.2%) come from families with more than three members (likely children), suggesting a high potential for resource dilution. However, this potential dilution is partially offset by high parental investment, as seen in the Distribution of Extra Paid Classes, where nearly half the students (46.1%) receive private tutoring. Crucially, the Distribution of Parental Education shows that the largest single cohort of parents has achieved 'Higher education', indicating a substantial level of educational capital in the home, although the father's education is slightly lower in the secondary and primary categories, highlighting a complex and varied socioeconomic landscape within the student body.
   """
)

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
    color_discrete_sequence=px.colors.qualitative.Pastel  
)
fig1.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig1, use_container_width=True)

st.write(
    """
    The highest frequency for both Mother and Father is the 'Higher education' category. Mothers have a higher count in 'Higher education', while Fathers have a higher count in the 'secondary education' and 'primary education (4th grade)' categories.
    """
)

# --- 2️⃣ Distribution of Family Size (Pie Chart) ---
family_size_counts = GP_df['family_size'].value_counts().sort_index()

fig2 = px.pie(
    names=family_size_counts.index,
    values=family_size_counts.values,
    title='Distribution of Family Size (GP School)',
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig2.update_traces(textinfo='percent+label')
st.plotly_chart(fig2, use_container_width=True)

st.write(
    """
   72.2% of students come from families with 'Greater than 3' members, while 27.8% come from families of 'Less than or equal to 3' members.
   """
)

# --- 3️⃣ Distribution of Extra Paid Classes (Donut Chart) ---
extra_paid_counts = GP_df['extra_paid_classes'].value_counts()

fig3 = go.Figure(
    data=[go.Pie(
        labels=extra_paid_counts.index,
        values=extra_paid_counts.values,
        hole=0.4,
        textinfo='percent+label',
        textfont=dict(size=14),
        marker=dict(colors=px.colors.qualitative.Pastel)  
    )]
)

fig3.update_layout(
    title='Distribution of Extra Paid Classes (GP School)',
    showlegend=True,
)

st.plotly_chart(fig3, use_container_width=True)

st.write(
    """
    A slight majority of students, 53.9%, report not taking extra paid classes, while 46.1% report that they do take them.
    """
)
