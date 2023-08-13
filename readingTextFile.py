'''
read() method er diye amra kuno file er content/data read korte pari.
read() method text mode e string return kore and binary mode e
bytes return kore.
raed(char) text method e parametre deya zay. binary mode parametre
deya lage na.
read(char) method /n char hisabe gononay dhore.
'''
fileObj=open('names.txt',mode='r')

try:
    if fileObj:
        data1=fileObj.read(20)
        print(data1)
    else:
        print('file does not open')
finally:
    fileObj.close()
    print('file closed')