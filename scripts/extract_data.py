import boto3

def extract_data_from_s3(bucket_name, file_key):
    """Extract data from an S3 bucket."""
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    data = obj['Body'].read()
    return data

if __name__ == "__main__":
    data = extract_data_from_s3('your-bucket-name', 'data/sample_data.csv')
    print("Data extracted:", data)
