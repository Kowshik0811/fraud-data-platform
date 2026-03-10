import random
import uuid
from datetime import datetime

MERCHANTS = ["Amazon", "Walmart", "Target", "Apple", "Uber"]
LOCATIONS = ["CA", "NY", "TX", "FL", "WA"]

def generate_transaction():

    transaction = {
        "transaction_id": str(uuid.uuid4()),
        "user_id": random.randint(1000, 9999),
        "merchant": random.choice(MERCHANTS),
        "amount": round(random.uniform(10, 5000), 2),
        "location": random.choice(LOCATIONS),
        "device_id": random.randint(1, 100),
        "timestamp": datetime.utcnow().isoformat()
    }

    return transaction