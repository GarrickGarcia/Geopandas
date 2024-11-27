import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# List the objects in the Foursquare S3 bucket
bucket_name = 'fsq-os-places-us-east-1'
prefix = 'release/dt=2024-11-19/places/parquet/'

response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

# Print the list of objects
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print("No objects found.")
