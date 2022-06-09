""""
  ATTENTION!!!! GOVNOCODE
        INCOMING
                     """
def create_file(fileName, input=""):
    newFile = open(fileName, 'w')
    newFile.write(input)
    print("The file "+fileName+" has added")
    newFile.close()

def read_file(fileName):
    rFile = open(fileName, "r")
    for stringLines in rFile.readlines():
        print(stringLines)
    rFile.close()

def append_file(fileName,input):
    aFile = open(fileName, "a")
    aFile.write("\n"+input)
    print("\n The "+"| "+input+" |" +" has successful added. File now: "+"\n-------------------")
    aFile.close()
    read_file(fileName)

#ya ne umeyu v OOP python po etomu nasral vse v main

#now gonna be ebicheskaya realization cherez while-true

status = True
while(status):
    userMove = input("Cho budem delat? ")
    if(userMove.lower()=="help"):
        print("My programm can: "+"\n 1)Create - creat file, type name and input"+"\n 2)Read - read file, type file name"
              +"\n 3)Append - append file, type file name and text to append")
    elif(userMove.lower()=="zatknis"):
        print("zatikayus")
        status=False
    elif(userMove.lower()=="create"):
        fileName = input("Type file name ")
        textInput = input("Type text input or press enter(empty by default) ")
        create_file(fileName,textInput)
    elif(userMove.lower()=="read"):
        fileName = input("What file do u want to read? ")
        read_file(fileName)
    elif(userMove.lower()=="append"):
        fileName = input("Type the name of file ")
        appendInput = input("Type the line: ")
        append_file(fileName,appendInput)


#govnocode ended


abs = 10

