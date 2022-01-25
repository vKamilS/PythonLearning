import os
import time

dir = input('Provide folder path:')

if not os.path.isdir(dir):
    print('Provided path is not a folder')
else:
    fileName = input('Provide file name:')
    path=os.path.join(dir, fileName)
    if not os.path.exists(path):
        print('File does not exists.')
    else:
        print('File data:')
        print('File size is:', os.path.getsize(path))
        print('Last modify date is:', time.localtime(os.path.getmtime(path)))
        print('Current folder is:', os.getcwd())
        print('The directory path is:', os.path.dirname(path))





