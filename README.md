# CYB 371 – DATA MINING AND DATA WAREHOUSING
DUKUYE IMMACULATE OGHENEFEGA
24/14536
CYBERSECURITY


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
