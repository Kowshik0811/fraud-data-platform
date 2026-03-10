import joblib
import numpy as np

model = joblib.load("fraud_model.pkl")

def score_transaction(amount):

    score = model.predict(np.array([[amount]]))

    if score[0] == -1:
        return "fraud"

    return "normal"