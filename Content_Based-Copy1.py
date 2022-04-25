import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse

'''
 This one is for Popularity Learning
'''

def country_popularity(data, country):
    country_recsys = data[data['Country'].isin(country)]
    country_recsys['Unique_ISBN'].value_counts()[:10]
    print(country_recsys['Unique_ISBN'].value_counts()[:10])

