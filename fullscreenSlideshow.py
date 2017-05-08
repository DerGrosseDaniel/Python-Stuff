#!/usr/bin/python

import os, random, subprocess, time

file_list = []
s = 3
path = "/imagepath/"
for f in os.listdir(path):
	file_list.append(f)

random.shuffle(file_list)

i = 1
n = len(file_list)
for f in file_list:
    print(str(i)+"/"+str(n))
    i+=1
    p = subprocess.call("timeout "+str(s+2)+"s viewnior --fullscreen \""+path+str(f)+"\" &", shell=True, executable="/bin/bash")
    time.sleep(s)
