from sklearn.preprocessing import StandardScaler

def preprocess_data(train, test):

    X = train.drop(columns=['Y1', 'ID'])

    y = train['Y1']

    X_test = test.drop(columns=['ID'])

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    X_test_scaled = scaler.transform(X_test)

    return X_scaled, X_test_scaled, y.values, scaler