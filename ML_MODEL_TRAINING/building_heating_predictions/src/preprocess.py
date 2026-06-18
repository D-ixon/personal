from sklearn.preprocessing import StandardScaler
from load_data import train, test
import pandas as pds


def preprocess_data(train, test):

    X = train.drop(columns=['Y1', 'ID'], axis=1)
    y = train['Y1']
    
    X_test = test.drop(columns=['ID'], axis=1)
    
    scaler = StandardScaler()
    
    X_scaled = scaler.fit_transform(X).values
    X_test_scaled = scaler.transform(X_test).values
    
    return X_scaled, X_test_scaled, y.values
