#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
tmp script for capture the scene of my home.
'''

import os
import time
import subprocess

__HOME__ = '/media/Xiahaifeng/Screen/screen'
__LOG__ = '/media/Xiahaifeng/Screen/index.html'

if __name__ == '__main__':
    # dir name
    dirName = os.path.join(__HOME__, time.strftime("%Y-%m-%d", time.localtime()), str(time.localtime().tm_hour))
    count = 0
    while not os.path.exists(dirName) and count < 5:
        os.makedirs(dirName)
        count += 1
    filePath = "{0}.jpg".format(os.path.join(dirName, time.strftime("%Y-%m-%d %H:%m:%S", time.localtime())))
    args = ["raspistill", "-n", "-t", "1", "-h", "1024", "-w", "1024", "-o", filePath]
    pipe = subprocess.Popen(args, stderr=subprocess.PIPE)
    lines = pipe.stderr.readlines()
    if len(lines) > 0:
        logger = open(__LOG__, 'a')
        for l in lines:
            logger.write(l)
        logger.close()
    exit(0)

