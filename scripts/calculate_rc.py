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

def propagate_shock(initial_balance_sheet, initial_loss_allocation, alpha):
    # Retrocession matrix R based on alpha
    # ARC-US (index 0) cedes alpha to ARC-BM (index 1)
    R = np.array([
        [1 - alpha, alpha],  # ARC-US retains (1-alpha), cedes alpha to ARC-BM
        [0.0, 1.0]           # ARC-BM retains 100% of its own loss and assumed loss
    ])

    L0 = initial_loss_allocation.values

    # Calculate net losses for each entity after retrocession (L^U)
    net_loss_us = L0[0] * R[0,0]
    net_loss_bm = L0[1] * R[1,1] + L0[0] * R[0,1]

    L_U = pd.Series([net_loss_us, net_loss_bm], index=initial_loss_allocation.index)

    # Calculate ceded and assumed amounts for balance sheet updates
    ceded_loss_us_to_bm = L0[0] * R[0,1]
    retained_loss_us = L0[0] * R[0,0]

    # Create copies of balance sheets to modify
    updated_balance_sheet = initial_balance_sheet.copy()

    # Update Capital (C^U)
    updated_balance_sheet.loc['Capital (C)', 'ARC-US'] -= L_U['ARC-US']
    updated_balance_sheet.loc['Capital (C)', 'ARC-BM'] -= L_U['ARC-BM']

    # Update Reserves and Recoverables
    updated_balance_sheet.loc['Reserves (Res)', 'ARC-US'] += retained_loss_us
    updated_balance_sheet.loc['Recoverables (Recov)', 'ARC-US'] += ceded_loss_us_to_bm
    updated_balance_sheet.loc['Reserves (Res)', 'ARC-BM'] += (L0[1] + ceded_loss_us_to_bm)

    # Recalculate RC^U using updated balance sheets and net catastrophe losses
    rc_u_us = calculate_naic_rbc(updated_balance_sheet['ARC-US'], L_U['ARC-US'])
    rc_u_bm = calculate_bma_bscr(updated_balance_sheet['ARC-BM'], L_U['ARC-BM'])

    return {
        'updated_balance_sheet': updated_balance_sheet,
        'net_losses': L_U,
        'rc_u_us': rc_u_us,
        'rc_u_bm': rc_u_bm
    }

def calculate_cost(alpha):
    company_data = get_company_data()
    balance_sheet_pre_shock = company_data['balance_sheet']
    initial_loss_allocation = company_data['initial_loss_allocation']

    shock_results = propagate_shock(balance_sheet_pre_shock, initial_loss_allocation, alpha)

    capital_us_post_shock = shock_results['updated_balance_sheet'].loc['Capital (C)', 'ARC-US']
    capital_bm_post_shock = shock_results['updated_balance_sheet'].loc['Capital (C)', 'ARC-BM']

    sr_us_post_shock = capital_us_post_shock / shock_results['rc_u_us']
    sr_bm_post_shock = capital_bm_post_shock / shock_results['rc_u_bm']

    # Cost function to minimize
    # Add a small epsilon to avoid division by zero if SR becomes 1 or less
    epsilon = 1e-6
    cost = 1 / (sr_us_post_shock - 1 + epsilon) + 1 / (sr_bm_post_shock - 1 + epsilon)
    
    return cost, sr_us_post_shock, sr_bm_post_shock

if __name__ == '__main__':
    company_data = get_company_data()
    balance_sheet_pre_shock = company_data['balance_sheet']
    initial_loss_allocation = company_data['initial_loss_allocation']

    print("--- Pre-Shock Data ---")
    print("Balance Sheet (in M$):")
    print(balance_sheet_pre_shock)
    print("\nInitial Loss Allocation (L^0, in M$):")
    print(initial_loss_allocation)

    # Calculate RC for ARC-US (NAIC RBC) and ARC-BM (BMA BSCR) pre-shock
    # Assuming 0 PML for pre-shock RC calculation
    pml_cat_us = 0 # No catastrophe in pre-shock
    pml_cat_bm = 0 # No catastrophe in pre-shock

    rc_us_pre_shock = calculate_naic_rbc(balance_sheet_pre_shock['ARC-US'], pml_cat_us)
    rc_bm_pre_shock = calculate_bma_bscr(balance_sheet_pre_shock['ARC-BM'], pml_cat_bm)

    print(f"\nRequired Capital for ARC-US (NAIC RBC) Pre-Shock: {rc_us_pre_shock:.2f} M$")
    print(f"Required Capital for ARC-BM (BMA BSCR) Pre-Shock: {rc_bm_pre_shock:.2f} M$")

    # Calculate initial solvency ratios
    capital_us_pre_shock = balance_sheet_pre_shock.loc['Capital (C)', 'ARC-US']
    capital_bm_pre_shock = balance_sheet_pre_shock.loc['Capital (C)', 'ARC-BM']

    sr_us_pre_shock = capital_us_pre_shock / rc_us_pre_shock
    sr_bm_pre_shock = capital_bm_pre_shock / rc_bm_pre_shock

    print(f"Initial Solvency Ratio for ARC-US: {sr_us_pre_shock:.2f}")
    print(f"Initial Solvency Ratio for ARC-BM: {sr_bm_pre_shock:.2f}")

    print("\n--- Post-Shock Data (with fixed retrocession, alpha=0.5) ---")
    # Test with alpha = 0.5
    alpha_fixed = 0.5
    shock_results_fixed = propagate_shock(balance_sheet_pre_shock, initial_loss_allocation, alpha_fixed)

    print("\nUpdated Balance Sheet (in M$):")
    print(shock_results_fixed['updated_balance_sheet'])

    print("\nNet Losses (L^U, in M$):")
    print(shock_results_fixed['net_losses'])

    print(f"\nRequired Capital for ARC-US (NAIC RBC) Post-Shock: {shock_results_fixed['rc_u_us']:.2f} M$")
    print(f"Required Capital for ARC-BM (BMA BSCR) Post-Shock: {shock_results_fixed['rc_u_bm']:.2f} M$")

    # Calculate post-shock solvency ratios
    capital_us_post_shock_fixed = shock_results_fixed['updated_balance_sheet'].loc['Capital (C)', 'ARC-US']
    capital_bm_post_shock_fixed = shock_results_fixed['updated_balance_sheet'].loc['Capital (C)', 'ARC-BM']

    sr_us_post_shock_fixed = capital_us_post_shock_fixed / shock_results_fixed['rc_u_us']
    sr_bm_post_shock_fixed = capital_bm_post_shock_fixed / shock_results_fixed['rc_u_bm']

    print(f"Post-Shock Solvency Ratio for ARC-US: {sr_us_post_shock_fixed:.2f}")
    print(f"Post-Shock Solvency Ratio for ARC-BM: {sr_bm_post_shock_fixed:.2f}")

    cost_fixed, sr_us_fixed, sr_bm_fixed = calculate_cost(alpha_fixed)
    print(f"Cost for alpha={alpha_fixed}: {cost_fixed:.2f}")

    print("\n--- Optimization Loop ---")
    alphas = np.arange(0, 1.01, 0.01)
    costs = []
    sr_us_values = []
    sr_bm_values = []

    min_cost = float('inf')
    optimal_alpha = -1

    for alpha in alphas:
        cost, sr_us, sr_bm = calculate_cost(alpha)
        costs.append(cost)
        sr_us_values.append(sr_us)
        sr_bm_values.append(sr_bm)

        if cost < min_cost:
            min_cost = cost
            optimal_alpha = alpha

    print(f"Optimal alpha: {optimal_alpha:.2f}")
    print(f"Minimum cost: {min_cost:.2f}")

    # Save results for plotting
    results_df = pd.DataFrame({
        'alpha': alphas,
        'cost': costs,
        'sr_us': sr_us_values,
        'sr_bm': sr_bm_values
    })
    results_df.to_csv('results/optimization_results.csv', index=False)
    print("Optimization results saved to results/optimization_results.csv")