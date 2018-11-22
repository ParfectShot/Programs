import os
# input of directory path
dirname = input()
# function listing all the files in that directory and subdirectories inside it
def listfiles(dirname):
    files = os.listdir(dirname)
    all = list()

    for i in files:
        fpath = os.path.join(dirname,i)

        if os.path.isdir(fpath):
                all+= listfiles(fpath)
        else:
                all.append(fpath)
    return all
# loop iterating though list returned by listfiles function and printong all the names of the files
for x in listfiles(dirname):
    print(x)
