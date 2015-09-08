from Tkinter import Tk
from tkFileDialog import askopenfilename
import tkFileDialog

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

f = open(filename,"r")

lines = f.readlines()


f.close()


for i, j in enumerate(lines):
    words = lines[i].split()

    if len(words) > 5:
       #lines[i] = words[len(words)-1]
       hour =  int(float(words[len(words)-1][0:2])) - 1
       output = "%02d" % (hour,) + ":" + words[len(words)-1][3:]
       print output
    else:
        del lines[i]

#print lines

'''
f = tkFileDialog.asksaveasfile(mode='w')


for line in lines:
    f.write(line)

f.close()
'''