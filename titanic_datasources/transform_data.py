def getColNames(dataframe, col):
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

class Transformer():
    def preprocess(self,dataframe):
        import pandas as pd
        data_to_preprocess = dataframe
        age = getColNames(dataframe,"Age")
        data_to_preprocess[age].fillna(value=data_to_preprocess[age].median(), inplace=True)
        features = getColNames(dataframe,["Pclass", "Sex", "SibSp", "Parch"])
        train_df = pd.get_dummies(data_to_preprocess[features])
        data_to_preprocess = pd.concat([data_to_preprocess[getColNames(dataframe,["Age", "Fare", "Survived", "PassengerId","timestamp"])], train_df], axis=1)
        preprocessed_data = data_to_preprocess
        return preprocessed_data
