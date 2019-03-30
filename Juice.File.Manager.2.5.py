import shutil         #Contains functions for operating files
import os         #imports the os

def Read():        #For reading files
    path=input("Enter the location of file to read:")
    file=open(path,"r")
    print(file.read()) 
    input('Press Enter...')  
    file.close() 


def Write():    #For writing or creating files
    path=input("Enter the location of file to write or create:")
    if os.path.isfile(path):
        print('Rebuilding Existing file') #For existing file
    else:
        print('Creating new file') #For new file
    text=input("Enter the text to write:")
    file=open(path,"w")
    file.write(text)

def Add():      # Adding text to a file
    path=input("Enter the file location:")
    text=input("Enter the text to write:")
    file=open(path,"a")
    file.write('\n'+text)


def Delete():          #Deleting a File
    path=input("Enter the location of file to be write or create:")
    if os.path.exists(path):      # checks if the file exists
        print('File Found')     #For existing file
        os.remove(path)          #os.remove(file path) is used to delete
        print('File has been deleted')
    else:
        print('File Does\'nt exist')    #Is no file exist



def Dirlist():      #Listing files in a directory
    path=input("Enter the Directory location to list:")
    sortlist=sorted(os.listdir(path))       #Sorting and listing files
    i=0
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1


def Check():       #Checking file or directory presence
    fp=int(input('Check the presence of \n1.File \n2.Directry \n'))
    if fp==1:
        path=input("Enter the file location:")
        os.path.isfile(path)
        if os.path.isfile(path)==True:
            print('File Found')
        else:
            print('File not Found')
    if fp==2:
        path=input("Enter the Directory location:")
        os.path.isdir(path)
        if os.path.isdir(path)==False:
            print('Directory Found')
        else:
            print('Directory Not Found')



def Move():        #For moving or renameing file
    path1=input('Enter the location of File to move or rename:')
    mr=int(input('1.Rename \n2.Move \n'))
    if mr==1:
        path2=input('Enter the resulting location with resulting file name:')
        shutil.move(path1,path2)
        print('File renamed')
    if mr==2:
        path2=input('Enter the location to move:')
        shutil.move(path1,path2)
        print('File moved')


def Copy():       #For copying
    path1=input('Enter the location of File to copy or rename:')
    path2=input('Enter the location to copy:')
    shutil.copy(path1,path2)
    print('File copied')


def Makedir():            #For creating directory
    path=input("Enter the directory name with location to make \neg. C:\\Hello\\Newdir \nWhere newdir is new directory:")
    os.makedirs(path) 
    print('Directory Created')


def Removedir():             #For removing Directory
    path=input('Enter the location of Directory:')
    treedir=int(input('1.Deleted Directory \n2.Delete Directory Tree \n3.Exit \n'))
    if treedir==1:
        os.rmdir(path)
    if treedir==2:
        shutil.rmtree(path)
        print('Directory Deleted')
    if treedir==3:
        exit()


def Openfile():
    path=input('Enter the location of Program:')
    try:
        os.startfile(path)
    except:
        print('File not found')

def Information():
    print('''

                              Detailed Build Information
Made On:GNU/LINUX
Date Created:30 of september 2017
Thanks To:Python Fans
''')

def Extra():
    print('''                                         Extras

Trusted Websites:GitHub
Gmail/Email:
Team Members:
>Ender_Night_Lord-chromebook (Owner)

Version:2.5
''')
run=1
while(run==1):     #Running the program again
    os.system('cls')        #Used to clear the screen after running again the program
    print('Juice File Manager 2.5')
    dec=int(input('''1.Read a file
2.Write in a File
3.Append text in a File
4.Delete a file
5.List Files in a directory
6.Check file existence
7.Move a file
8.Copy a file
9.Create a Directory
10.Delete A Directory
11.Open a program
12.Exit

Other

13.Build Information
14.Extras

Operation Number:
'''))
    if dec==1:
        Read()
    if dec==2:
        Write()
    if dec==3:
        Add()
    if dec==4:
        Delete()
    if dec==5:
        Dirlist()
    if dec==6:
        Check()
    if dec==7:
        Move()
    if dec==8:
        Copy()
    if dec==9:
        Makedir()
    if dec==10:
        Removedir()
    if dec==11:
        Openfile()
    if dec==12:
        exit()
    if dec==13:
         Information()
    if dec==14:
        Extra()
        
        
    run=int(input("1.Run again \n2.Exit \nChoose the option number: \n"))
    if run==2:
        exit()
