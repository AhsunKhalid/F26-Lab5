# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 22/10/2026
# Purpose: Process File data.
# Usage: ./lab5c.py

# TO DO 1: Run the code provided in readme.md file.
# TO DO 2: Open rhyme.txt file.
# TO DO 3: Print the output as directed in readme.md file.

with open("rhyme.txt", "w") as dataFile :
  dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")

f=open('rhyme.txt', 'r')
line=f.readline()
while line!="":
    clean_line=line.strip().strip('.')
    words_list=clean_line.split()
    count=len(words_list)
    print(clean_line, "---", count,'words')
    line=f.readline()
f.close()
