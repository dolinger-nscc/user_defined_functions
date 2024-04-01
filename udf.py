import pandas as pd
import numpy as np
from datetime import datetime

def gen_unseen_pct(data, frac = 0.2, random_state = np.random.seed(None)):
    '''This function takes 3 arguments:
    data is the Pandas DataFrame that is to be split
    frac is the percentage to be randomly sampled and used as a "set-aside" dataset (default is 20%)
    random_state is the random_state you would like to use for reproducibility while testing (default is a random seed)
    
    Returns two DataFrames:
    1st df is larger remainder of the frac (fractional set)
    2nd df is the fractional set (i.e. 20% by default)'''
    unseen_data = data.sample(frac=frac, random_state=random_state)
    df = data.drop(unseen_data.index)
    return df, unseen_data

def gen_balanced_sample(data, series, random_state = np.random.seed(None)):
    '''This function takes 3 arguments:
    data is the Pandas DataFrame that is to be balanced by category
    series is the series to be balanced by category (will attempt to return the number of the minimum category count)
    random_state is the random_state you would like to use for reproducibility while testing (default is a random seed)
    
    Returns one DataFrame and one summary of your series count (using value_counts):
    Use tuple unpacking:
    1st object is the DataFrame
    2nd object is the Series Summary'''
    
    samples = data[series].value_counts().min()
    df = data.groupby(series).apply(lambda x: x.sample(n=min(len(x), samples))).reset_index(drop=True)
    return df, df[series].value_counts()

def what_time():
    '''Test function that returns the current system time in hours, minutes, and seconds.'''
    return datetime.now().strftime('%H:%M:%S')
