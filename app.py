import streamlit as st

import numpy as np
import pandas as pd

st.title("Exploring Life Expectancy at Birth and GDP")

# Page selectors
page = st.sidebar.selectbox('Select page',
  ['Intro','Exploring the Data','Visualisations'])


# Intro Page
if page == "Intro":
    st.header("Introduction to the project")
    st.subheader("What is the goals of the project?")
    st.markdown('''This is a project that investigates Life\
                Expectancy at Birth and GDP for six nations between 2000 and 2015.
                \n The goals are to prepare data, followed by analysis with plots,\
                and seek to explain the findings.''')
    st.subheader("What questions will I answer?")
    st.markdown('Here are the questions that this project will seek to answer:')
    questions = [
        '1. Has life expectancy increased over time in the six nations?',
        '2. Has GDP increased over time in the six nations?',
        '3. Is there a correlation between GDP and life expectancy of a country?',
        '4. What is the average life expectancy in these nations? and',
        '5. What is the distribution of that life expectancy?'
    ]

    st.write('[')


# Data Page
elif page == "Exploring the Data":
    st.header("Exploring the Data")

# Visualisations
else:
    st.header("Visualisations")
