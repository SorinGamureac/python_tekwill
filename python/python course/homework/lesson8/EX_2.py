#!/usr/local/bin/python3
import os
pwd = os.getcwd()
content = os.scandir('.')


lastaccesed = {}
for f in content:
    info = f.stat()
    lastimeaccessed = info.st_atime
    folder_content = os.listdir(pwd)
    lastaccesed.update({f.name : lastimeaccessed})
lastaccesed_file = max(lastaccesed)
print(lastaccesed_file)


