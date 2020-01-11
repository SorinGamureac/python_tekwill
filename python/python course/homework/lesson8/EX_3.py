#!/usr/local/bin/python3
import os
pwd = os.getcwd()
content = os.scandir('.')


lastmodified = {}
for f in content:
    info = f.stat()
    lastimemodified = info.st_mtime
    folder_content = os.listdir(pwd)
    lastmodified.update({f.name : lastimemodified})
print(lastmodified)
lastmodified_file = max(lastmodified)
print(lastmodified_file)
