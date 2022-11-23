import boto3
import os
import time
import os.path
import shutil
from datetime import date
from archiving import archive_files
from send_email import send_email_notification

s3 = boto3.resource('s3')

# Buckets that files will be uploaded to
beft_afternoon_int = 'beft-afternoon-int'


# Directories that files will be uploaded from
int_aud_rep = '/Users/donovanneethling/Documents/shutil_test/one/'

#Archive Directories
int_aud_rep_archive = '/Users/donovanneethling/Documents/shutil_test/archive/'

def upload_files(directory,bucket):
    list_of_files = os.listdir(directory)
    if len(list_of_files) > 0:
        for file in list_of_files:
            s3.Bucket(bucket).upload_file(directory + file, file)
            archive_files(directory,int_aud_rep_archive)
            send_email_notification("Please look in the beft-afternoon-int bucket for the files",directory + 'files uploaded')

upload_files(int_aud_rep, beft_afternoon_int)

#git test
