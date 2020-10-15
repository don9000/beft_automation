import boto3
import os
import shutil

s3_resource = boto3.resource('s3')
s3_client=boto3.client('s3')
beft_mweb = s3_resource.Bucket('beft-mweb')
download_path = '/Users/donovanneethling/Python/beft_automation/beft_files/'

# dict_list is a list of dictionaries for each file in the s3 bucket
dict_list=s3_client.list_objects(Bucket='beft-mweb')['Contents']

#s3_client.download_file('beft-mweb', 'Afternoon1/beftadmin.key', 'beftadmin2.key')
file_name = dict_list[3]['Key'].split('/')[1]


# s3_bucket = s3_resource.Bucket("beft-mweb")
# dir = "Afternoon1"
# files_in_s3 = [f.key.split(dir + "/")[1] for f in
# s3_bucket.objects.filter(Prefix=dir).all()]

def get_file_name(directory):
    files_list = []
    for object_summary in beft_mweb.objects.filter(Prefix= directory):
        if (object_summary.key.split('/')[1]) != '':
            files_list.append(object_summary.key.split('/')[1])
    return files_list
#
# dict_list=s3_client.list_objects(Bucket='beft-mweb')['Contents']
# print(dict_list[5]["Key"])
print()



files = ['Afternoon1/beftadmin.key']
bucket = 'beft-mweb'

s3 = boto3.resource('s3')

for file in files:
    s3.Bucket(bucket).download_file(file, '/Users/donovanneethling/Python/beft_automation/beft_files/one/' + os.path.basename(file) )


# for object_summary in beft_mweb.objects.filter(Prefix="Afternoon1/"):
#     print(object_summary.key)
