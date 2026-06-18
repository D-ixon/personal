import pandas as pds
import os

# Get the directory where load_data.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path dynamically
train_path = os.path.join(base_dir, '..', 'data', 'Training_dataset.csv')
test_path = os.path.join(base_dir, '..', 'data', 'test_dataset.csv')

train_df = pds.read_csv(train_path)
test_df = pds.read_csv(test_path)