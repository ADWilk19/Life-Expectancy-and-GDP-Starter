# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions

# Page Config
st.set_page_config(
    page_title="Findings",
    page_icon="🔍",
)

# Findings Page
st.header("Findings 🔍")
st.sidebar.header("Findings")
st.sidebar.markdown("""In this section I will attempt to answer the following questions:\n
1. Has life expectancy increased over time in the 6 nations?
2. Has GDP increased over time for the 6 nations?
3. Is there a correlation between GDP and life expectancy of a country?
4. What is the average life expectancy for these nations? and
5. What is the distribution of that life expectancy?
""")

# Has Life Expectancy Increased?
st.markdown('#### 1. Has life expectancy increased over time in the 6 nations?')
functions.life_expectancy_line_plot()
st.markdown('The chart above shows that the life expectancy at birth has increased for \
    the 6 nations.  This is clearer when displayed using a facet chart, below:')
functions.life_expectancy_facet_plot()

# Has GDP Increased?
st.markdown('#### 2. Has GDP increased over time for the 6 nations?')
functions.GDP_line_plot()

# Is there a correlation between GDP and Life Expectancy?
st.markdown('#### 3. Is there a correlation between GDP and life expectancy of a country?')
functions.scatter_plot()

# What is the average life expectancy in these nations?
st.markdown('#### 4. What is the average life expectancy in these nations?')
# functions.life_expectancy_bar()

# What is the distriubtion of that life expectancy?
st.markdown('#### 5. What is the distribution of that life expectancy?')
functions.life_expectancy_displot()
