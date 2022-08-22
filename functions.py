# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    df = pd.read_csv('all_data.csv')
    return df.head()
