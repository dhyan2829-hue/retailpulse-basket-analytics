import pandas as pd
from itertools import combinations
from collections import Counter

def run_phase3_basket_analysis():
    df = pd.read_csv('data/fact_sales.csv')
    
    # Group items by transaction
    baskets = df.groupby('transaction_id')['product_name'].apply(list).to_dict()
    total_transactions = len(baskets)
    
    # Count item pairs
    pair_counts = Counter()
    item_counts = Counter()
    
    for items in baskets.values():
        unique_items = sorted(list(set(items)))
        for item in unique_items:
            item_counts[item] += 1
        for pair in combinations(unique_items, 2):
            pair_counts[pair] += 1

    # Calculate Support, Confidence, and Lift
    rules = []
    for (item_a, item_b), count in pair_counts.items():
        support = count / total_transactions
        confidence_a_to_b = count / item_counts[item_a]
        confidence_b_to_a = count / item_counts[item_b]
        
        # Lift calculation
        expected_support = (item_counts[item_a] / total_transactions) * (item_counts[item_b] / total_transactions)
        lift = support / expected_support if expected_support > 0 else 0
        
        rules.append({
            'Antecedent': item_a,
            'Consequent': item_b,
            'Support': round(support, 3),
            'Confidence': round(confidence_a_to_b, 3),
            'Lift': round(lift, 3)
        })
    
    rules_df = pd.DataFrame(rules)
    rules_df.to_csv('data/market_basket_rules.csv', index=False)
    print("Phase 3 Complete: Market Basket Rules generated.")

if __name__ == '__main__':
    run_phase3_basket_analysis()
