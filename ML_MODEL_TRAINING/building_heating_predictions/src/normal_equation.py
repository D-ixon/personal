import pandas as pds
import numpy as np

train_ds = pds.read_csv('data/training_dataset.csv')
test_ds = pds.read_csv('data/test_dataset.csv')

X = train_ds.drop(columns=['ID', 'Y1'])
y = train_ds['Y1']

X_array = X.to_numpy()
y_array = y.to_numpy()

print(X_array.shape)