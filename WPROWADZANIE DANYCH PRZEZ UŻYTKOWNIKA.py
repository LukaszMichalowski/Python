
#filename = input("Enter filename: ")
#print("The file name is:%s"%(filename))

while True:
    
    filesizeStr=input("enter the max file size(MB):")

    if filesizeStr.isdecimal():
        filesizeInt=int(filesizeStr)
        break

        
print("The max size is %d"%(filesizeInt))
print("Size in KB is %d"%(filesizeInt*1024))

