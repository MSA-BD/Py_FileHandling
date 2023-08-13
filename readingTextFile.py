'''
read() method er diye amra kuno file er content/data read korte pari.
read() method text mode e string return kore and binary mode e
bytes return kore.
raed(char) text method e parametre deya zay. binary mode parametre
deya lage na.
read(char) method /n char hisabe gononay dhore.
'''
fileObj=open('names.txt',mode='r')
for data in fileObj:
    print('print fileobj by loop: ',data,end='')

try:
    if fileObj:
        data1=fileObj.read(20)
        print(data1)
    else:
        print('file does not open')
finally:
    fileObj.close()
    print('file closed')

#readline() method
fileHandler=open('names.txt',mode='r')
data3=fileHandler.readline(3)
print(data3,end='')
data4=fileHandler.readline(2)
print(data4)
# fileHandler.close()

#readlines() method
# readlines() method protiti line er list return kore
datas=fileHandler.readlines()
for data in datas:
    print(data,end='')
fileHandler.close()