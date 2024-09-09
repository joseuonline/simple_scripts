import ofxparse
import csv
import os
import tkinter as tk
from tkinter import filedialog

def parse_ofx_qfx(file_path):
    """
    Parse OFX or QFX file and return transactions as a list of dictionaries.
    """
    with open(file_path) as file:
        ofx = ofxparse.OfxParser.parse(file)
    
    transactions = []
    for account in ofx.accounts:
        for transaction in account.statement.transactions:
            transactions.append({
                'date': transaction.date,
                'amount': transaction.amount,
                'payee': transaction.payee,
                'memo': transaction.memo,
                'checknum': transaction.checknum,
                'type': transaction.type,
            })
    
    return transactions

def export_to_csv(transactions, output_csv):
    """
    Export list of transactions to a CSV file.
    """
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=transactions[0].keys())
        writer.writeheader()
        for transaction in transactions:
            writer.writerow(transaction)

def select_file():
    """
    Open a file dialog for the user to select an OFX or QFX file.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    file_path = filedialog.askopenfilename(
        title="Select OFX or QFX file",
        filetypes=[("OFX files", "*.ofx"), ("QFX files", "*.qfx")]
    )
    return file_path

def main():
    input_file = select_file()  # Prompt the user to select a file
    if not input_file or not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return

    # Extract the file name and replace the extension with .csv
    output_file = os.path.splitext(input_file)[0] + ".csv"

    transactions = parse_ofx_qfx(input_file)
    export_to_csv(transactions, output_file)
    print(f"Transactions have been exported to {output_file} successfully.")

if __name__ == "__main__":
    main()
