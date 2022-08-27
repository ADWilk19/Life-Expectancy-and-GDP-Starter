# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions

# Page Config
st.set_page_config(
    page_title="Visualisations",
    page_icon="📊",
)

# Visualisations Page
st.header("Visualisations 📊")
st.sidebar.header("Visualisations")
st.sidebar.markdown("""These visualisations are split over the following tabs:\n
- Dist Plots;
- Bar Plots;
- Violin Plots; and
- Line Charts;
- Scatter Plots.
""")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dist Plots", "Bar Plots", "Violin Plots","Line Charts","Scatter Plots"])

# Dist Plots
with tab1:
    st.subheader('Dist Plots')
    # Load data
    df = pd.read_csv('all_data.csv')
    df.columns = ['country', 'year', 'life_expectancy', 'GDP']

    # GDP dist plot
    functions.GDP_dist_plot()
    st.markdown('It would appear that `GDP` is right skewed for these countries.\
        This type of distribution could be described as a power law distribution.\
        More about the power law can be read [here](https://en.wikipedia.org/wiki/Power_law).')

    # Life Expectancy at Birth dist plot
    st.markdown('#### The distribution of Life Expectancy at Birth for the six countries:')
    functions.life_expectancy_distplot()
    st.markdown('`Life Expectancy at Birth` is very left skewed where most of the values are on the right-hand side.\
        This is almost the opposite of what was observed in the `GDP` column. A further\
        look might also identify different modes or smaller groupings of distributions within the range.')

# Bar Plots
with tab2:
    st.subheader('Bar Plots')
    st.markdown('First, I need to break down the data by country.\
        This can be done by finding the average GDP and Life Expectancy:')
    st.code('''
            dfMeans = df.drop("year", axis = 1).groupby("country").mean().reset_index()
            ''')
    dfMeans = df.drop("year", axis = 1).groupby("country").mean().reset_index()
    st.write(dfMeans)

    st.markdown('Now it is possible to plot some bar charts:')

    # GDP
    st.markdown('### Average GDP by Country')
    functions.GDP_bar()
    st.markdown('For the average `GDP` by `Country` it seems that the US has a much higher value compared\
        to the rest of the countries. In this bar plot, Zimbabwe is not even visible where Chile is just barely seen.\
        In comparison, the USA has a huge GDP compared to the rest. China, Germany and Mexico seem to be relatively\
        close in figures.')


    # Life Expectancy at Birth
    st.markdown('### Average Life Expectancy at Birth by Country')
    functions.life_expectancy_bar()
    st.markdown('As can be seen, the average `Life Expectancy at Birth` for most countries is\
        somewhere between 74 and 80 years.  The exception is Zimbabwe which, at just over 50 years,\
        might explain the left skew of the dist plot.')

# Violin and Swarm Plots
with tab3:
    st.subheader('Violin Plots')
    # What is a violin plot?
    st.markdown('#### What is a Violin Plot? 🤔')
    st.markdown('''According to [Mode](https://mode.com/blog/violin-plot-examples/#:~:text=What%20is%20a%20violin%20plot%3F,the%20density%20of%20each%20variable),
                a violin plot is a hybrid of a box plot and a kernel density plot, which shows peaks in the data.
                It is used to visualize the distribution of numerical data.  Unlike a box plot that can only show
                summary statistics, violin plots depict summary statistics and the density of each variable.
                ''')
    st.markdown('#### Violin plots for GDP and Life Expectancy at Birth')

    # Violin plots for average GDP and Life Expectancy at Birth
    functions.violin_plot()

    # Swarm plot
    st.subheader('Overlaid Swarm Plot')
    st.markdown ('''Swarm plots are useful because they show dot density around the values as well as distribution\
        through area/shape.  The charts below show swarm plots over violin plots for `GDP` and `Life Expectancy`.\n
In the case of of the `GDP` plot on the left, Chile and Zimbabwe have a vertical line of dots that illustrate the number of data points that fall around their values. This detail would have been lost in the box plot, unless the reader is very adept at data visualizations.''')
    functions.swarm_violin_plot()

# Line Plots
with tab4:
    st.subheader('Line Plots')

    # GDP
    st.markdown('#### GDP')
    st.markdown('''
                The line plot below shows `GDP` broken down by country over the 15 year period.\n
                Of the six countries, the USA and China have seen the most siginificant increases. \
                China went from less than a quarter trillion dollars to one trillion dollars over the time span.
                ''')
    functions.GDP_line_plot()

    # GDP Facet line plots
    st.markdown('''Next, faceted line plots can be utilised to compare year on year growth/shrinkage for each country \
                with appropriate scaling:''')
    functions.GDP_facet_plot()

    # Life Expectancy at Birth
    st.markdown('#### Life Expectancy at Birth')
    st.markdown('''
                The line plot below shows `Life Expectancy at Birth` broken down by country over the 15 year period.\n
                Of the six countries, Zimbabwe has seen the biggest increase of 14 years.
                ''')
    functions.life_expectancy_line_plot()

    # Facet line plots
    st.markdown('''Next, faceted line plots can be utilised to compare year on year for each country \
                with appropriate scaling:''')
    functions.life_expectancy_facet_plot()
    st.markdown('''
                Looking at the facet plots, above, it is apparent that Chile and Mexico seemed to have dips in their life expectancy around the \
                same time which could be looked into further. This type of plotting proves useful since much \
                of these nuances were lost when the y axis was shared among the countries. \
                Also, the seemingly linear changes were not as smooth for some of the countries.
                ''')

# Scatter Plots
with tab5:
    st.subheader('Scatter Plots')
    functions.scatter_plot()
    st.markdown('''
                The next two charts will explore the relationship between `GDP` and `Life Expectancy at Birth`. In the chart, above, \
                it looks like the previous charts where GDP for Zimbabwe is staying flat, while their life expectancy \
                is going up. For the other countries they seem to exhibit a rise in life expectancy as GDP goes up. \
                The US and China seem to have very similar slopes in their relationship between GDP and life expectancy.
                ''')
    functions.facet_scatter()
    st.markdown('''
                Like the previous plots, countries are broken out into each scatter plot by facets. Looking at the \
                individual countries, most have linear relationships between GDP and life expectancy. China, on the \
                other hand has a slightly exponential curve, and Chile's looks a bit logarithmic. In general though one \
                can see an increase in GDP and life expectancy, exhibiting a positive correlation.
                ''')
