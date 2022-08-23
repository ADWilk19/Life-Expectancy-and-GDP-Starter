# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Visualisations",
    page_icon="📊",
)

# Visualisations Page
st.header("Visualisations 📊")
st.sidebar.header("Visualisations")
st.sidebar.markdown("""These visualisations are split over the following tabs:\n
- Displots;
- Barplots;
- Violin plots; and
- Lineplots.
""")


# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Displots", "Barplots", "Violin plots","Lineplots"])


with tab1:
    # Load data
    df = pd.read_csv('all_data.csv')
    df.columns = ['country', 'year', 'life_expectancy', 'GDP']

    # GDP displot
    st.markdown('### The distribution of GDP for the six countries:')
    plt.figure(figsize=(4,3))
    ax1 = sns.displot(df.GDP, rug = True, kde=False)
    plt.xlabel("GDP in Trillions of U.S. Dollars")
    plt.title("GDP is right skewed between 2000 and 2015",loc='left')
    plt.show()
    # plt.clf()
    st.pyplot(ax1)
    st.markdown('It would appear that `GDP` is right skewed for these countries.\
        This type of distribution could be described as a power law distribution.\
        More about the power law can be read [here](https://en.wikipedia.org/wiki/Power_law).')

    # Life Expectancy at Birth displot
    st.markdown('### The distribution of Life Expectancy at Birth for the six countries:')
    plt.figure(figsize=(8,6))
    ax2 = sns.displot(df.life_expectancy, rug = True, kde=False)
    plt.xlabel("Life Expectacny at Birth (Years)")
    plt.title("Life Expectancy at Birth is left skewed between 2000 and 2015")
    plt.show()
    # plt.clf()
    st.pyplot(ax2)
    st.markdown('`Life Expectancy at Birth` is very left skewed where most of the values are on the right-hand side.\
        This is almost the opposite of what was observed in the `GDP` column. A further\
        look might also identify different modes or smaller groupings of distributions within the range')
