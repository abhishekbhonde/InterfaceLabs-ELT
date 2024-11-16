import pandas as pd

def transform_data():
    # Load payment report
    payment_report = pd.read_csv('../data/payment.csv')
    
    # Debugging: Print column names
    print("Payment Report Columns:", payment_report.columns)
    
    # Clean payment report
    payment_report = payment_report[payment_report['type'] != 'Transfer']  # Updated column name
    payment_report.rename(columns={'type': 'Payment Type'}, inplace=True)
    payment_report['Transaction Type'] = 'Payment'

    # Load merchant tax report
    mtr_report = pd.read_excel('../data/marchent.xlsx')
    mtr_report = mtr_report[mtr_report['Transaction Type'] != 'Cancel']
    mtr_report['Transaction Type'] = mtr_report['Transaction Type'].replace({
        'Refund': 'Return',
        'FreeReplacement': 'Return'
    })

    # Merge datasets
    merged_data = pd.concat([payment_report, mtr_report], ignore_index=True)
    merged_data.to_csv('../data/merged_data.csv', index=False)
    print("Transformation complete! Merged data saved to '../data/merged_data.csv'.")

if __name__ == "__main__":
    transform_data()
