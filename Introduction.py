import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)


# st.sidebar.success("Select a demo above.")
st.sidebar.header("Introduction to the project")
st.sidebar.markdown("This project will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.")
st.header("Introduction to the project 👋")
st.subheader("Objective 📍")
st.markdown("To explore the relationship between GDP and Life Expectancy at Birth in the data sourced, below: ")
st.subheader("Data Sources 💽")
st.markdown('The data was retrieved from the following sources:\n- GDP Source:\
    [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)\
    national accounts data, and OECD National Accounts data files.\n- Life expectancy Data Source: \
    [World Health Organization](http://apps.who.int/gho/data/node.main.688)')
st.subheader("What are the goals of the project? 🎯")
st.markdown('''This project will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.
            The goals are to prepare data, followed by analysis with plots, and seek to explain the findings from the study.''')
st.subheader("What questions will I attempt to answer? 🙋")
st.markdown('''
            Here are the questions that this project will seek to answer:
            1. Has life expectancy increased over time in the six nations?
            2. Has GDP increased over time in the six nations?
            3. Is there a correlation between GDP and life expectancy of a country?
            4. What is the average life expectancy in these nations? and
            5. What is the distribution of that life expectancy?
            ''')
