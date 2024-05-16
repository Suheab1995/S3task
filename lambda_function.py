import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Check if event is an S3 event
        if event['Records'][0]['eventSource'] != 'aws:s3':
            return {'statusCode': 400, 'body': 'Not an S3 event'}

        # Get the bucket and key from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']

        # Check if the file is a PNG
        if not object_key.lower().endswith('.png'):
            return {'statusCode': 200, 'body': 'Not a PNG file'}

        # Copy the object to bucket2
        copy_source = {'Bucket': bucket_name, 'Key': object_key}
        dest_key = os.path.basename(object_key)
        s3_client.copy_object(CopySource=copy_source, Bucket='bucket199552', Key=dest_key)

        return {'statusCode': 200, 'body': f'Copied {object_key} to bucket2'}

    except Exception as e:
        return {'statusCode': 500, 'body': str(e)}
