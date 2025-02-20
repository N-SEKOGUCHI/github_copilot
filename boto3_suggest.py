import boto3
import urllib3

# ... (AWS credentials and S3 details) ...

try:
    # Disable connection pooling by creating a new session with a custom configuration.
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

    # Create a custom urllib3 pool with maxsize=1 (no pooling)
    http_pool = urllib3.PoolManager(maxsize=1)

    # Create an S3 client using the session and the custom pool *Suggesting by Google Gemini. Is it works?
    s3 = session.client('s3', config=boto3.session.Config(s3={'http_client': http_pool}))

    # Example: PUT Object operation
    with open(file_path, 'rb') as f:
        response = s3.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=f
        )

	# If you use boto3.client('s3') instead of boto3.resouce('s3'), application may close http session.
	s3.close()

    print(f"File uploaded successfully to s3://{bucket_name}/{key}")
    print(response)

except Exception as e:
    print(f"Error: {e}")
