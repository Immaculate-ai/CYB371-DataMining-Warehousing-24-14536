"""Run all CYB 371 data-mining demonstrations."""

import classification
import clustering
import association_rules
import regression
import anomaly_detection


def main():
    print("\n" + "=" * 70)
    print("CYB 371 - DATA MINING AND DATA WAREHOUSING PRACTICAL")
    print("=" * 70)

    classification.run()
    clustering.run()
    association_rules.run()
    regression.run()
    anomaly_detection.run()

    print("\nAll demonstrations completed.")


if __name__ == "__main__":
    main()
