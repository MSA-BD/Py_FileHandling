'''
write(stringData) and writelines(stringData) method diye amra file
e content write korte pari.
write() and writelines() method duti-i file content overrite kore
dey.sudu matro notun content i file e thake.
write() and writelines() method integer value return kore. Kototi
char and koto line write kora hoyche ta return kore.
write() and writelines() method e cursor pointer 0 index theke
start hoy.
'''
# newFile=open(input('Enter your new filename: '),mode='w')
# try:
#     if newFile:
#         chars=newFile.write(input('Enter file content: '))
#         print(chars)
#     else:
#         print('File does not create')
# finally:
#     newFile.close()

#copying existing file on a new file
# existFile=open('para.txt',mode='r')
# newFile=open(input('Enter new filename: '),mode='w')
# data=existFile.readlines()
# for line in data:
#     writeChars=newFile.write(line)
#     print(f"Write {writeChars} chars in {newFile.name}")

# writelines() method
lines=open('para.txt',mode='r').readlines()
# for line in lines:
#     print(line) //We should stop CNG vehicle permession/n
newFile=open(input('Enter writelines filename: '), mode='w')
totalWriteLine=0
# for line in lines:
#     newFile.writelines(line)
#     totalWriteLine+=1
# print(totalWriteLine)




