# What is file handling in python?
'''
Files: Files are named location on disk to store information.
Files are used to store data parmanently. Files are saved on
non-volatile memmory. We can retrieve data whenever required.
There aare two types of files :
1. Text Files( text, json. yaml, csv,etc file)
2. Binary Files( Audion, Video, PDF,Image etc files)
What is file handling:
 1. Open the file,
 2.Admit some 0peration on file,
 3. Close the file
'''
fileObj=open('names.txt',mode='r')
if fileObj:
    print('File opend successfully')

