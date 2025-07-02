import matplotlib.pyplot as plt
import pandas as pd

def plot_optimization_tradeoff():
    results_df = pd.read_csv('results/optimization_results.csv')

    plt.figure(figsize=(12, 7))
    plt.plot(results_df['alpha'], results_df['sr_us'], label='Solvency Ratio ARC-US', marker='o', markersize=4)
    plt.plot(results_df['alpha'], results_df['sr_bm'], label='Solvency Ratio ARC-BM', marker='x', markersize=4)
    
    # Find the optimal alpha from the saved results
    optimal_row = results_df.loc[results_df['cost'].idxmin()]
    optimal_alpha = optimal_row['alpha']
    optimal_sr_us = optimal_row['sr_us']
    optimal_sr_bm = optimal_row['sr_bm']

    plt.axvline(x=optimal_alpha, color='r', linestyle='--', label=f'Optimal Alpha ({optimal_alpha:.2f})')
    plt.scatter(optimal_alpha, optimal_sr_us, color='red', s=100, zorder=5, label='Optimal SR ARC-US')
    plt.scatter(optimal_alpha, optimal_sr_bm, color='red', s=100, zorder=5, label='Optimal SR ARC-BM')

    plt.xlabel('Cession Rate Alpha (ARC-US to ARC-BM)')
    plt.ylabel('Solvency Ratio')
    plt.title('Solvency Ratios vs. Cession Rate (Optimization Trade-off)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('results/optimization_tradeoff.png')
    plt.close()

if __name__ == '__main__':
    plot_optimization_tradeoff()
