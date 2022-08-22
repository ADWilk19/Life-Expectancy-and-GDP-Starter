import streamlit as st
import numpy as np
import pandas as pd
import functions


st.title("Exploring Life Expectancy at Birth and GDP")

# Page selectors
page = st.sidebar.selectbox('Select page',
  ['Introduction 👋','Exploring the Data  🔍','Visualisations 📊'])


# Intro Page
if page == "Introduction 👋":
    st.header("Introduction to the project 👋")
    st.subheader("What are the goals of the project? 🎯")
    st.markdown('''This is a project that investigates Life\
                Expectancy at Birth and GDP for six nations between 2000 and 2015.\nThe goals are to\
                prepare the data, explore  and analyse it to create plots and
                seek to answer the questions, below.''')
    st.subheader("What questions will I attempt to answer? 🙋")
    st.markdown('''
                Here are the questions that this project will seek to answer:
                1. Has life expectancy increased over time in the six nations?
                2. Has GDP increased over time in the six nations?
                3. Is there a correlation between GDP and life expectancy of a country?
                4. What is the average life expectancy in these nations? and
                5. What is the distribution of that life expectancy?
                ''')

# Data Page
elif page == "Exploring the Data  🔍":
    st.header("Exploring the Data 🔍")
    st.subheader("Data Sources 💽")
    st.markdown('The data was retrieved from the following sources:\n- GDP Source:\
        [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)\
        national accounts data, and OECD National Accounts data files.\n- Life expectancy Data Source: \
        [World Health Organization](http://apps.who.int/gho/data/node.main.688)')
    st.subheader('Initial Exploration 🔍')
    st.markdown('To begin, I loaded the data using Pandas.  The head of the DataFrame can be seen below:')
    st.code('df = pd.read_csv("all_data.csv")\ndf.head()')
    st.write(functions.load_data())
    st.markdown(''' Looking at the column headers, it looks as if they could be renamed to make\
        it easier to read. 🤔
        ''')


# Visualisations
# else:
#     st.header("Visualisations 📊")
