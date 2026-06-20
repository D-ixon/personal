from sklearn.preprocessing import StandardScaler
""""

def preprocess_data(train, test):

    X = train.drop(columns=['Y1', 'ID'])

    y = train['Y1']

    X_test = test.drop(columns=['ID'])

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    X_test_scaled = scaler.transform(X_test)

    return X_scaled, X_test_scaled, y.values, scaler
    """


def preprocess_data(train_df, test_df):
    # 1. Separate features (X) and target (y)
    X_train = train_df.drop(columns=['Y1', 'ID'])
    y_train = train_df['Y1']
    X_test = test_df.drop(columns=['ID'])
    
    # 2. Initialize the scaler
    scaler = StandardScaler()
    
    # 3. Fit on Training data, then transform both
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test) # Note: Only use .transform() here!
    
    return X_train_scaled, X_test_scaled, y_train, scaler