# RetailPulse — Product Mix & Basket Analytics Engine

## Executive Overview
RetailPulse is a business analytics suite designed for category managers to analyze SKU-level performance, basket behavior, margin leakage, and promotional lift.

## Repository Architecture
* `data/`: Contains raw transaction logs and transformed star schema fact tables.
* `etl/`: Data extraction, transformation, and margin calculations (`data_cleaning.py`).
* `analytics/`: Core analytics engines:
  * `product_performance.py`: SKU/Category ranking & margin leakage detection.
  * `basket_engine.py`: Market Basket Analysis (Support, Confidence, Lift).
  * `promo_seasonality.py`: Promotional lift and weekly seasonality analysis.
* `dashboards/`: Dashboard generation script and automated executive summary outputs.
* `docs/`: Complete KPI dictionary, category insights, and market basket reports.

## Getting Started
Run all pipelines sequentially to process raw sales data through to executive reporting:
```bash
python etl/data_cleaning.py
python analytics/product_performance.py
python analytics/basket_engine.py
python analytics/promo_seasonality.py
python dashboards/build_excel_dashboard.py
