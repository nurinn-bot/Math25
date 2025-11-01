import streamlit as st
st.set_page_config(
    page_title="GP School Data"
)
visualise = st.Page('GP15 Math Data.py', title='Student Data', icon=":material/school:")

home = st.Page('home.py', title='GP15 Student Gender Data', default=True, icon=":material/home:")

analysis = st.Page("analysis.py", title="Analysis", icon="📈")

pg = st.navigation(
        {
            "Menu": [home, visualise, analysis]
        }
    )

pg.run()
