import pandas as pd

def run_phase2_analytics():
    # Load transformed sales data
    df = pd.read_csv('data/fact_sales.csv')
    
    # 1. Top & Bottom Performing SKUs by Net Sales
    sku_summary = df.groupby(['sku_id', 'product_name', 'category']).agg(
        total_units=('units_sold', 'sum'),
        total_net_sales=('net_sales', 'sum'),
        total_margin=('gross_margin', 'sum'),
        avg_discount=('discount_pct', 'mean')
    ).reset_index()
    
    # 2. Regional & Channel SKU Performance
    channel_summary = df.groupby(['channel', 'category']).agg(
        net_sales=('net_sales', 'sum')
    ).reset_index()
    
    # 3. Margin Leakage Detection (High discount > 15% eroding margin)
    margin_leakage = df[df['discount_pct'] >= 0.15].groupby(['sku_id', 'product_name']).agg(
        discounted_transactions=('transaction_id', 'count'),
        total_discount_given=('discount_amount', 'sum'),
        remaining_margin=('gross_margin', 'sum')
    ).reset_index()
    
    # Save Outputs
    sku_summary.to_csv('data/sku_performance_summary.csv', index=False)
    margin_leakage.to_csv('data/margin_leakage_report.csv', index=False)
    
    print("Phase 2 Analytics Complete: Performance and Margin Leakage summaries generated.")

if __name__ == '__main__':
    run_phase2_analytics()
