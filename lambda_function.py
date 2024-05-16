import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            bucket_name = record['s3']['bucket']['name']
            object_key = record['s3']['object']['key']

            # Check if the file is a PNG
            if object_key.lower().endswith('.png'):
                # Copy the object to bucket2
                copy_source = {'Bucket': bucket_name, 'Key': object_key}
                dest_key = os.path.basename(object_key)
                s3_client.copy_object(CopySource=copy_source, Bucket='mybucket19952', Key=dest_key)

        return {
            'statusCode': 200,
            'body': 'PNG objects copied successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
