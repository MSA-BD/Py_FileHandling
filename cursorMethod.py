'''
cursor method tell() : cursor er current position return kore.
cursor 0 index theke suru hoy.
seek() method cursor er position change kore
'''
fileObj=open('names.txt',mode='r')
data=fileObj.read(10)
print(data)
cursor=fileObj.tell()
print(cursor)

#seek() method
fileObj.seek(16)
data2=fileObj.read()
print('data2 from start 16 char',data2)
print('file closed')
