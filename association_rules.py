"""Association rule mining: Apriori, FP-Growth, and Eclat."""

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules


TRANSACTIONS = [
    ["bread", "milk", "butter"],
    ["bread", "milk"],
    ["bread", "butter"],
    ["milk", "butter"],
    ["bread", "milk", "butter", "eggs"],
    ["bread", "eggs"],
    ["milk", "eggs"],
    ["bread", "milk", "eggs"],
]


def eclat(transactions, min_support=0.25):
    """Small educational Eclat implementation using transaction-ID sets."""
    items = sorted({item for basket in transactions for item in basket})
    vertical = {
        item: {i for i, basket in enumerate(transactions) if item in basket}
        for item in items
    }
    frequent = []

    def extend(prefix, candidates):
        for index, (item, tids) in enumerate(candidates):
            new_itemset = prefix + (item,)
            support = len(tids) / len(transactions)
            if support >= min_support:
                frequent.append((new_itemset, support))
                suffix = []
                for next_item, next_tids in candidates[index + 1:]:
                    intersection = tids & next_tids
                    if len(intersection) / len(transactions) >= min_support:
                        suffix.append((next_item, intersection))
                extend(new_itemset, suffix)

    initial = [(item, tids) for item, tids in vertical.items()]
    extend(tuple(), initial)
    return frequent


def run():
    print("\n[3] ASSOCIATION RULE MINING")
    print("Example: discover products that appear together in shopping baskets.")

    encoder = TransactionEncoder()
    encoded = encoder.fit(TRANSACTIONS).transform(TRANSACTIONS)
    basket_df = pd.DataFrame(encoded, columns=encoder.columns_)

    for algorithm_name, algorithm in [("Apriori", apriori), ("FP-Growth", fpgrowth)]:
        itemsets = algorithm(basket_df, min_support=0.25, use_colnames=True)
        print(f"\n{algorithm_name} frequent itemsets:")
        print(itemsets.to_string(index=False))

        if not itemsets.empty:
            rules = association_rules(itemsets, metric="confidence", min_threshold=0.5)
            if not rules.empty:
                print(f"{algorithm_name} rules (first five):")
                print(rules[["antecedents", "consequents", "support", "confidence", "lift"]]
                      .head().to_string(index=False))
            else:
                print("No rules met the selected confidence threshold.")

    print("\nEclat frequent itemsets:")
    for items, support in eclat(TRANSACTIONS, min_support=0.25):
        print(f"{items}: support = {support:.2f}")


if __name__ == "__main__":
    run()
