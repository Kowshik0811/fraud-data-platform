import boto3
import json

s3 = boto3.client("s3")

BUCKET = "fraud-data-lake"

def upload_transaction(transaction):

    key = f"transactions/{transaction['timestamp']}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(transaction)
    )