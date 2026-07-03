import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def main():
    print("=" * 60)
    print("POLYNOMIAL REGRESSION EXPERIMENT")
    print("=" * 60)

    DATA_FILE = "data\Training_dataset.csv" 
    
    try:
        df = pd.read_csv(DATA_FILE)
        print(f"Successfully loaded {DATA_FILE}")
    except FileNotFoundError:
        print(f"ERROR: Could not find '{DATA_FILE}'. Please check the name and location.")
        return

    X = df.drop(columns=['ID', 'Y1'])
    y = df['Y1']

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.20, random_state=42
    )
    
    degrees_to_test = [1, 2, 3]
    
    for degree in degrees_to_test:
        print(f"\n--- Testing Polynomial Degree {degree} ---")
        
        # Step A: Transform the features
        poly_transformer = PolynomialFeatures(degree=degree)
        X_train_poly = poly_transformer.fit_transform(X_train)
        X_valid_poly = poly_transformer.transform(X_valid)
        
        # Step B: Feed the transformed features into a standard Linear Regression model
        model = LinearRegression()
        model.fit(X_train_poly, y_train)
        
        # Step C: Predict and Calculate RMSE
        predictions = model.predict(X_valid_poly)
        rmse = np.sqrt(mean_squared_error(y_valid, predictions))
        
        # Print results
        print(f"Number of features after expansion: {X_train_poly.shape[1]}")
        print(f"RMSE: {rmse:.4f}")

    print("\n" + "=" * 60)
    print("EXPERIMENT COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()