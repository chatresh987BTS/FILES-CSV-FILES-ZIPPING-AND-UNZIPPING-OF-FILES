THIS THE PROGRAM TO HOW TO ZIP AND UNZIP THE FILES.

from zipfile import *
f = ZipFile("files.zip", "w", ZIP_DEFLATED)
f.write("sample1.txt")
f.write("sample2.txt")
f.close()
print("ZIP file created")
from zipfile import *
f = ZipFile("files.zip", 'r', ZIP_STORED)
n = f.namelist()
for n1 in n:
   print("File Name: ", n1)
   print("File data is:")
   f1 = open(n1, 'r')
   print(f1.read())
   print()
