import os

try:
    os.remove('images/1.png')
    print('file deleted')
except:
    print("File doesn't exist")