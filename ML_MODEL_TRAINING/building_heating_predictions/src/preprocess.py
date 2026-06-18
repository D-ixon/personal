from sklearn.preprocessing import StandardScaler
from load_data import train_df, test_df
import pandas as pds


def preprocess_data(train, test):

    X = train_df.drop(columns=['Y1', 'ID'], axis=1)
    y = train_df['Y1']
    
    X_test = test_df.drop(columns=['ID'], axis=1)
    
    scaler = StandardScaler()
    
    X_scaled = scaler.fit_transform(X).values
    X_test_scaled = scaler.transform(X_test).values
    
    return X_scaled, X_test_scaled, y.values
