import pandas as pd

def generate_dashboard_workbook():
    fact_df = pd.read_csv('data/fact_sales.csv')
    
    # Create Excel Writer for Multi-Tab Product Intelligence Dashboard
    with pd.ExcelWriter('dashboards/RetailPulse_Executive_Dashboard.xlsx', engine='openpyxl') as writer:
        # Sheet 1: Executive KPI Summary
        kpi_summary = pd.DataFrame({
            'Metric': ['Total Gross Sales', 'Total Net Sales', 'Total Gross Margin', 'Average Margin %', 'Unique Transactions'],
            'Value': [
                fact_df['gross_sales'].sum(),
                fact_df['net_sales'].sum(),
                fact_df['gross_margin'].sum(),
                (fact_df['gross_margin'].sum() / fact_df['net_sales'].sum()) * 100,
                fact_df['transaction_id'].nunique()
            ]
        })
        kpi_summary.to_excel(writer, sheet_name='Executive Summary', index=False)
        
        # Sheet 2: Category Performance
        cat_summary = fact_df.groupby('category').agg(
            Net_Sales=('net_sales', 'sum'),
            Gross_Margin=('gross_margin', 'sum'),
            Units_Sold=('units_sold', 'sum')
        ).reset_index()
        cat_summary.to_excel(writer, sheet_name='Category Performance', index=False)
        
    print("Executive Dashboard Workbook generated successfully at dashboards/RetailPulse_Executive_Dashboard.xlsx")

if __name__ == '__main__':
    generate_dashboard_workbook()
