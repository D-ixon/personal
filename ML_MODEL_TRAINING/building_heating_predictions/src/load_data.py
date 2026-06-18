import pandas as pds

train = pds.read_csv('data/Training_dataset.csv')
test = pds.read_csv('data/test_dataset.csv')

print(train.head())
print(test.head())

print(f"Training dataset shape: {train.shape}")
print(f"Test dataset shape: {test.shape}")
