# Imports
import streamlit as st
import pandas as pd
import functions

st.set_page_config(
    page_title="Exploring the data",
    page_icon="🧭",
)
st.sidebar.header("Exploring the Data")
st.markdown("# Exploring the Data")

st.header("Exploring the Data 🔍")
st.subheader("Data Sources 💽")
st.markdown('The data was retrieved from the following sources:\n- GDP Source:\
    [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)\
    national accounts data, and OECD National Accounts data files.\n- Life expectancy Data Source: \
    [World Health Organization](http://apps.who.int/gho/data/node.main.688)')
st.subheader('Initial Exploration 🔍')
st.markdown('To begin, I loaded the data using Pandas.  The head of the table can be seen below:')
st.code('df = pd.read_csv("all_data.csv")\ndf.head()')
df = functions.load_data()
st.table(df.head())
st.markdown('The table has four columns.  The Life Expectancy at Birth column could be renamed to make it easier to read.')
df.columns = ['country', 'year', 'life_expectancy', 'GDP']
df = df.assign(hack='').set_index('hack')
st.table(df.head())
st.code('''
        countries = []
        for i in df.country.unique():
            countries.append(i)
        print(countries)
        ''')
countries = []
for i in df.country.unique(): countries.append(i)
st.write(countries)
st.markdown('There are six countries in this dataset, and the table has ' + str(len(df)) + ' rows.')
