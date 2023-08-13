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
newFile=open(input('Enter your new filename: '),mode='w')
try:
    if newFile:
        chars=newFile.write(input('Enter file content: '))
        print(chars)
    else:
        print('File does not create')
finally:
    newFile.close()
