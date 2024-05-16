import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    # Check if the object has a PNG extension
    if source_key.lower().endswith('.png'):
        # Destination bucket and key
        destination_bucket = "mybucket19962"
        destination_key = f"png_objects/{source_key.split('/')[-1]}"

        # Copy the object
        s3.copy_object(
            Bucket=destination_bucket,
            Key=destination_key,
            CopySource={'Bucket': source_bucket, 'Key': source_key}
        )
        print(f"Object copied from {source_bucket}/{source_key} to {destination_bucket}/{destination_key}")
        return "PNG object copied successfully"
    else:
        print(f"Ignoring non-PNG object: {source_bucket}/{source_key}")
        return "Non-PNG object ignored"
