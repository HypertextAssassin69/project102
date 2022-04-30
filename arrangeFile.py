import os
import shutil
def arrangeFile():
    directory = input("please enter the path of the folder which you want to clear: ")
    listOfItem = os.listdir(directory)

    print(listOfItem)
    for item in listOfItem:# each file or folder from listOfItem will be used
        print(item)
        noFileType = item.split('.')
        print(noFileType)
        print(len(noFileType))
        if len(noFileType) >1:
            splitext ,e = os.path.splitext(directory+"\\"+item)
            print (splitext+" + "+e)
            print(e.split('.'))
            dot,fileExtension = e.split('.')
            print(fileExtension)
            if os.path.exists(directory+"\\"+fileExtension+" folder") == True:
                shutil.move(directory+"\\"+item,directory+"\\"+fileExtension+" folder")
            else :
                fileForWanderers =os.makedirs(directory+"\\"+fileExtension+" folder")
                shutil.move(directory+"\\"+item,directory+"\\"+fileExtension+" folder")
arrangeFile()  