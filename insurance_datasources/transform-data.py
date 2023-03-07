import logging
import sys, json
import os
import pandas as pd
from sklearn import preprocessing

def getColNames(df, col):
    """
    Function to  do a case insensitve search for column names in dataframe 
    corresponding to the ones given in col and return the output
    
    Parameters
    ----------
    dataframe: dataframe,
        Dataframe frome which the column names must be take
    col: str, list
        Column names to search for in the dataframe
        
    Returns
    -------
        A list/string of column names from dataframe corresponding to the one(s) given in col
    """
    if type(col) == list:
        col = list(map(lambda x: x.lower(), col))
        return [x for x in df.columns if x.lower() in col]
    col = col.lower()
    return [x for x in df.columns if x.lower() == col][0]

DEFAULT_MODEL_NAME = "model"
class Transformer():
    def preprocess(self, dataframe):
        data_to_preprocess = dataframe 
        col_search = ['sex', 'smoker', 'region']
        for col in getColNames(dataframe,col_search):
            if (data_to_preprocess[col].dtype == 'object'):
                le = preprocessing.LabelEncoder()
                le = le.fit(data_to_preprocess[col])
                data_to_preprocess[col] = le.transform(data_to_preprocess[col])
                print('Completed Label encoding on',col)
        preprocessed_data = data_to_preprocess
        return preprocessed_data

    def postprocess(self, dataframe):
        pass

