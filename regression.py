"""Regression algorithms using a generated house-price dataset."""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score


def run():
    print("\n[4] REGRESSION")
    print("Example: predict house price using size, bedrooms, and distance to town.")

    rng = np.random.default_rng(7)
    size = rng.uniform(50, 250, 160)           # square metres
    bedrooms = rng.integers(1, 6, 160)
    distance = rng.uniform(1, 30, 160)         # kilometres
    X = np.column_stack([size, bedrooms, distance])

    # Illustrative price formula plus random noise; price is in thousands of currency units.
    y = 35 + 1.8 * size + 12 * bedrooms - 1.4 * distance + rng.normal(0, 18, 160)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=7
    )

    models = {
        "Linear Regression": LinearRegression(),
        "Multiple Linear Regression": LinearRegression(),
        "Polynomial Regression (degree 2)": make_pipeline(
            PolynomialFeatures(degree=2, include_bias=False), LinearRegression()
        ),
        "Ridge Regression": make_pipeline(StandardScaler(), Ridge(alpha=1.0)),
        "Lasso Regression": make_pipeline(StandardScaler(), Lasso(alpha=0.1, max_iter=10000)),
        "Decision Tree Regression": DecisionTreeRegressor(max_depth=4, random_state=7),
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print(
            f"{name:34s} MAE = {mean_absolute_error(y_test, predictions):.2f}, "
            f"R² = {r2_score(y_test, predictions):.3f}"
        )

    sample = np.array([[150, 3, 8]])
    final_model = LinearRegression().fit(X_train, y_train)
    print(f"\nExample predicted price for 150 sqm, 3 bedrooms, 8 km from town: "
          f"{final_model.predict(sample)[0]:.2f} thousand units")


if __name__ == "__main__":
    run()
