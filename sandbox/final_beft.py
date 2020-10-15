import boto3
import os
import shutil

s3_resource = boto3.resource('s3')
s3_client=boto3.client('s3')
bucket_name = 'beft-mweb'
afternoon1_file_count = len(s3_client.list_objects(Bucket= 'beft-mweb', Prefix= 'Afternoon1/')['Contents'])
afternoon2_file_count = len(s3_client.list_objects(Bucket= 'beft-mweb', Prefix= 'Afternoon2/')['Contents'])

# afternoon1_file_object and afternoon2_file_object point to the files in the two sub directories
# s3_client.list_objects(Bucket='beft-mweb')['Contents'] returns an array of dictionaries
afternoon1_file_object = s3_client.list_objects(Bucket= bucket_name)['Contents'][1]['Key']
afternoon2_file_object = s3_client.list_objects(Bucket= bucket_name)['Contents'][2]['Key']

def determine_file_location():
    if afternoon1_file_count == 1 and afternoon2_file_count == 2:
        return s3_client.list_objects(Bucket= 'beft-mweb')['Contents'][2]['Key']
    elif afternoon1_file_count == 2 and afternoon2_file_count == 1:
        return s3_client.list_objects(Bucket= 'beft-mweb')['Contents'][1]['Key']
    elif afternoon1_file_count == 2 and afternoon2_file_count == 2:
        return "File in both directories"





# isolates the filename from the string returned by afternoon1_file_object and afternoon2_file_object
afternoon1_file_name = afternoon1_file_object.split('/')[1]
afternoon2_file_name = afternoon2_file_object.split('/')[1]
download_path = '/Users/donovanneethling/Python/beft_automation/beft_files/' + afternoon1_file_name
#determines the amount of files in the directories
# a len() greater than 1 indicates there are files
afternoon1_file_count = len(s3_client.list_objects(Bucket= 'beft-mweb', Prefix= 'Afternoon1/')['Contents'])
afternoon2_file_count = len(s3_client.list_objects(Bucket= 'beft-mweb', Prefix= 'Afternoon2/')['Contents'])

def test_for_files(file_count):
    if file_count > 1:
        return True
    else:
        return False


###DOWNLOADING FILES THAT WORKS#####

def download_files_from_dir(bucket, path, file):
    s3_client.download_file(bucket, path, file)
    with open(file, 'wb') as f:
        s3_client.download_fileobj(bucket, path, f)
# TESTING#

print(determine_file_location())
print(afternoon1_file_object)
print(afternoon2_file_object)
# download_files_from_dir(bucket_name, afternoon2_file_object, download_path)
