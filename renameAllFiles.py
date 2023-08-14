
import os
'''
files rename korar jonno nicer argument proyujon:
1. folder path
2. os.listdir(path)
3. newname and oldname
4. os.rename(oldname,newaname)
'''
#get folder path and repalce it:
folderPath=(input('Enter folder path: ')+'/').replace('\\','/')
print(folderPath)
def changeName():
    i=0
    for filename in os.listdir(folderPath):
        oldName=folderPath+filename
        newName=folderPath+'random'+str(i)+'.png'
        os.rename(oldName,newName)
        i+=1
changeName()

