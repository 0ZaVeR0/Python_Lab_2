import os

subdirectory = 'example'
files = os.listdir('example')
format = input()

files = [x for x in files if format in x]

print(len(files))