import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import tempfile
import os
from datetime import datetime

# Load the data
data = pd.read_csv('../data/merged_data.csv')

# Convert date columns to datetime format
data['date/time'] = pd.to_datetime(data['date/time'], errors='coerce')

# Clean 'total' and 'Invoice Amount' columns (remove commas and convert to float)
data['total'] = data['total'].replace({',': ''}, regex=True).astype(float)
data['Invoice Amount'] = data['Invoice Amount'].replace({',': ''}, regex=True).astype(float)

# Sidebar Filters
st.sidebar.header("Filters")

# Date filter
start_date, end_date = st.sidebar.date_input(
    "Select Date Range",
    [data['date/time'].min().date(), data['date/time'].max().date()]
)

# Filter data based on date
filtered_data = data[
    (data['date/time'] >= pd.to_datetime(start_date)) &
    (data['date/time'] <= pd.to_datetime(end_date))
]

# Payment type filter
payment_filter = st.sidebar.multiselect(
    "Select Payment Types",
    options=filtered_data['Payment Type'].unique()
)

if payment_filter:
    filtered_data = filtered_data[filtered_data['Payment Type'].isin(payment_filter)]

# Transaction type filter
transaction_filter = st.sidebar.multiselect(
    "Select Transaction Types",
    options=filtered_data['Transaction Type'].unique()
)

if transaction_filter:
    filtered_data = filtered_data[filtered_data['Transaction Type'].isin(transaction_filter)]
 
# Main Dashboard
st.title("Transaction Analysis Dashboard")
st.write("This dashboard provides insights into the transaction data.")

# Display filtered data
st.subheader("Filtered Data")
st.write(filtered_data)

# Visualization 1: Daily Transactions Line Chart
st.subheader("Daily Transactions Trend")
daily_transactions = filtered_data.groupby(filtered_data['date/time'].dt.date).size()
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(daily_transactions.index, daily_transactions.values, marker='o', linestyle='-', color='b')
ax.set_title("Daily Transactions")
ax.set_xlabel("Date")
ax.set_ylabel("Number of Transactions")
st.pyplot(fig)

# Visualization 2: Pie Chart for Payment Types
st.subheader("Proportion of Payment Types")
payment_counts = filtered_data['Payment Type'].value_counts()
fig, ax = plt.subplots()
ax.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Visualization 3: Heatmap for Correlations
st.subheader("Correlation Heatmap")
numerical_columns = ['total', 'Invoice Amount']
correlation = filtered_data[numerical_columns].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Allow users to download filtered data as CSV
st.subheader("Download Filtered Data as CSV")
csv = filtered_data.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)

# Function to generate and download a PDF
def generate_pdf():
    # Initialize PDF
    pdf = FPDF()
    pdf.add_page()

    # Title in PDF
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Transaction Data Analysis Report", ln=True, align='C')

    # Add filtered data as a table in the PDF
    pdf.ln(10)  # Line break
    pdf.set_font("Arial", size=10)
    
    # Dynamically set column widths based on the number of columns
    num_columns = len(filtered_data.columns)
    col_width = 180 / num_columns  # Adjust the width dynamically based on the number of columns

    # Add column headers
    columns = filtered_data.columns.tolist()
    for col in columns:
        pdf.cell(col_width, 10, col, border=1, align='C')
    pdf.ln()  # Line break after header

    # Add rows (filtered data)
    for i, row in filtered_data.iterrows():
        for value in row:
            pdf.cell(col_width, 10, str(value), border=1, align='C')
        pdf.ln()  # Line break after each row

    # Your previous code to generate the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    daily_transactions = filtered_data.groupby(filtered_data['date/time'].dt.date).size()
    ax.plot(daily_transactions.index, daily_transactions.values, marker='o', linestyle='-', color='b')
    ax.set_title("Daily Transactions")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Transactions")

    # Save plot to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    plt.savefig(temp_file.name)
    plt.close(fig)  # Close the figure after saving the image

    # Add image to PDF
    pdf.image(temp_file.name, x=10, w=180)

    # Clean up: remove the temporary file after adding it to the PDF
    os.remove(temp_file.name)

    # Output the PDF data (return it or save it to a file as needed)
    pdf_output = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(pdf_output.name)

    # Returning the PDF file path
    return pdf_output.name

# Allow users to download the PDF
st.subheader("Download Report as PDF")
pdf_data = generate_pdf()
with open(pdf_data, "rb") as pdf_file:
    st.download_button(
        label="Download PDF",
        data=pdf_file,
        file_name="report.pdf",
        mime="application/pdf"
    )

