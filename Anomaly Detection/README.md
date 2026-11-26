# Anomaly Detection

An unsupervised machine-learning project for identifying unusual credit-card transactions and prioritising potential fraud for review.

## Project

The complete analysis is available in [Anomaly Detection in Transactions](./Anomaly%20Detection%20in%20Transactions/README.md). It uses the public ULB Credit Card Fraud Detection dataset and evaluates anomaly scores without using the fraud label during model fitting.

The workflow covers:

- Exploratory analysis of fraud prevalence, transaction amounts, and anonymised PCA features
- Data-quality checks and feature standardisation
- Isolation Forest, One-Class SVM, and Local Outlier Factor detectors
- PR-AUC, ROC-AUC, precision@k, recall, and F1 evaluation
- Top-k alert-queue analysis for analyst triage

## Verified Dataset Scope

- **20,492 transactions** in the project subsample
- **492 fraud cases** retained from the source data
- **2.40% fraud prevalence**
- `Class` is held out for evaluation and is not used to train the unsupervised detectors

## Highlighted Result

The detailed project README reports Isolation Forest as the strongest detector, with **0.9447 ROC-AUC**, **0.6438 PR-AUC**, and **0.5894 precision@k** when reviewing the top 492 anomaly scores. The analysis also reports **1.000 precision in the top 50 alerts** for the evaluated run.

## Folder Structure

```text
Anomaly Detection/
└── Anomaly Detection in Transactions/
    ├── 01_eda.ipynb
    ├── 02_data_cleaning.ipynb
    ├── 03_model_building.ipynb
    ├── utils.py
    ├── requirements.txt
    ├── data/
    └── README.md
```

## Getting Started

Open the detailed project README for dataset instructions, dependencies, notebook order, model results, and limitations:

[Open the full project documentation](./Anomaly%20Detection%20in%20Transactions/README.md)

## Author

**Vishal Yadav**

Part of the [EDA Project Portfolio](https://github.com/Vishal123-tech/EDA-PROJECT-/).
