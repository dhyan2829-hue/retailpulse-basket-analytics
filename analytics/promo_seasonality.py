import pandas as pd

def run_phase4_promo_analysis():
    df = pd.read_csv('data/fact_sales.csv')
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df['day_of_week'] = df['transaction_date'].dt.day_name()
    
    # 1. Day of Week Sales & Seasonality Trends
    weekly_trends = df.groupby('day_of_week').agg(
        total_net_sales=('net_sales', 'sum'),
        total_units=('units_sold', 'sum'),
        transaction_count=('transaction_id', 'nunique')
    ).reset_index()
    
    # 2. Promo vs Non-Promo Lift Analysis
    df['is_promotional'] = df['discount_pct'] > 0
    promo_lift = df.groupby('is_promotional').agg(
        avg_units_per_txn=('units_sold', 'mean'),
        avg_net_sales=('net_sales', 'mean'),
        total_margin=('gross_margin', 'sum')
    ).reset_index()
    
    # Save Results
    weekly_trends.to_csv('data/weekly_seasonality.csv', index=False)
    promo_lift.to_csv('data/promo_lift_analysis.csv', index=False)
    print("Phase 4 Analytics Complete: Seasonality and Promo Lift datasets generated.")

if __name__ == '__main__':
    run_phase4_promo_analysis()
