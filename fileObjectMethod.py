'''
File object method are: readable() and writable() both are return
boolean value
'''
fileObject=open('names.txt',mode='w')
if fileObject.mode=='w+':
    print('File are accepted both method')
elif fileObject.mode=='r':
    print('File are only readable')
else:
    print('Fole are only writable')
fileObject.close()