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
1. Has life expectancy increased over time for the 6 nations?
2. Has GDP increased over time for the 6 nations?
3. Is there a correlation between GDP and life expectancy of a country?
4. What is the average life expectancy for these nations? and
5. What is the distribution of that life expectancy?
""")

# 1. Has Life Expectancy Increased?
st.markdown('#### 1. Has life expectancy increased over time for the 6 nations?')
functions.life_expectancy_line_plot()
st.markdown('The chart above shows that the life expectancy at birth has increased for \
the 6 nations.  This is clearer when displayed using a facet chart, below:')
functions.life_expectancy_facet_plot()
st.markdown('''Of the six countries, the USA and China have seen the most siginificant increases. \
               China went from less than a quarter trillion dollars to one trillion dollars over the time span''')

# 2. Has GDP Increased?
st.markdown('#### 2. Has GDP increased over time for the 6 nations?')
functions.GDP_line_plot()
st.markdown('''
                The line plot above shows `GDP` broken down by country over the 15 year period.\n
                Of the six countries, the USA and China have seen the most siginificant increases. \
                China went from less than a quarter trillion dollars to one trillion dollars over the time span.
                ''')

# 3. Is there a correlation between GDP and Life Expectancy?
st.markdown('#### 3. Is there a correlation between GDP and life expectancy of a country?')
functions.scatter_plot()
st.markdown('''The chart above shows `GDP` against `Life Expectancy`.  It looks like the previous charts where GDP for Zimbabwe is staying flat, while their life expectancy \
                is going up. The other countries seem to exhibit a rise in life expectancy as GDP goes up. \
                The US and China seem to have very similar slopes in their relationship between GDP and life expectancy.
                ''')

# 4. What is the average life expectancy in these nations?
st.markdown('#### 4. What is the average life expectancy in these nations?')
functions.life_expectancy_bar()
st.markdown('As can be seen, the average `Life Expectancy at Birth` for most countries is\
        somewhere between 74 and 80 years.  The exception is Zimbabwe which, at just over 50 years,\
        might explain the left skew of the dist plot.')

# 5. What is the distriubtion of that life expectancy?
st.markdown('#### 5. What is the distribution of that life expectancy?')
functions.life_expectancy_distplot()
st.markdown('`Life Expectancy at Birth` is very left skewed where most of the values are on the right-hand side.\
        This is almost the opposite of what was observed in the `GDP` column. A further\
        look might also identify different modes or smaller groupings of distributions within the range.')
