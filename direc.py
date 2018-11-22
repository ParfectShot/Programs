import os
dirname = input()
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
print(listfiles(dirname))