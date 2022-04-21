import pandas as pd

# Modules for data visualization
import seaborn as sns
import missingno as msno
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import squarify
import geopandas as gpd
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

def create_array_for_drawing(user):
    country = user.Country.value_counts()

    coun = {}
    for idx, val in country.items():
        l = idx.split(',')
        for i in l:
            i = i.strip()
            if i in coun.keys():
                d = {}
                d[i] = val + coun[i]
                coun.update(d)
            else:
                d = {i:val}
                coun.update(d)

    nation, count = [],[]
    for idx, val in coun.items():
        nation.append(idx)
        count.append(val)

    return (pd.DataFrame({'country':nation, 'count': count})
            .sort_values('count', ascending = False))

def plot_box_country(df):
    temp = create_array_for_drawing(df)
    temp['color'] = temp['count'].apply(lambda x : '#b20710' if x > temp['count'].values[3] else 'grey')
    # visulaization
    fig, ax = plt.subplots(figsize = (18,8), dpi = 60)
    fig.patch.set_facecolor('#f6f5f5')
    ax.set_facecolor('#f6f5f5')

    bar_kawrgs = {'edgecolor':'#f6f5f5'}
    squarify.plot(sizes= temp['count'][0:10], label = temp['country'][0:10], ax = ax, color = temp['color'],  **bar_kawrgs,
                text_kwargs = {'font':'serif', 'size':13, 'color':'black', 'weight':'bold', 'alpha':0.8},alpha = 0.9)

    ax.text(0,115,'TOP 10 countries have the highest number of reader',{'font':'serif', 'size':35, 'color':'black', 'weight':'bold'}, alpha = 1)

    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    for loc in ['left','right','top', 'bottom']:
        ax.spines[loc].set_visible(False)

    fig.show()

def plot_world_map(df):
    temp = create_array_for_drawing(df)
    temp['color'] = temp['count'].apply(lambda x : '#b20710' if x > temp['count'].values[30] else 'grey')

    #loading geodataframe
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    #converting country names to iso codes
    temp['iso_code'] = coco.convert(names=temp['country'], to ='ISO3')
    temp = temp[temp['iso_code'] != 'not found']

    # merging geodataframe and pandas dataframe
    temp_map = world.merge(temp,left_on = 'iso_a3', right_on = 'iso_code')

    temp_map.drop(columns = ['continent', 'gdp_md_est','pop_est','name',], inplace = True)
    temp_map = temp_map.sort_values(by = 'count', ascending = False)


    #viualization
    colors = ['grey','#f8f9f9','#b20710']
    cmap  = matplotlib.colors.LinearSegmentedColormap.from_list("", colors = colors)

    fig, ax  = plt.subplots(figsize = (15,7.5), dpi = 80)
    fig.patch.set_facecolor('#f6f5f5')
    ax.set_facecolor('#f6f5f5')
    temp_map.dropna().plot(column = 'count', 
                        color = temp_map.dropna()['color'], 
                        cmap = cmap,
                        scheme='quantiles', 
                        k=10, legend = False,
                        ax = ax)

    for loc in ['left','right','top','bottom']:
        ax.spines[loc].set_visible(False)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    fig.show()

def draw_top_chart(data, x, y_list, title):
    fig, ax1 = plt.subplots(figsize=(20, 10))
    plt.xticks(rotation=90)

    palette = sns.color_palette("RdBu", len(data))

    sns.barplot(x=x, y=y_list[0], data=data, palette=palette, ax=ax1)
    ax1.set_title(title, fontsize=30, fontweight = 'bold')

    ax2 = ax1.twinx()
    sns.scatterplot(x=x, y=y_list[1], data=data, color='black', ax=ax2)

    plt.show()