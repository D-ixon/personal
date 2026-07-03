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

    DATA_FILE = "data/Training_dataset.csv" 
    TEST_FILE = "data/test_dataset.csv"
    
    try:
        df = pd.read_csv(DATA_FILE)
        test_df = pd.read_csv(TEST_FILE)
        print(f"Successfully loaded {DATA_FILE} and {TEST_FILE}")
    except FileNotFoundError:
        print(f"ERROR: Could not find the data files. Please check the names and location.")
        return

    X = df.drop(columns=['ID', 'Y1'])
    y = df['Y1']

    test_ids = test_df['ID']
    X_test = test_df.drop(columns=['ID'])

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.20, random_state=42
    )
    
    degrees_to_test = [1, 2, 3]
    best_rmse = float('inf')
    best_degree = 1
    
    for degree in degrees_to_test:
        print(f"\n--- Testing Polynomial Degree {degree} ---")
        
        poly_transformer = PolynomialFeatures(degree=degree)
        X_train_poly = poly_transformer.fit_transform(X_train)
        X_valid_poly = poly_transformer.transform(X_valid)
        
        model = LinearRegression()
        model.fit(X_train_poly, y_train)
        
        predictions = model.predict(X_valid_poly)
        rmse = np.sqrt(mean_squared_error(y_valid, predictions))
        
        print(f"Number of features after expansion: {X_train_poly.shape[1]}")
        print(f"RMSE: {rmse:.4f}")
        
        if rmse < best_rmse:
            best_rmse = rmse
            best_degree = degree

    print("\n" + "=" * 60)
    print(f"BEST POLYNOMIAL DEGREE: {best_degree} (RMSE: {best_rmse:.4f})")
    print("=" * 60)

    print(f"\nRetraining Degree {best_degree} model on full training data...")
    
    final_poly = PolynomialFeatures(degree=best_degree)
    X_full_poly = final_poly.fit_transform(X)
    X_test_poly = final_poly.transform(X_test)
    
    final_model = LinearRegression()
    final_model.fit(X_full_poly, y)
    
    test_predictions = final_model.predict(X_test_poly)
    
    submission = pd.DataFrame({
        "ID": test_ids,
        "Heating_Load": test_predictions
    })
    
    submission.to_csv("polynomial_submission.csv", index=False)
    print("\npolynomial_submission.csv has been created successfully.")
    print("Submission File Preview:")
    print(submission.head())

if __name__ == "__main__":
    main()