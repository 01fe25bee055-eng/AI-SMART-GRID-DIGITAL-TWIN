"""Train a baseline Random Forest model from labelled smart-grid examples.

Run from repository root: python ai-model/train_model.py
The bundled sample dataset is illustrative only, not for real protection.
"""
from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "smart_grid_data.csv"
MODEL_PATH = ROOT / "smart_grid_model.joblib"
FEATURES = ["voltage", "current", "temperature"]
TARGET = "status"
REQUIRED = {"Normal", "Overload", "Fault"}

data = pd.read_csv(DATA_PATH)
missing = set(FEATURES + [TARGET]) - set(data.columns)
if missing:
    raise ValueError(f"Missing CSV columns: {sorted(missing)}")
if not REQUIRED.issubset(set(data[TARGET].unique())):
    raise ValueError(f"Dataset must include labels: {sorted(REQUIRED)}")
if data[FEATURES].isna().any().any() or data[TARGET].isna().any():
    raise ValueError("Dataset contains missing values.")

X, y = data[FEATURES], data[TARGET]
counts = y.value_counts()
if counts.min() < 2:
    raise ValueError("Need at least 2 examples per class for stratified splitting.")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = RandomForestClassifier(
    n_estimators=150, random_state=42, class_weight="balanced"
)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Hold-out accuracy (tiny sample data is not meaningful):",
      round(accuracy_score(y_test, pred), 3))
print(classification_report(y_test, pred, zero_division=0))
joblib.dump(model, MODEL_PATH)
print(f"Saved model to: {MODEL_PATH}")
print("Use real, diverse, correctly labelled data and independent testing before drawing conclusions.")
