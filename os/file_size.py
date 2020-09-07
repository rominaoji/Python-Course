#!/usr/bin/python

import os

try:
    filesize = os.path.getsize('myfile.txt')
    print('file size: {} bytes'.format(filesize))
except IOError as e:
    print(e)
