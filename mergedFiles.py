from os import path
existFiles=[]
mergedFilesData=''
def addFilesToMerged():
    while True:
        addFileName = input('Enter file name to merged: ') + '.txt'
        try:
            isExistFile = path.isfile(addFileName)
            print(isExistFile)
            if isExistFile=='True':
                # print(isExistFile)
                existFiles.append(addFileName)
                addMore = input('Do you want to add more file?(y/n): ')
                if addMore != 'y':
                        break
            else:
                raise FileExistsError('File does not exist')
                addMore = input('Do you want to add more file?(y/n):')
                if addMore != 'y':
                    break
                else:
                    continue
        except FileExistsError as error:
            print(f"{addFileName} file does not exist")
            addMore = input('Do you want to add more file?(y/n): ')
            if addMore != 'y':
                break
            else:
                continue
        # finally:
        #     addMore = input('Do you want to add more file?(y/n): ')
        #     if addMore != 'y':
        #         break


addFilesToMerged()
print(existFiles)
