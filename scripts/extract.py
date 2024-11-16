import pandas as pd

def load_datasets():
    # Updated file paths
    payment_report_path = '../data/payment.csv'
    mtr_report_path = '../data/marchent.xlsx'  # Updated file name
    
    # Read datasets
    payment_report = pd.read_csv(payment_report_path)
    mtr_report = pd.read_excel(mtr_report_path)
    
    return payment_report, mtr_report

if __name__ == "__main__":
    payment_report, mtr_report = load_datasets()
    print("Payment Report:")
    print(payment_report.head())
    print("\nMerchant Tax Report:")
    print(mtr_report.head())
