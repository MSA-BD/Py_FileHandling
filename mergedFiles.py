from os import path
# existFiles=[]
# mergedFilesData=''
# def addFilesToMerged():
#     while True:
#         addFileName = input('Enter file name to merged: ') + '.txt'
#         try:
#             isExistFile = path.isfile(addFileName)
#             print(isExistFile)
#             if isExistFile=='True':
#                 # print(isExistFile)
#                 existFiles.append(addFileName)
#                 addMore = input('Do you want to add more file?(y/n): ')
#                 if addMore != 'y':
#                         break
#             else:
#                 raise FileExistsError('File does not exist')
#                 addMore = input('Do you want to add more file?(y/n):')
#                 if addMore != 'y':
#                     break
#                 else:
#                     continue
#         except FileExistsError as error:
#             print(f"{addFileName} file does not exist")
#             addMore = input('Do you want to add more file?(y/n): ')
#             if addMore != 'y':
#                 break
#             else:
#                 continue
#         # finally:
#         #     addMore = input('Do you want to add more file?(y/n): ')
#         #     if addMore != 'y':
#         #         break

existFiles=[]
def  addFilesToMerged():
   while True:
       addFileName=input('Enter filename to merged: ')+'.txt'
       isExistFile=path.isfile(addFileName)
       if isExistFile:
           existFiles.append(addFileName)
           addMore=input('Do you want to add more?(y/n): ')
           if addMore!='y':
             break
       else:
           # ekahne error rasise korte hobe
           print('Last typed file does not exist!')
           addMore = input('Do you want to add more?(y/n): ')
           if addMore != 'y':
               break
           else:
               continue


def readDataByLoop(files):
    mergedFilesData=''
    for file in files:
        fileObj=open(file,mode='r',encoding='utf-8')
        data=fileObj.read()+'/n'
        mergedFilesData=mergedFilesData+data
        fileObj.close()
    return mergedFilesData

def writeAllDataInAFile(mergedFilesData):
    fileObj=open(input('Enter team file name: ')+'.txt',mode='x',
                 encoding='utf-8')
    totalWrite=fileObj.write(mergedFilesData)
    print(f"Total write {totalWrite} charechter in {fileObj.name} "
          f"file")
    fileObj.close()

addFilesToMerged()
allData=readDataByLoop(existFiles)
writeAllDataInAFile(allData)
print(existFiles)
