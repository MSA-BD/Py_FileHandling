from os import path
existFiles=[]
mergedFilesData=''
def addFilesToMerged():
 while True:
    try:
        addFile=input('Enter filename to merged: ')+'.txt'
        if path.isfile(addFile)=='False':
            return 'File does not exist'
        else:
            existFiles.append(addFile)
    except FileExistsError as error:
        return error
    finally:
        addMore=input('Dou want to add more?(y/n)')
        if addMore !='y':
            break
addFilesToMerged()
print(existFiles)
