# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Loading Data & Descriptive Stats
def load_data():
    '''
    Loads the data and renames the columns ready for analysis.
    '''
    df = pd.read_csv('all_data.csv')
    df.columns = ['country', 'year', 'life_expectancy', 'GDP']
    return df

def info():
    df = pd.read_csv('all_data.csv')
    return df.info()

# Distplots
def GDP_dist_plot():
    '''
    Creates a dist plot for GDP
    '''
    df = load_data()
    plt.figure(figsize=(3,3))
    ax1 = sns.displot(df.GDP, rug = True, kde=False)
    plt.xlabel("GDP in Trillions of U.S. Dollars")
    plt.title("GDP is right skewed between 2000 and 2015",loc='left')
    plt.show()
    st.pyplot(ax1)

def life_expectancy_distplot():
    '''
    Creates a dist plot for Life Expectancy at Birth
    '''
    df = load_data()
    plt.figure(figsize=(8,6))
    ax2 = sns.displot(df.life_expectancy, rug = True, kde=False)
    plt.xlabel("Life Expectacny at Birth (Years)")
    plt.title("Life Expectancy at Birth is left skewed between 2000 and 2015")
    plt.show()
    st.pyplot(ax2)

# Bar Charts

def GDP_bar():
    '''
    Creates a GDP bar chart
    '''
    df = load_data()
    dfMeans = df.drop("year", axis = 1).groupby("country").mean().reset_index()
    fig, ax = plt.subplots()
    plt.figure(figsize=(8,6))
    ax = sns.barplot(x ='GDP',y = 'country',data=dfMeans,order=dfMeans.sort_values('GDP').country,ax=ax)
    for i in ax.containers:
        ax.bar_label(i,)
    ax.set_xlabel('Average GDP in trillions of dollars')
    ax.set_ylabel('Country')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_xticks([])
    ax.set_xticklabels([])
    st.pyplot(fig)

def life_expectancy_bar():
    '''
    Creates a life expectancy bar chart
    '''
    df = load_data()
    dfMeans = df.drop("year", axis = 1).groupby("country").mean().reset_index()
    fig2, ax2 = plt.subplots()
    plt.figure(figsize=(8,6))
    ax2 = sns.barplot(x ='life_expectancy',
                      y = 'country',
                      data=dfMeans,
                      order=dfMeans.sort_values('life_expectancy').country,ax=ax2)
    for i in ax2.containers:
        ax2.bar_label(i,)
    ax2.set_xlabel('Average Life Expectancy at Birth (Years)')
    ax2.set_ylabel('Country')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.set_xticks([])
    ax2.set_xticklabels([])
    st.pyplot(fig2)

# Violin and Swarm Charts

def violin_plot():
    '''
    Creates a violin chart for GDP and Life Expectancy
    '''
    df = load_data()
    fig, (ax1,ax2) = plt.subplots(1, 2, sharey=True, figsize=(9, 6))
    ax1 = sns.violinplot(ax=ax1, x=df.GDP, y=df.country)
    ax1.set_xlabel("GDP in Trillions of U.S. Dollars",size=13)
    ax1.set_ylabel('Country',size=13)
    ax1.xaxis.set_label_coords(.5, -.1)
    ax2 = sns.violinplot(ax=ax2, x=df.life_expectancy, y=df.country)
    ax2.set_ylabel('Country',size=13)
    ax2.set_xlabel("Life expectancy at birth (years)",size=13)
    ax2.xaxis.set_label_coords(.5, -.1)
    st.pyplot(fig)

def swarm_violin_plot():
    '''
    Creates a swarm plot over a violin plot
    '''
    df = load_data()
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

def GDP_line_plot():
    '''
    Creates a line plot for GDP.
    '''
    df = load_data()
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

def life_expectancy_line_plot():
    '''
    Creates a line plot for life expectancy.
    '''
    df=load_data()
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

def GDP_facet_plot():
    '''
    Creates a facet plot for GDP, broken down by country.
    '''
    df = load_data()
    fig = plt.figure(figsize=(16,8))
    fig = sns.FacetGrid(df, col="country", col_wrap=3,
                        hue = "country", sharey = False)
    fig = (fig.map(sns.lineplot,"year","GDP",marker="o")
            .add_legend()
            .set_axis_labels("Year","GDP"))
    st.pyplot(fig)

def life_expectancy_facet_plot():
    '''
    Creates a facet plot for life expectancy, broken down by country.
    '''
    df = load_data()
    fig = plt.figure(figsize=(16,8))
    fig = sns.FacetGrid(df, col="country", col_wrap=3,
                        hue = "country", sharey = False)
    fig = (fig.map(sns.lineplot,"year","life_expectancy",marker="o")
            .add_legend()
            .set_axis_labels("Year","life_expectancy"))
    st.pyplot(fig)

# Scatter Plots

def scatter_plot():
    '''
    Creates a scatter plot for life expectancy and GDP.
    '''
    df = load_data()
    fig = plt.figure(figsize=(9,6))
    ax = sns.scatterplot(x=df.life_expectancy,y=df.GDP,hue=df.country)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.title('Life Expectancy at Birth vs GDP',size=15)
    plt.xlabel('Life Expectancy at Birth',size=13)
    plt.ylabel('GDP in Trillions of Dollars',size=13)
    st.pyplot(fig)

def facet_scatter():
    '''
    Creates a facet scatter plot for GDP and life expectancy.
    '''
    df = load_data()
    scatter = sns.FacetGrid(df,col="country",col_wrap=3,
                      hue = "country", sharey = False, sharex = False)
    scatter = (scatter.map(sns.scatterplot,"life_expectancy", "GDP")
         .add_legend()
         .set_axis_labels("Life expectancy at birth (years)", "GDP in Trillions of U.S. Dollars"))
    st.pyplot(scatter)
