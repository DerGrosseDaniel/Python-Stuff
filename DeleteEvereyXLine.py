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
    if i % 2 == 0:
       del lines[i]



f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")

#f = open("output.txt","w")

for line in lines:
    f.write(line)

f.close()