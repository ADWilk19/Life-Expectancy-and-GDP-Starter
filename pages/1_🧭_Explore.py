# Imports
import streamlit as st
import pandas as pd
import functions

# Side bar info
st.set_page_config(
    page_title="Exploring the data",
    page_icon="🧭",
)
st.sidebar.header("Exploring the Data")
st.sidebar.markdown("Looking at and cleaning the data.")
st.markdown("# Exploring the Data")

# Page content
    # Load
st.subheader('Initial Exploration 🔍')
st.markdown('To begin, I loaded the data using Pandas.  The head of the table can be seen below:')
st.code('df = pd.read_csv("all_data.csv")\ndf.head()')
df = functions.load_data()
st.table(df.head())

    # Clean
st.subheader('Cleaning the Data 🧹')
st.markdown('The Life Expectancy at Birth column could be renamed to make it easier to read:')
st.code('''df.columns = ['country', 'year', 'life_expectancy', 'GDP']''')
df.columns = ['country', 'year', 'life_expectancy', 'GDP']
df = df.assign(hack='').set_index('hack')
st.table(df.head())

    # Explore
st.subheader('Looking at the shape of the dataset and the number of countries repesented 📉')
st.markdown('What is the shape of the df?')
st.code('print(df.shape)')
st.write(df.shape)
st.markdown('The data has 96 records and four columns.')
st.markdown('To see which countries are represented in the dataset:')
st.code('''
        print(df.country.unique()):
        ''')

st.write(df.country.unique())
st.markdown('There are six countries in the dataset.')
st.subheader('Descriptive statistics 🧮')
st.write(df.describe())
