import boto3

def del_s3():
    s3_resource = boto3.resource('s3')
    print("Buckets:")
    for bucket in s3_resource.buckets.all():
        print(f"\t{bucket.name}")
        
    name_bucket = s3_resource.Bucket(bucket.name)
    for name_bucket in name_bucket.objects.all():
        print(name_bucket)
        name_bucket.delete()

    name_bucket = s3_resource.Bucket(bucket.name)
    name_bucket.delete()
    
if __name__ == '__main__':
    del_s3()
