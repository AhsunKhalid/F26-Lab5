# Add comments before you do anything else.
#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Process File data.
# Usage: ./lab5d.py

# TO DO 1: Copy the files pythonStatements.txt and machineCode.txt in folder.
# TO DO 2: Follow the instructions from the readme.me file to create the exact output.

python=open('pythonStatements.txt', 'r')
machine=open('machineCode.txt','r')
output=open('output.txt','w')

pyline=python.readline()
mCline=machine.readline()

while pyline and mCline:
    py=pyline.strip().split('#')[0].strip()  
    #strip gets rid of blank spaces, split stuff in pythonstatements.txt into new lines by #
    mc=mCline.strip()
    output.write(py+'\t'+mc+'\n')
    pyline=python.readline()
    mCline=machine.readline()
python.close ()
machine.close()
output.close()