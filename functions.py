# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    df = pd.read_csv('all_data.csv')
    return df

def info():
    df = pd.read_csv('all_data.csv')
    return df.info()

def GDP_displot():
    df = pd.read_csv('all_data.csv')
    # GDP displot
    plt.figure(figsize=(8,6))
    sns.displot(df.GDP, rug = True, kde=False)
    plt.xlabel("GDP in Trillions of U.S. Dollars")
    plt.show()
    
