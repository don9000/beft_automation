import os
import os.path
import time

path = '/Users/donovanneethling/Python/beft_automation/beft_files/file1.txt'

while os.path.isfile(path):
    time.sleep(60)
