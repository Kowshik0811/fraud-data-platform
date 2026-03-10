from fastapi import FastAPI
from ml_model.fraud_model import score_transaction

app = FastAPI()

@app.post("/score")

def score(transaction: dict):

    amount = transaction["amount"]

    result = score_transaction(amount)

    return {
        "fraud_prediction": result
    }