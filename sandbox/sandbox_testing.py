import boto3
import os
import shutil

s3_resource = boto3.resource('s3')
s3_client=boto3.client('s3')
beft_mweb = s3_resource.Bucket('beft-mweb')
#
# afternoon1_file_object = s3_client.list_objects(Bucket='beft-mweb')['Contents'][1]['Key']
# afternoon2_file_object = s3_client.list_objects(Bucket='beft-mweb')['Contents'][3]['Key']
# afternoon1_file_name = afternoon1_file_object.split('/')[1]
# afternoon2_file_name = afternoon1_file_object.split('/')[1]
# print(afternoon_file_name)

afternoon1_file_count = len(s3_client.list_objects(Bucket= 'beft-mweb', Prefix= 'Afternoon1/')['Contents'])
afternoon2_file_count = len(s3_client.list_objects(Bucket= 'beft-mweb', Prefix= 'Afternoon2/')['Contents'])

# print(len(response['Contents']))


def test_for_files(file_count):
    if file_count > 1:
        return True
    else:
        return False

print(test_for_files(afternoon1_file_count))

# object_array = s3_client.list_objects(Bucket='beft-mweb')['Contents']
# print(object_array)
#
# for e in object_array:
#     print(e)
#     print("====================================")




# for ele in object_array:
#     if ele['Key'] == 'Afternoon1/':
#         print(ele['Key'])
# print(s3_client.list_objects(Bucket='beft-mweb')['Contents'][0])
# print(s3_client.list_objects(Bucket='beft-mweb')['Contents'][1])
# print(s3_client.list_objects(Bucket='beft-mweb')['Contents'][2])
# print(s3_client.list_objects(Bucket='beft-mweb')['Contents'][3])


# with open('FILE_NAME', 'wb') as f:
#     s3_client.download_fileobj(beft_mweb, 'Afternoon1/beftadmin.key', 'newfile.txt')


###DOWNLOADING FILES THAT WORKS#####
# s3 = boto3.client('s3')
# s3.download_file('beft-mweb', afternoon2_file_object, afternoon2_file_name)
#
#
#
# with open(afternoon2_file_name, 'wb') as f:
#     s3.download_fileobj('beft-mweb', afternoon2_file_object, f)
