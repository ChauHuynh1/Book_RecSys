import pandas as pd

# Modules for data visualization
import seaborn as sns
import missingno as msno
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from wordcloud import WordCloud, STOPWORDS
from dataprep.clean import validate_country
import squarify
import geopandas as gpd #Map
import country_converter as coco
import matplotlib

def missing_percentage(df):
    """This function takes a DataFrame(df) as input and returns two columns, total missing values and total missing values percentage"""
    total = df.isnull().sum().sort_values(ascending=False)[df.isnull().sum().sort_values(ascending=False) != 0]
    percent = round(df.isnull().sum().sort_values(ascending=False) / len(df) * 100, 2)[
        round(df.isnull().sum().sort_values(ascending=False) / len(df) * 100, 2) != 0]
    return pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

def draw_missing_plot(df):
    # display missing values in descending
    print("Missing values in the user dataframe in descending: \n", missing_percentage(df).sort_values(by='Total', ascending=False))

    # visualize where the missing values are located
    msno.matrix(df, color=(255 / 255, 192 / 255, 203 / 255))
    pink_patch = mpatches.Patch(color='pink', label='present value')
    white_patch = mpatches.Patch(color='white', label='absent value')
    plt.legend(handles=[pink_patch, white_patch])
    plt.show()

def whitespace_remover(df):
    """
    The function will remove extra leading and trailing whitespace from the data.
    """
    # iterating over the columns
    for i in df.columns:
        # checking datatype of each columns
        if df[i].dtype == 'object' or df[i].dtype == 'str':
            # applying strip function on column
            df[i] = df[i].map(str.strip)
        else:
            # if condition is False then it will do nothing.
            pass

def check_content(df, column_name):
    categories = list(df[column_name].value_counts().index)
    for x in range(len(categories)):
        print (categories[x])


def plot_density_rating(df):
    # sns.displot(train, x="Survived", hue="Pclass", kind="kde", fill=True)
    plot = sns.displot(df, x="Book_Rating", kind="kde", fill=True, color='blue', height= 14)

    # plot = sns.countplot(x="Book_Rating", data=rating)

    plot.fig.suptitle("Distribution of Rating", fontsize=25, y=1.08, fontweight = 'bold')
    plot.set_xlabels("Rating", fontsize = 20, fontweight = 'bold' )
    plot.set_ylabels("Density", fontsize = 20, fontweight = 'bold')

def plot_number_of_rating_point(rating):
    fig, ax = plt.subplots(figsize = (20,15), dpi = 90)

    a = rating['Book_Rating'].value_counts().sort_index()
    colors = ['grey','grey','grey','grey','grey','grey','grey','#b20710','grey','grey','grey','grey','grey','grey']
    ax.bar(x = a.index, height = a.values, color = colors, alpha = 0.9)

    # Create labels
    label = a.values.tolist()
    
    # Text on the top of each bar
    for i in range(len(label)):
        x = i + 0.25
        y = (i+18)/2 + label[i]
        x = x+0.4
        y = y + 55
        ax.text(x,y, '{}'.format(a.values[i]),{'font': 'serif', 'weight': 'normal', 'color': 'black', 'fontsize': 20}, alpha = 0.8)

    ax.axes.get_yaxis().set_visible(False)
    fig.show()