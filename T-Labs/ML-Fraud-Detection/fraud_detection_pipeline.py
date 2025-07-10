# fraud_detection_pipeline.ipynb

# --- IMPORT LIBRARIES ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, precision_recall_curve, auc
from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline
from sklearn.utils.class_weight import compute_class_weight

# Optional (for anomaly detection)
from sklearn.ensemble import IsolationForest

# --- LOAD DATA ---
df = pd.read_csv('bank_transactions.csv')  # Replace with your actual file name

# --- EDA ---
# 1. Univariate Analysis
print(df.describe())
df['IsFraud'].value_counts(normalize=True).plot(kind='bar', title='Class Distribution')
plt.show()

# Histograms of numeric features
numeric_cols = ['Amount', 'OldBalanceOrg', 'NewBalanceOrig', 'OldbalanceDest', 'NewbalanceDest']
df[numeric_cols].hist(figsize=(12, 8))
plt.show()

# 2. Bivariate Analysis
sns.boxplot(x='IsFraud', y='Amount', data=df)
plt.title('Transaction Amounts by Fraud Status')
plt.show()

sns.countplot(x='Type', hue='IsFraud', data=df)
plt.title('Transaction Type vs Fraud')
plt.show()

# Check current fraud flag performance
pd.crosstab(df['IsFlaggedFraud'], df['IsFraud'], normalize='index')

# --- DATA TRANSFORMATION ---
# Drop non-predictive columns
df = df.drop(['NameOrig', 'NameDest'], axis=1)

# Encode categorical feature 'Type'
df['Type'] = LabelEncoder().fit_transform(df['Type'])

# Separate features and target
X = df.drop(['IsFraud'], axis=1)
y = df['IsFraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42)

# Handle imbalance with SMOTE
sm = SMOTE(random_state=42)
X_train_res, y_train_res = sm.fit_resample(X_train, y_train)

# Scale numeric features
scaler = StandardScaler()
X_train_res_scaled = scaler.fit_transform(X_train_res)
X_test_scaled = scaler.transform(X_test)

# --- MODEL TRAINING ---

# Logistic Regression
logreg = LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000)
logreg.fit(X_train_res_scaled, y_train_res)
y_pred_lr = logreg.predict(X_test_scaled)
print("\nLogistic Regression")
print(classification_report(y_test, y_pred_lr))

# Random Forest
rf = RandomForestClassifier(class_weight='balanced', n_estimators=100, random_state=42)
rf.fit(X_train_res, y_train_res)
y_pred_rf = rf.predict(X_test)
print("\nRandom Forest")
print(classification_report(y_test, y_pred_rf))

# XGBoost
xgb = XGBClassifier(scale_pos_weight=(len(y_train_res) - sum(y_train_res)) / sum(y_train_res),
                     use_label_encoder=False, eval_metric='logloss', random_state=42)
xgb.fit(X_train_res, y_train_res)
y_pred_xgb = xgb.predict(X_test)
print("\nXGBoost")
print(classification_report(y_test, y_pred_xgb))

# Optional: Isolation Forest (Anomaly Detection)
iso_forest = IsolationForest(contamination=0.001, random_state=42)
iso_forest.fit(X_train)
y_pred_iso = iso_forest.predict(X_test)
y_pred_iso = np.where(y_pred_iso == -1, 1, 0)  # Convert anomaly flag to fraud label
print("\nIsolation Forest")
print(classification_report(y_test, y_pred_iso))

# --- EVALUATION ---
def plot_roc_pr(y_true, y_scores, label):
    from sklearn.metrics import roc_curve, precision_recall_curve
    fpr, tpr, _ = roc_curve(y_true, y_scores)
    precision, recall, _ = precision_recall_curve(y_true, y_scores)
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(fpr, tpr, label=f'{label} ROC')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.title('ROC Curve')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(recall, precision, label=f'{label} PR')
    plt.title('Precision-Recall Curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.legend()
    plt.show()

# Plot ROC & PR for XGBoost (example)
y_prob_xgb = xgb.predict_proba(X_test)[:, 1]
plot_roc_pr(y_test, y_prob_xgb, 'XGBoost')

# --- FEATURE IMPORTANCE (Random Forest & XGBoost) ---
importances_rf = pd.Series(rf.feature_importances_, index=X.columns)
importances_rf.sort_values().plot(kind='barh', title='Random Forest Feature Importances')
plt.show()

importances_xgb = pd.Series(xgb.feature_importances_, index=X.columns)
importances_xgb.sort_values().plot(kind='barh', title='XGBoost Feature Importances')
plt.show()
