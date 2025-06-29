import pandas as pd
import numpy as np
from scripts.company_data import get_company_data

def calculate_naic_rbc(balance_sheet, pml_cat):
    # Provisional NAIC RBC Risk Factors
    factors = {
        'FI': 0.005,
        'E': 0.15,
        'Recov': 0.05,
        'Res': 0.05,
        'Prem': 0.01, # Assuming Premium is a risk driver, though not in balance sheet
        'Cat': 0.05  # 5% of PML
    }

    # Extract relevant balance sheet items
    fi = balance_sheet['Fixed Income (FI)']
    eq = balance_sheet['Equities (E)']
    recov = balance_sheet['Recoverables (Recov)']
    res = balance_sheet['Reserves (Res)']
    # Assuming Prem and Cat are external inputs for now, as they are not in the balance sheet
    prem = 0 # Placeholder for Premium risk driver
    cat = pml_cat # Catastrophe risk driver (PML)

    # Calculate sub-capitals (simplified for now)
    C_fi = fi * factors['FI']
    C_eq = eq * factors['E']
    C_cred = recov * factors['Recov'] # Simplified credit risk
    C_rsrv = res * factors['Res'] # Simplified reserve risk
    C_prem = prem * factors['Prem']
    C_cat = cat * factors['Cat']
    C_subsidiary = 0 # Assuming no subsidiary risk for now

    # NAIC RBC formula (simplified, assuming no subsidiary risk for now)
    rbc = np.sqrt(C_fi**2 + C_eq**2 + C_cred**2 + C_rsrv**2 + C_prem**2 + C_cat**2) + C_subsidiary
    return rbc

def calculate_bma_bscr(balance_sheet, pml_cat):
    # Provisional BMA BSCR Risk Factors
    factors = {
        'FI': 0.003,
        'E': 0.10,
        'Recov': 0.03,
        'Res': 0.03,
        'Prem': 0.008, # Assuming Premium is a risk driver
        'Cat': 0.04   # 4% of PML
    }

    # Extract relevant balance sheet items
    fi = balance_sheet['Fixed Income (FI)']
    eq = balance_sheet['Equities (E)']
    recov = balance_sheet['Recoverables (Recov)']
    res = balance_sheet['Reserves (Res)']
    # Assuming Prem and Cat are external inputs for now
    prem = 0 # Placeholder for Premium risk driver
    cat = pml_cat # Catastrophe risk driver (PML)

    # Calculate sub-capitals (simplified for now)
    C_fi = fi * factors['FI']
    C_eq = eq * factors['E']
    C_cred = recov * factors['Recov'] # Simplified credit risk
    C_rsrv = res * factors['Res'] # Simplified reserve risk
    C_prem = prem * factors['Prem']
    C_cat = cat * factors['Cat']
    C_op = 0 # Assuming no operational risk for now
    C_adj = 0 # Assuming no risk adjustment for now

    # BMA BSCR formula (simplified)
    bscr = np.sqrt(C_fi**2 + C_eq**2 + C_cred**2 + C_rsrv**2 + C_prem**2 + C_cat**2) + C_op + C_adj
    return bscr

if __name__ == '__main__':
    company_data = get_company_data()
    balance_sheet = company_data['balance_sheet']

    # Assuming a placeholder PML for Catastrophe risk for pre-shock calculation
    # This will be replaced by actual scenario-driven PML later
    pml_cat_us = 0 # No catastrophe in pre-shock
    pml_cat_bm = 0 # No catastrophe in pre-shock

    # Calculate RC for ARC-US (NAIC RBC)
    rc_us = calculate_naic_rbc(balance_sheet['ARC-US'], pml_cat_us)
    print(f"Required Capital for ARC-US (NAIC RBC): {rc_us:.2f} M$")

    # Calculate RC for ARC-BM (BMA BSCR)
    rc_bm = calculate_bma_bscr(balance_sheet['ARC-BM'], pml_cat_bm)
    print(f"Required Capital for ARC-BM (BMA BSCR): {rc_bm:.2f} M$")

    # Calculate initial solvency ratios
    capital_us = balance_sheet['ARC-US']['Capital (C)']
    capital_bm = balance_sheet['ARC-BM']['Capital (C)']

    sr_us = capital_us / rc_us
    sr_bm = capital_bm / rc_bm

    print(f"Initial Solvency Ratio for ARC-US: {sr_us:.2f}")
    print(f"Initial Solvency Ratio for ARC-BM: {sr_bm:.2f}")
