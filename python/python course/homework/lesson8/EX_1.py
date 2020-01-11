#!/usr/local/bin/python3
import os
pwd = os.getcwd()
content = os.scandir('.')

# Ex 1
size = []
for f in content:
    info = f.stat()
    sizes = info.st_size
    size.append(sizes)
print(sum(size)/1024)

