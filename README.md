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



**CYB 371 Data Mining and Warehousing – Python Practical Project**

This repository demonstrates five major data-mining techniques using Python and Scikit-learn. It includes simple examples of classification, clustering, association rule mining, regression, and anomaly detection, together with commonly used algorithms and explanations of their practical applications.



DUKUYE IMMACULATE OGHENEFEGA
CYBERSECURITY


# CYB 371 – DATA MINING AND DATA WAREHOUSING

## QUESTION 1: DATABASES USED TO STORE STRUCTURED, SEMI-STRUCTURED AND UNSTRUCTURED DATA

Data can be classified into three major categories based on how it is organised and stored. These are structured data, semi-structured data and unstructured data.

### 1. Structured Data

Structured data is data that is organised in a predefined format, usually in rows and columns. It follows a fixed structure, making it easy to store, search, retrieve and analyse.

**Examples:**
- Student records.
- Employee information.
- Bank transaction records.
- Customer details.

**Databases used:** Relational Database Management Systems (RDBMS).

**Examples of databases:**
- MySQL
- PostgreSQL
- Microsoft SQL Server
- Oracle Database

### 2. Semi-Structured Data

Semi-structured data is data that does not follow a strict table format but has some form of organisation through tags, keys, labels or other markers.

It is more flexible than structured data because it does not require a fixed database schema.

**Examples:**
- JSON files.
- XML documents.
- Emails.
- Web data.

**Databases used:** NoSQL databases and document-oriented databases.

**Examples of databases:**
- MongoDB
- CouchDB
- Amazon DynamoDB

### 3. Unstructured Data

Unstructured data is data that does not follow a predefined format or organised table structure. It is usually more difficult to process using traditional relational databases.

**Examples:**
- Images and photographs.
- Videos.
- Audio recordings.
- PDF documents.
- Social media posts.

**Storage systems used:**
- Data Lakes.
- Object Storage Systems.
- Distributed File Systems.

**Examples:**
- Amazon S3.
- Azure Data Lake Storage.
- Hadoop Distributed File System (HDFS).

### Summary

| Data Type | Database/Storage System | Examples |
|---|---|---|
| Structured Data | Relational Databases | MySQL, PostgreSQL |
| Semi-Structured Data | NoSQL Databases | MongoDB, CouchDB |
| Unstructured Data | Data Lakes and Object Storage | Amazon S3, HDFS |

**Note:** Modern data lakes can store structured, semi-structured and unstructured data, while traditional data warehouses mainly store structured and processed data for analysis.

---

## QUESTION 2: ALGORITHMS USED FOR DIFFERENT DATA MINING TECHNIQUES

Data mining is the process of discovering useful patterns, relationships and information from large amounts of data using statistical and computational techniques.

The major data mining techniques and their algorithms are explained below.

### 1. Classification

Classification is a data mining technique used to organise or categorise data into predefined classes based on its characteristics.

**Example:** A bank uses classification to determine whether a loan application should be approved or rejected.

**Algorithms used:**
1. Decision Tree.
2. Naive Bayes.
3. Random Forest.
4. Support Vector Machine (SVM).
5. K-Nearest Neighbours (KNN).
6. Logistic Regression.

### 2. Clustering

Clustering is a data mining technique used to group similar data points together based on their characteristics without using predefined categories.

**Example:** A supermarket groups customers according to their shopping habits and purchasing behaviour.

**Algorithms used:**
1. K-Means Clustering.
2. Hierarchical Clustering.
3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise).
4. Mean Shift.
5. Gaussian Mixture Model (GMM).

### 3. Association Rule Mining

Association Rule Mining is a data mining technique used to discover relationships and patterns between items in large datasets. It identifies items or events that frequently occur together.

**Example:** In a supermarket, customers who buy bread may also frequently buy butter.

**Algorithms used:**
1. Apriori Algorithm.
2. FP-Growth Algorithm (Frequent Pattern Growth).
3. Eclat Algorithm.

### 4. Regression

Regression is a data mining technique used to predict continuous numerical values based on the relationship between different variables.

**Example:** Predicting the price of a house based on its size, location and number of rooms.

**Algorithms used:**
1. Linear Regression.
2. Multiple Linear Regression.
3. Polynomial Regression.
4. Ridge Regression.
5. Lasso Regression.
6. Decision Tree Regression.

### 5. Anomaly Detection

Anomaly Detection is a data mining technique used to identify unusual patterns, activities or data points that differ significantly from normal behaviour.

**Example:** A bank detects an unusual transaction on a customer's account that may indicate fraudulent activity.

**Algorithms used:**
1. Isolation Forest.
2. Local Outlier Factor (LOF).
3. One-Class Support Vector Machine (SVM).
4. DBSCAN.
5. Z-Score Method.
6. Autoencoders.

### SUMMARY OF DATA MINING TECHNIQUES AND THEIR ALGORITHMS

| Data Mining Technique | Algorithms |
|---|---|
| Classification | Decision Tree, Naive Bayes, Random Forest, SVM, KNN |
| Clustering | K-Means, Hierarchical Clustering, DBSCAN, Mean Shift |
| Association Rule Mining | Apriori, FP-Growth, Eclat |
| Regression | Linear Regression, Polynomial Regression, Ridge Regression, Lasso Regression |
| Anomaly Detection | Isolation Forest, LOF, One-Class SVM, DBSCAN, Autoencoders |

### CONCLUSION

Data mining techniques are important for extracting useful information and discovering hidden patterns in large datasets. Each technique uses different algorithms to solve specific problems. Classification predicts categories, clustering groups similar data, association rule mining discovers relationships, regression predicts numerical values, while anomaly detection identifies unusual activities or patterns.
