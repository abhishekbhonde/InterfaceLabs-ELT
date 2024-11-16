# Transaction Analysis Dashboard

This project implements an interactive dashboard for visualizing transaction data using Streamlit, with various filters and charts to help analyze trends and insights from the dataset. The dashboard also includes features for exporting data and generating reports as PDFs.

## Features

- **Sidebar Filters**: Filter data based on date range, payment type, and transaction type.
- **Visualizations**:
  - **Daily Transactions Trend**: A line chart showing daily transactions.
  - **Payment Type Distribution**: A pie chart visualizing the distribution of payment types.
  - **Correlation Heatmap**: A heatmap showing correlations between transaction values.
- **Export Options**:
  - **Download Data as CSV**: Export the filtered data to a CSV file.
  - **Download Reports as PDF**: Generate and download a PDF report containing visualizations.

## Prerequisites

Ensure you have the following software installed:

- Python (>= 3.7)
- Git (for version control and repository management)

## Dependencies

The project requires the following Python libraries:

- `streamlit`: For building the interactive dashboard.
- `pandas`: For data processing and manipulation.
- `matplotlib`: For creating visualizations.
- `seaborn`: For generating statistical plots.
- `fpdf`: For generating PDF reports.
- `datetime`: For handling date-related operations.

You can install the required libraries by running:

```bash
pip install -r requirements.txt
```

## Installation and Setup

Step 1: Clone the Repository
Clone the repository to your local machine using Git:

```
git clone https://github.com/yourusername/transaction-analysis-dashboard.git

cd transaction-analysis-dashboard
```

Step 2: Install Dependencies

After cloning the repository, install the required Python packages listed in requirements.txt:

```
pip install -r requirements.txt
```

Step 3: Data Preparation

```
Make sure the transaction dataset (merged_data.csv) is available in the data folder of the project. If you don't have the dataset yet, you can modify the code to load the data from your own source.
```

Step 4: Run the Dashboard
Once the dependencies are installed and the data is in place, you can run the Streamlit app by executing the following command:

```

streamlit run dashboard.py
```

This will start a local server, and you can view the dashboard in your browser by navigating to ` http://localhost:8501.`

```
How It Works
1. Loading Data
The dashboard reads transaction data from a CSV file (merged_data.csv) and processes it to generate insights. The data should have the following columns:

date/time: The timestamp of the transaction.
Payment Type: The method used for payment (e.g., credit card, PayPal).
Transaction Type: The type of transaction (e.g., order, refund, etc.).
total: The total amount for the transaction.
Invoice Amount: The total amount invoiced.
2. Sidebar Filters
The sidebar allows users to filter the data based on:

Date Range: Filter transactions within a selected date range.
Payment Type: Filter by the method of payment.
Transaction Type: Filter by the type of transaction.
3. Visualizations
The dashboard includes the following visualizations:

Daily Transactions Trend: A line chart that shows the number of transactions per day.
Payment Type Distribution: A pie chart that shows the percentage distribution of different payment types.
Correlation Heatmap: A heatmap that shows the correlation between the total and Invoice Amount columns.
4. Exporting Data & Reports
Export Filtered Data as CSV: You can download the filtered dataset as a CSV file using the "Download Filtered Data" button.
Export Report as PDF: You can generate a PDF report with the charts and download it using the "Download PDF Report" button.
5. PDF Report Generation
The app generates a PDF report that includes:

A summary of the filtered data.
Visualizations like the daily transactions trend, payment type distribution, and correlation heatmap.
Directory Structure
plaintext
Copy code
transaction-analysis-dashboard/
├── data/                     # Folder containing the dataset (merged_data.csv)
├── dashboard.py              # Streamlit app script
├── requirements.txt          # List of required dependencies
├── README.md                 # This file
Troubleshooting
Error: KeyError: 'Payment Type'
If you encounter an error related to the Payment Type column, make sure that the dataset contains a column named Payment Type. If the column name is different, update the code to match the correct column name.
```
