import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    df = df.drop(['RowNumber','CustomerId','Surname'], axis=1)
    df = pd.get_dummies(df, columns=['Geography','Gender'], drop_first=True)
    return df