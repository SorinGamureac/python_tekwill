import os
#Create new folder with name my_data_folder

pwd = os.getcwd()
path = pwd + "/my_data_folder"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)