import pandas as pd

# Load the merged dataset
data = pd.read_csv('../data/merged_data.csv')

# Display basic information about the dataset
print("Dataset Information:")
print(data.info())

# Display basic statistics
print("\nDataset Statistics:")
print(data.describe())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Analyze unique values in key columns
print("\nUnique Payment Types:")
print(data['payment_type'].value_counts())

print("\nUnique Transaction Types:")
print(data['transaction_type'].value_counts())
