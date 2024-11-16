import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the merged data
data = pd.read_csv('../data/merged_data.csv')

# Normalize column names to lowercase and remove leading/trailing spaces
data.columns = data.columns.str.strip().str.lower()

# Define the relevant date column
date_column = 'invoice date'

# Check if the date column exists
if date_column in data.columns:
    # Convert the date column to datetime format
    data[date_column] = pd.to_datetime(data[date_column], errors='coerce')

    # Drop rows with invalid or missing dates
    data = data.dropna(subset=[date_column])

    # Set the date column as the index for time-based analysis
    data.set_index(date_column, inplace=True)

    # Resample the data to aggregate daily transactions
    if 'total' in data.columns:
        daily_transactions = data['total'].resample('D').sum()

        # Plot the line chart for daily transactions
        plt.figure(figsize=(10, 5))
        daily_transactions.plot(kind='line', title='Daily Transactions')
        plt.xlabel('Date')
        plt.ylabel('Total')
        plt.grid(True)
        plt.savefig('../data/daily_transactions.png')  # Save plot as an image
        print("Daily transactions plot saved as 'daily_transactions.png'.")
    else:
        print("The 'total' column is missing in the dataset.")
else:
    print(f"The specified date column '{date_column}' is not in the dataset.")

# Visualize the distribution of payment types
if 'payment type' in data.columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=data, x='payment type')
    plt.title('Payment Type Distribution')
    plt.xlabel('Payment Type')
    plt.ylabel('Count')
    plt.grid(True)
    plt.savefig('../data/payment_type_distribution.png')  # Save plot as an image
    print("Payment type distribution plot saved as 'payment_type_distribution.png'.")
else:
    print("The 'payment type' column is missing in the dataset.")
