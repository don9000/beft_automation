import boto3
import os
import time
import os.path
import shutil
from datetime import date
from archiving_and_alerting import archive_files

s3 = boto3.resource('s3')
bucket_name = 'beft-mweb'
directory = '/Users/donovanneethling/Documents/shutil_test/one/'
list_of_files = os.listdir(directory)

print(len(list_of_files))

# archive_files('/Users/donovanneethling/Documents/shutil_test/one/', '/Users/donovanneethling/Documents/shutil_test/archive/')


# print(list_of_files)
#
# for item in list_of_files:
#     if os.path.isfile(item):
#         print(item)


# def upload_files(directory,bucket):
#     list_of_files = os.listdir(directory)
#     for file in list_of_files:
#         s3.Bucket(bucket).upload_file(directory + file, file)



# s3.Bucket(bucket_name).upload_file(source, "newfile")

# upload_files(directory,bucket_name)
# print('done')
