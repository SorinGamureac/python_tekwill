#!/usr/local/bin/python3
import os
# cdr = os.getcwd()

# print(cdr)
pwd = os.getcwd()

#folder_content = os.listdir(f"{pwd}/myfolder")
# print(folder_content)
content = os.scandir('.')
# print(content)

# my_folder_path = os.path.join(pwd, 'myfolder')
# print(my_folder_path)

#folder = os.listdir(pwd)

# Ex 1
# size = []
# for f in content:
#     info = f.stat()
#     sizes = info.st_size
#     size.append(sizes)
# print(sum(size))

# print(info.st_atime) # Last time accessed
# print(info.st_mtime) # last modified

# lastmodified = {}
# for f in content:
#     info = f.stat()
#     lastimeaccessed = info.st_atime
#     folder_content = os.listdir(pwd)
#     lastmodified.update({f.name : lastimeaccessed})
# print(lastmodified)
# lastmodified_file = max(lastmodified)
# print(lastmodified_file)
