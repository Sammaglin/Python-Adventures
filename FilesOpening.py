with open("file1.txt","r+") as myfile:
    # with Open is used to open any file in pyhton
    print(myfile.read())
    #file_name.read is used to read the file txt
    myfile.write("I am Fine")
    # .write is used to write txt in that file
myfile.close()
# it is compulsary to close the file after work