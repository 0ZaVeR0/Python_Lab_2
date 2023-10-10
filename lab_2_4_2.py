import os
import random

subdirectory = 'example'
try:
    os.mkdir(subdirectory)
except Exception:
    pass

formats = [".test1",".test2",".test3",".test4",".test5",".test6",".test7",".test8",".test9",".test10"]
for i in range(100):
    file = open(os.path.join(subdirectory, "test_name" + str(i) + formats[random.randint(0,9)]),'w')
    file.close()