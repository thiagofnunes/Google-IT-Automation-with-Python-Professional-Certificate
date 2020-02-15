#!/usr/bin/env python3

import sys
import os
from pathlib import Path
with open (sys.argv[1], "r") as myfile:
   for line in myfile:
    data= line.replace("\n", "")
    base=os.path.basename(data)
    baseNew = base.replace("jane","jdoe")
    #Dont forget to change to your own directory
    os.chdir('/home/student-02-06265fe82641/data')
    os.rename(base, baseNew)
myfile.close()
