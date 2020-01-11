import os

pwd = os.getcwd()

path = pwd + "\my_data_folder"

try:
    os.chdir(".\my_data_folder")
except OSError:
    print ("Changed of the directory %s failed" % path)
else:
    print ("Successfully changed the directory %s " % path)