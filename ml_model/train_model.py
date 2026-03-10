import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

data = pd.read_csv("transactions.csv")

features = data[["amount"]]

model = IsolationForest(contamination=0.02)

model.fit(features)

joblib.dump(model, "fraud_model.pkl")