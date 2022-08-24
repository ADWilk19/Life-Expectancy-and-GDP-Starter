# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
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

# Displots
with tab1:
    st.subheader('Displots')
    # Load data
    df = pd.read_csv('all_data.csv')
    df.columns = ['country', 'year', 'life_expectancy', 'GDP']

    # GDP displot
    st.markdown('#### The distribution of GDP for the six countries:')
    plt.figure(figsize=(3,3))
    ax1 = sns.displot(df.GDP, rug = True, kde=False)
    plt.xlabel("GDP in Trillions of U.S. Dollars")
    plt.title("GDP is right skewed between 2000 and 2015",loc='left')
    plt.show()
    st.pyplot(ax1)
    st.markdown('It would appear that `GDP` is right skewed for these countries.\
        This type of distribution could be described as a power law distribution.\
        More about the power law can be read [here](https://en.wikipedia.org/wiki/Power_law).')

    # Life Expectancy at Birth displot
    st.markdown('#### The distribution of Life Expectancy at Birth for the six countries:')
    plt.figure(figsize=(8,6))
    ax2 = sns.displot(df.life_expectancy, rug = True, kde=False)
    plt.xlabel("Life Expectacny at Birth (Years)")
    plt.title("Life Expectancy at Birth is left skewed between 2000 and 2015")
    plt.show()
    st.pyplot(ax2)
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
    fig, ax = plt.subplots()
    plt.figure(figsize=(8,6))
    ax = sns.barplot(x ='GDP',y = 'country',data=dfMeans,order=dfMeans.sort_values('GDP').country,ax=ax)
    for i in ax.containers:
        ax.bar_label(i,)
    ax.set_xlabel('GDP in trillions of dollars')
    ax.set_ylabel('Country')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_xticks([])
    ax.set_xticklabels([])
    st.pyplot(fig)
    st.markdown('For the average `GDP` by `Country` it seems that the US has a much higher value compared\
        to the rest of the countries. In this bar plot, Zimbabwe is not even visible where Chile is just barely seen.\
        In comparison, the USA has a huge GDP compared to the rest. China, Germany and Mexico seem to be relatively\
        close in figures.')


    # Life Expectancy at Birth
    st.markdown('### Average Life Expectancy at Birth by Country')
    fig2, ax2 = plt.subplots()
    plt.figure(figsize=(8,6))
    ax2 = sns.barplot(x ='life_expectancy',y = 'country',data=dfMeans,order=dfMeans.sort_values('life_expectancy').country,ax=ax2)
    for i in ax.containers:
        ax2.bar_label(i,)
    ax2.set_xlabel('Life Expectancy at Birth (Years)')
    ax2.set_ylabel('Country')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.set_xticks([])
    ax2.set_xticklabels([])
    st.pyplot(fig2)
    st.markdown('As can be seen, the average `Life Expectancy at Birth` for most countries is\
        somewhere between 74 and 80 years.  The exception is Zimbabwe which, at just over 50 years,\
        might explain the left skew of the displot.')

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
    fig, (ax1,ax2) = plt.subplots(1, 2, sharey=True, figsize=(9, 6))
    ax1 = sns.violinplot(ax=ax1, x=df.GDP, y=df.country)
    ax1.set_xlabel("GDP in Trillions of U.S. Dollars",size=13)
    ax1.set_ylabel('Country',size=13)
    ax1.xaxis.set_label_coords(.5, -.1)
    ax2 = sns.violinplot(ax=ax2, x=df.life_expectancy, y=df.country)
    ax2.set_ylabel('Country',size=13)
    ax2.set_xlabel("Life expectancy at birth (years)",size=13)
    ax2.xaxis.set_label_coords(.5, -.1)
    # spacing = 0.100
    # fig.subplots_adjust(bottom=spacing)
    st.pyplot(fig)

    # Swarm plot
    st.subheader('Overlaid Swarm Plot')
    st.markdown ('''Swarm plots are useful because they show dot density around the values as well as distribution\
        through area/shape.  The charts below show swarm plots over violin plots for `GDP` and `Life Expectancy`.\n
In the case of of the `GDP` plot on the left, Chile and Zimbabwe have a vertical line of dots that illustrate the number of data points that fall around their values. This detail would have been lost in the box plot, unless the reader is very adept at data visualizations.''')
    fig2, (ax3,ax4) = plt.subplots(1, 2, sharey=True, figsize=(9, 6))
    ax3 = sns.swarmplot(ax=ax3, x=df.GDP, y=df.country)
    ax3 = sns.violinplot(ax=ax3, x=df.GDP, y=df.country,color='black')
    ax3.set_xlabel("GDP in Trillions of U.S. Dollars",size=13)
    ax3.xaxis.set_label_coords(.5, -.1)
    ax4 = sns.swarmplot(ax=ax4, x=df.life_expectancy, y=df.country)
    ax4 = sns.violinplot(ax=ax4, x=df.life_expectancy, y=df.country,color='black')
    ax4.set_xlabel("Life expectancy at birth (years)",size=13)
    ax4.xaxis.set_label_coords(.5, -.1)
    st.pyplot(fig2)

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
    fig = plt.figure(figsize=(8,6))
    ax = sns.lineplot(x=df.year, y=df.GDP, hue=df.country,marker="o")
    ax.set_xlabel("Year",size=12)
    ax.set_xbound(lower=None, upper=2016)
    ax.set_ylabel("GDP in Trillions of Dollars", size=10)
    ax.set_title('GDP between 2000 and 2015',size=12)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    st.pyplot(fig)

    # GDP Facet line plots
    st.markdown('''Next, faceted line plots can be utilised to compare year on year growth/shrinkage for each country \
                with appropriate scaling:''')
    plt.figure(figsize=(16,8))
    fig = sns.FacetGrid(df, col="country", col_wrap=3,
                        hue = "country", sharey = False)
    fig = (fig.map(sns.lineplot,"year","GDP",marker="o")
            .add_legend()
            .set_axis_labels("Year","GDP"))
    ax.xaxis.set_label_coords(.5, -.1)
    st.pyplot(fig)


    # Life Expectancy at Birth
    st.markdown('#### Life Expectancy at Birth')
    st.markdown('''
                The line plot below shows `Life Expectancy at Birth` broken down by country over the 15 year period.\n
                Of the six countries, Zimbabwe has seen the biggest increase of 14 years.
                ''')
    fig = plt.figure(figsize=(8,6))
    ax = sns.lineplot(x=df.year,y=df.life_expectancy,hue=df.country,marker="o")
    ax.set_xlabel("Year",size=12)
    ax.set_xbound(lower=None, upper=2016)
    ax.set_ylabel("Life Expectancy at Birth", size=10)
    ax.set_title('Life Expectancy at Birth has increased for all countries over this 15 year period',size=12)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    st.pyplot(fig)

    # Facet line plots
    st.markdown('''Next, faceted line plots can be utilised to compare year on year for each country \
                with appropriate scaling:''')
    plt.figure(figsize=(16,8))
    fig = sns.FacetGrid(df, col="country", col_wrap=3,
                        hue = "country", sharey = False)
    fig = (fig.map(sns.lineplot,"year","life_expectancy",marker="o")
            .add_legend()
            .set_axis_labels("Year","Life expectancy at birth (years)"))
    st.pyplot(fig)
    st.markdown('''
                Looking at the facet plots, above, it is apparent that Chile and Mexico seemed to have dips in their life expectancy around the \
                same time which could be looked into further. This type of plotting proves useful since much \
                of these nuances were lost when the y axis was shared among the countries. \
                Also, the seemingly linear changes were not as smooth for some of the countries.
                ''')
