import matplotlib.pyplot as plt
import numpy as np
from scripts.company_data import get_company_data
from scripts.calculate_rc import calculate_naic_rbc, calculate_bma_bscr, propagate_shock

def plot_solvency_impact():
    company_data = get_company_data()
    balance_sheet_pre_shock = company_data['balance_sheet']
    initial_loss_allocation = company_data['initial_loss_allocation']

    # Pre-shock data
    capital_us_pre_shock = balance_sheet_pre_shock.loc['Capital (C)', 'ARC-US']
    capital_bm_pre_shock = balance_sheet_pre_shock.loc['Capital (C)', 'ARC-BM']
    rc_us_pre_shock = calculate_naic_rbc(balance_sheet_pre_shock['ARC-US'], pml_cat=0)
    rc_bm_pre_shock = calculate_bma_bscr(balance_sheet_pre_shock['ARC-BM'], pml_cat=0)

    sr_us_pre_shock = capital_us_pre_shock / rc_us_pre_shock
    sr_bm_pre_shock = capital_bm_pre_shock / rc_bm_pre_shock
    sr_group_pre_shock = (capital_us_pre_shock + capital_bm_pre_shock) / (rc_us_pre_shock + rc_bm_pre_shock)

    # Post-shock data
    shock_results = propagate_shock(balance_sheet_pre_shock, initial_loss_allocation)
    capital_us_post_shock = shock_results['updated_balance_sheet'].loc['Capital (C)', 'ARC-US']
    capital_bm_post_shock = shock_results['updated_balance_sheet'].loc['Capital (C)', 'ARC-BM']
    rc_us_post_shock = shock_results['rc_u_us']
    rc_bm_post_shock = shock_results['rc_u_bm']

    sr_us_post_shock = capital_us_post_shock / rc_us_post_shock
    sr_bm_post_shock = capital_bm_post_shock / rc_bm_post_shock
    sr_group_post_shock = (capital_us_post_shock + capital_bm_post_shock) / (rc_us_post_shock + rc_bm_post_shock)

    # Data for plotting
    labels = ['ARC-US', 'ARC-BM', 'Group']
    pre_shock_srs = [sr_us_pre_shock, sr_bm_pre_shock, sr_group_pre_shock]
    post_shock_srs = [sr_us_post_shock, sr_bm_post_shock, sr_group_post_shock]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, pre_shock_srs, width, label='Pre-Shock', color='skyblue')
    rects2 = ax.bar(x + width/2, post_shock_srs, width, label='Post-Shock', color='lightcoral')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Solvency Ratio')
    ax.set_title('Solvency Ratios Before and After Florida Hurricane Shock')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3, fmt='%.2f')
    ax.bar_label(rects2, padding=3, fmt='%.2f')

    fig.tight_layout()
    plt.savefig('results/solvency_impact.png')
    plt.close()

if __name__ == '__main__':
    plot_solvency_impact()
