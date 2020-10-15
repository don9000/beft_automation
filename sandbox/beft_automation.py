import boto3
import os
import shutil

s3_resource = boto3.resource('s3')
s3_client=boto3.client('s3')
download_path = '/Users/donovanneethling/Python/beft_automation/beft_files/'

# dict_list is a list of dictionaries for each file in the s3 bucket
dict_list=s3_client.list_objects(Bucket='beft-mweb')['Contents']

def s3_file_name(directory):
    files_list = []
    for object_summary in beft_mweb.objects.filter(Prefix= directory):
        if (object_summary.key.split('/')[1]) != '':
            files_list.append(object_summary.key.split('/')[1])
    return files_list

# download_files() uses the download_file method from boto3.resource to download the specified file(s)
# s3_resource.Bucket('bucket_name').download_file(source_file, destination/path/file_name])
# in this case source_file is the file name associated with the key in the dictionary passed into the loop from dict_list
def download_files():
    for dict in dict_list:
        s3_resource.Bucket('beft-mweb').download_file(dict['Key'], download_path + dict['Key'])

# confirm_download() compares the files in the s3 bucket with the files downloaded and returns a boolean value
# True if files match, which indicates a successful download.
# s3_file_list.append(dictionary['Key']) appends the value associated with Key (the name of the file) to s3_file_list
def confirm_download():
    s3_file_list = []
    downloaded_files = os.listdir(download_path)
    for dictionary in dict_list:
        s3_file_list.append(dictionary['Key'])
    return set(s3_file_list)==set(downloaded_files)

# delete_s3_files() uses confirm_download() before deleting the files from the s3 bucket
def delete_s3_files(s3_files):
    if confirm_download():
        for file in s3_files:
            s3_client.delete_object(
            Bucket='beft-mweb',
            Key=file['Key'])


# download_files()
# delete_s3_files(dict_list)
print(type(dict_list))
for each in dict_list:
    print(each)
