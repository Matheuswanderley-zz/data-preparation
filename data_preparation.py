import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import numpy.random as nr
import math
from IPython import get_ipython

ipy = get_ipython()
if ipy  is not None:
    ipy.run_line_magic('matplotlib', 'inline')
    # executa o csv e imprime as 20 primeiras linhas
    auto_prices = pd.read_csv('Automobile price data _Raw_.csv')
    auto_prices.head(20)

    auto_prices.columns = [str.replace('-', '_') for  str in auto_prices.columns]
    (auto_prices.astype(np.object) == '?').any()
    auto_prices.dtypes

    for col in auto_prices.columns:
        if auto_prices[col].dtype == object:
            count = 0
            count = [count + 1  for x in auto_prices[col] if x == '?']
            print(col + ' ' + str(sum(count)))
    
    
    auto_prices.drop('normalized_losses', axis = 1, inplace = True)
    cols = ['price', 'bore', 'stroke',
            'horsepower', 'peak_rpm']
    for column in cols:
        auto_prices.loc[auto_prices[column] == '?', column] = np.nan
    auto_prices.dropna(axis = 0, inplace = True)
    auto_prices.shape

    for column in cols:
        auto_prices[column] = pd.to_numeric(auto_prices[column])
    auto_prices[cols].dtypes

    auto_prices['num_of_cylinders'].value_counts()

    cylinder_categories = {'three':'three_four', 'four':'three_four', 
                    'five':'five_six', 'six':'five_six',
                    'eight':'eight_twelve', 'twelve':'eight_twelve'}
    auto_prices['num_of_cylinders'] = [cylinder_categories[x] for x in auto_prices['num_of_cylinders']]
    auto_prices['num_of_cylinders'].value_counts()


def plot_box(auto_prices, col, col_y = 'price'):
    sns.set_style("whitegrid")
    sns.boxplot(col, col_y, data=auto_prices)
    plt.xlabel(col) # Set text for the x axis
    plt.ylabel(col_y)# Set text for y axis
    plt.show()

    plot_box(auto_prices, 'num_of_cylinders')