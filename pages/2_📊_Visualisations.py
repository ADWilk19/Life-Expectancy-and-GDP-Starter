# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Visualisations",
    page_icon="📊",
)
st.sidebar.header("Visualisations")
st.markdown("# Visualisations")


# Visualisations Page
st.header("Visualisations 📊")

# Load data
df = pd.read_csv('all_data.csv')
df.columns = ['country', 'year', 'life_expectancy', 'GDP']

# GDP displot
st.markdown('Let looks at the distribution of GDP for the six countries:')
plt.figure(figsize=(4,3))
ax1 = sns.displot(df.GDP, rug = True, kde=False)
plt.xlabel("GDP in Trillions of U.S. Dollars")
plt.title("GDP is right-skewed between 2000 and 2015",loc='left')
plt.show()
# plt.clf()
st.pyplot(ax1)
st.markdown('It would appear that GDP is right-skewed for these countries.')

# Life Expectancy at Birth displot
plt.figure(figsize=(8,6))
ax2 = sns.displot(df.life_expectancy, rug = True, kde=False)
plt.xlabel("Life Expectacny at Birth (Years)")
plt.title("Life Expectancy at Birth is left-skewed between 2000 and 2015")
plt.show()
# plt.clf()
st.pyplot(ax2)
