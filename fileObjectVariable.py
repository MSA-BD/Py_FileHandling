'''
FileObjectVariable are : name, mode, encoding, closed
'''
fileObject=open('names.txt',mode='r',encoding='utf-8',buffering=10)
if fileObject:
    print('fileObject are available')
else:
    print('File could not open')
fileName=fileObject.name
print(fileName)
fileMode=fileObject.mode
print(fileMode)
fileEncodingType=fileObject.encoding
print(fileEncodingType)
fileObject.close()
isClosed=fileObject.closed
print(isClosed)