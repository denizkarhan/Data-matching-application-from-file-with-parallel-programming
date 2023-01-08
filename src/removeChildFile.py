import os

def removeFile():
    for i in range(1, 200):
        try:
            os.remove("childFile{}".format(i))
        except:
            break

removeFile()