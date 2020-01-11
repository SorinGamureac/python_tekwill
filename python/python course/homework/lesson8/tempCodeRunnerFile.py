lastmodified = {}
for f in content:
    info = f.stat()
    lastimeaccessed = info.st_atime
    folder_content = os.listdir(pwd)
    lastmodified.update({f.name : lastimeaccessed})
print(lastmodified)
lastmodified_file = max(lastmodified)
print(lastmodified_file)