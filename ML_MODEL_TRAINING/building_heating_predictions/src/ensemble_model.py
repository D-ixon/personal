import pandas as pd
import numpy as np
from load_data import train_df, test_df
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

def load_and_prepare_data(train_df):
    """Loads dataset and separates features and target."""
    df = pd.read_csv(train_df)
    # Isolate input features and target
    X = df.drop(columns=['ID', 'Y1'])
    y = df['Y1']
    return X, y

def main():
    print("=" * 50)
    print("INITIALIZING ENSEMBLE OPTIMIZATION")
    print("=" * 50)

    # 1. Load Data (Make sure your CSV path is correct for your workspace)
    # Adjust "Training_dataset.csv" if your file is named differently
    X, y = load_and_prepare_data("Training_dataset.csv")

    # 2. Split the Data (The "Leap of Faith")
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    # 3. Define the Architectures
    models = {
        "Linear Baseline": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42)
    }

    # 4. Train and Evaluate
    print("\nTraining models and calculating RMSE...\n")
    results = {}
    
    for name, model in models.items():
        # Train the model
        model.fit(X_train, y_train)
        
        # Predict on the validation set
        predictions = model.predict(X_valid)
        
        # Calculate RMSE
        rmse = np.sqrt(mean_squared_error(y_valid, predictions))
        results[name] = rmse
        
        print(f"[{name}] RMSE: {rmse:.4f}")

    # 5. Identify the Winner
    best_model = min(results, key=results.get)
    print("-" * 50)
    print(f"OPTIMIZATION COMPLETE.")
    print(f"Best Performing Architecture: {best_model} (RMSE: {results[best_model]:.4f})")
    print("-" * 50)

if __name__ == "__main__":
    main()