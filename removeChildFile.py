import os

for i in range(2, 200):
    try:
        os.remove("childFile{}".format(i))
    except:
        break