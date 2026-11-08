# CYB 371 – Data Mining and Warehousing Practical Project

A beginner-friendly Python project demonstrating five data-mining techniques:
classification, clustering, association rule mining, regression, and anomaly detection.

## 1. Project structure

```text
cyb371_data_mining_project/
├── README.md
├── requirements.txt
├── main.py
├── classification.py
├── clustering.py
├── association_rules.py
├── regression.py
└── anomaly_detection.py
```

## 2. Requirements

- Python 3.10 or newer
- Visual Studio Code
- Python extension for VS Code
- Internet connection for installing Python packages

## 3. Setup in VS Code

Open this folder in VS Code. Open the terminal (`Terminal > New Terminal`) and run:

### Windows

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, use Command Prompt in VS Code and run:

```cmd
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

In VS Code, select the interpreter inside `.venv` if it is not selected automatically.

## 4. Run the project

Run all five demonstrations:

```bash
python main.py
```

Or run one technique at a time:

```bash
python classification.py
python clustering.py
python association_rules.py
python regression.py
python anomaly_detection.py
```

The scripts use small example datasets created inside the code, so no external dataset download is required.

## 5. What each script demonstrates

| File | Technique | Algorithms demonstrated |
|---|---|---|
| `classification.py` | Classification | Decision Tree, Naive Bayes, Random Forest, SVM, KNN, Logistic Regression |
| `clustering.py` | Clustering | K-Means, Agglomerative/Hierarchical, DBSCAN, Mean Shift, Gaussian Mixture |
| `association_rules.py` | Association Rule Mining | Apriori, FP-Growth, Eclat |
| `regression.py` | Regression | Linear, Multiple Linear, Polynomial, Ridge, Lasso, Decision Tree Regression |
| `anomaly_detection.py` | Anomaly Detection | Isolation Forest, LOF, One-Class SVM, DBSCAN, Z-score, Autoencoder |

## 6. Important learning notes

- Classification and regression are supervised learning techniques: training examples include known target values.
- Clustering and anomaly detection are generally unsupervised techniques: they look for structure or unusual observations without target labels.
- Association rule mining discovers co-occurrence patterns in transaction data.
- The examples are educational demonstrations, not production-ready security or financial systems.
- Accuracy and other scores depend on the dataset. A high score on a small synthetic dataset does not prove that a model will work well in the real world.
- DBSCAN can be used for clustering and for identifying points labelled as noise. In the anomaly-detection example, noise points are treated as possible anomalies.

## 7. Suggested GitHub description

**CYB 371 Data Mining and Warehousing – Python Practical Project**

This repository demonstrates five major data-mining techniques using Python and Scikit-learn. It includes simple examples of classification, clustering, association rule mining, regression, and anomaly detection, together with commonly used algorithms and explanations of their practical applications.

## 8. Suggested screenshots for your assignment

After running the scripts, capture:
1. The VS Code terminal showing successful execution.
2. Classification model accuracy results.
3. The clustering output.
4. The association rules generated from the sample transactions.
5. Regression prediction results.
6. Anomaly detection results showing flagged observations.

## 9. Academic integrity and limitations

This is a learning project using generated sample data. Understand each script, change some input values, run it yourself, and describe the results in your own words before submitting or publishing it.
