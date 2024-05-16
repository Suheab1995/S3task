import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        source_key = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')

        # Destination bucket and key for bucket2
        destination_bucket2 = "mybucket19962"
        destination_key2 = f"png_objects/{source_key.split('/')[-1]}"

        # Copy the object to bucket2 if it's a PNG image
        if source_key.lower().endswith('.png'):
            s3.copy_object(
                Bucket=destination_bucket2,
                Key=destination_key2,
                CopySource={'Bucket': source_bucket, 'Key': source_key}
            )
            print(f"PNG object copied from {source_bucket}/{source_key} to {destination_bucket2}/{destination_key2}")

        # Destination bucket and key for bucket1
        destination_bucket1 = source_bucket
        destination_key1 = source_key

        # Copy the object to bucket1 regardless of file type
        s3.copy_object(
            Bucket=destination_bucket1,
            Key=destination_key1,
            CopySource={'Bucket': source_bucket, 'Key': source_key}
        )
        print(f"Object copied to {destination_bucket1}/{destination_key1}")
