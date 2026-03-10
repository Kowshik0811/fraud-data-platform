from kafka import KafkaProducer
import json
import time

from transaction_generator import generate_transaction

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TOPIC = "bank_transactions"

while True:

    transaction = generate_transaction()

    producer.send(TOPIC, transaction)

    print("Transaction sent:", transaction)

    time.sleep(1)