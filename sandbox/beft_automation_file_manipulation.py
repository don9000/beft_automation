import os
import shutil

downloaded_files_one = '/Users/donovanneethling/Python/beft_automation/beft_files/one/'
downloaded_files_two = '/Users/donovanneethling/Python/beft_automation/beft_files/two/'
destination_dir = '/Users/donovanneethling/Python/beft_automation'
src_files_one = os.listdir(downloaded_files_one)
src_files_two = os.listdir(downloaded_files_two)
source_dir = downloaded_files_one

listfiles = os.listdir(destination_dir)
for e in listfiles:
    if os.path.isfile(e):
        shutil.copy(e, '/Users/donovanneethling/Python/beft_automation/beft_files/one/' + e)
    else:
        print("#####################" + e + " is a folder #####################")



# def is_destination_dir_empty():
#     if len(os.listdir(destination_dir))>0:
#         return False
#     else:
#         return True

# print(src_files_one)
#
# if len(src_files_one) > 0:
#     for file_name in src_files_one:
#         shutil.copy(source_dir +'/' + file_name, destination_dir +'/' + file_name)
#         print(file_name + "copied to" + destination_dir +'/' + file_name )
#         print("this is " + os.name)
# else:
#     print("There are no files at this time")



# if len(src_files_one) > 0:
#     shutil.copy(downloaded_files_one + '/' + src_files_one[0], destination_dir + '/' + src_files_one[0])
#
