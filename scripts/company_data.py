import pandas as pd
import numpy as np

def get_company_data():
    """
    Returns a dictionary containing the toy company's data.
    """
    # Define the balance sheet data
    data = {
        'ARC-US': {
            'Fixed Income (FI)': 800,
            'Equities (E)': 200,
            'Recoverables (Recov)': 50,
            'Other Assets (OA)': 50,
            'Reserves (Res)': 700,
            'Capital (C)': 400
        },
        'ARC-BM': {
            'Fixed Income (FI)': 1500,
            'Equities (E)': 300,
            'Recoverables (Recov)': 100,
            'Other Assets (OA)': 100,
            'Reserves (Res)': 1200,
            'Capital (C)': 800
        }
    }

    # Convert to DataFrame for better structure
    df_balance_sheet = pd.DataFrame(data)

    # Define initial loss allocation (L^0) for the "Florida Hurricane" scenario
    initial_loss_allocation = {
        'ARC-US': 250,
        'ARC-BM': 50
    }
    
    # Convert to pandas Series for easy access
    s_initial_loss_allocation = pd.Series(initial_loss_allocation)

    return {
        'balance_sheet': df_balance_sheet,
        'initial_loss_allocation': s_initial_loss_allocation
    }

if __name__ == '__main__':
    company_data = get_company_data()
    print("Balance Sheet (in M$):")
    print(company_data['balance_sheet'])
    print("\nInitial Loss Allocation (in M$):")
    print(company_data['initial_loss_allocation'])
