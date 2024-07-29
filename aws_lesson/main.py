"""
sign up


iam

create user

aws-cli


"""

import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])
    response = s3.list_objects_v2(Bucket=bucket['Name'])

    for obj in response.get('Contents', []):
        print("\t", obj['Key'])

# s3.create_bucket(Bucket='new-bucket-12341233123')

# s3.download_file("new-bucket-12341233123", "index.html", "index-1.html")


