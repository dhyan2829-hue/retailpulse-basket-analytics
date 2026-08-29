import pandas as pd
import numpy as np

def run_phase1_etl():
    # Load raw transaction dataset
    df = pd.read_csv('data/raw_transactions.csv')
    
    # Financial Base Calculations
    df['gross_sales'] = df['units_sold'] * df['unit_price']
    df['discount_amount'] = df['gross_sales'] * df['discount_pct']
    df['net_sales'] = df['gross_sales'] - df['discount_amount']
    
    # Estimated Cost of Goods Sold (COGS at 60% of Gross Price)
    df['cogs'] = df['gross_sales'] * 0.60
    df['gross_margin'] = df['net_sales'] - df['cogs']
    df['margin_pct'] = np.where(df['net_sales'] > 0, (df['gross_margin'] / df['net_sales']) * 100, 0)
    
    # Save Transformed Fact Table
    df.to_csv('data/fact_sales.csv', index=False)
    print("Phase 1 ETL Complete: Fact table created successfully.")

if __name__ == '__main__':
    run_phase1_etl()
