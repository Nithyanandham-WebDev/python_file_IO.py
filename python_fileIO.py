
# python FileIO

python too support  file handling and allows user to handle files i.e to write and read file, along   with many other file handling options, to create a file.

files or named location on disk to store related information. they are used to store permantely store data in a non-volatile memory.

python files IO used read/write  a server lo, analyzing raw data etc.

Write-back (or Write-behind): Writing is done only to the cache. A modified cache block is written back to the store, just before it is replaced.

Write-around Using the write-around policy, data is written only to the backing store without writing to the cache.So, I/O completion is confirmed as soon as the data is written to the backing store


# file opening and closing in python 

# open(
# file,         -->Mandatory,Actual_File_Path
# mode='r',     -->Weather to Read/Write/Append on Opened File
# buffering=<Any_Integer<1>,  -->When Working Unkownsize/LargeSize File 
# encoding=None,   -->Tells Encoding Standard
# errors=None,   -->Tells how to handle Encoding/Decoding Errors
# newline=None,  -->Only in Text Mode,Controls Newline Characters
# closefd=Flase, -->prevent closing the underlying file object
# opener=None
# ) 
# if you are using all arguments in the order that is specified in open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None), you don't need to write argument name

# This can be done in Two Ways

#1--> Using open()
#         Requires Manual Closing of Opened File

#Basic_Synatx

# File_Object = open(File_Location|Path,Accsess_Mode)
# File_Object.close()

#2--> Using with
#             Automatically Closes When Control Leaves the With Block

#Basic_Synatx

# with open(File_Location|Path,Accsess_Mode) as File_Object:
#     File Operations


# Files access modes in python


s.no         character                   function

   1             r                        open a file for reading only.starts reading from begining of file the default mode.


   2             rb                       open a file for reading in binary format. start reading from begining of file 

   3             r+                       open a file for reading and writing.file pointer placed at begining of the file 

   4             w                        open a file  for writing  only file  pointer placed at begining of  the file.otherwise existing file nad creates a new one if it does not existing

   5            wb                        same as w but opens in binary mode.

   6            w+                        same as w but also allows to read from file  


   7            wb+                       same as w+ but also allows to read from file

   8            a                         open a file for appending. starts writing  at end of file. create a new file if file does not existing


   9            ab                        same as a but in binary format. create  a new file if file does not exit.

   10           a+                        same a a but also open for reading.

   11           ab+                       same a ab but also open for reading.


<!-- # File Reading Methods -->

# read(Size = Value)   -->return str,If Size Specified Reads that no of bytes,else reads Entire File
# readline(Size)     -->return str,Reads number of characters from the line.
# readlines()   -->return List,Reads Entire File as List Separated by New Linew Character


# read(Size)

with open("Python_FileIO_Practice.txt",'r') as File_Read:
    
     #Reads First 30 Characters From First Line
     #if Size not Specified it Rads Entire File .
    print("File Read Using With and Read():",File_Read.read(30))

        
File_Object_Read_Open = open("Python_FileIO_Practice.txt",'r')
print(File_Object_Read_Open.read())  # Reads Entire File No Size Specified



# readline(Size)

#Reads Single Line At Time.If Size Specified Reads That much Characters from Fetched Line.


with open("Python_FileIO_Practice.txt",'r') as File_Read:
    File_Method_ReadLine_With = File_Read.readline(30) #Reads First 30 Characters From First Line
    #if Size not Specified it Rads Entire File .
    print("File Read Using With and Readline():",File_Method_ReadLine_With)

        
File_Object_ReadLine_Open = open("Python_FileIO_Practice.txt",'r')
print("File Read Using Open and Readline():",File_Object_ReadLine_Open.readline())  # Reads Entire File No Size Specified

# when readline() method is called it fetches the first line if it called again it fetches the second line and so on.

# Read first 10 Lines Using Readline()

for x in range(10):
    print(x+1,File_Object_ReadLine_Open.readline())
       
# Above Piece of Code calls readline() for 10 times so each time it fetches next line.

File_Object_ReadLine_Open.close()



# readlines()   -->Reads Entire File and returns them as a list.
# Here it Checks for \n Character in the File if Encountered It Appends the text before \n character to the output list.


with open("Python_FileIO_Practice.txt",'r') as File_Read:
    File_Method_ReadLines_With = File_Read.readlines() #Reads Entire File and Emits a list

    print("File Read Using With and Readlines():",File_Method_ReadLines_With)

        
File_Object_ReadLines_Open = open("Python_FileIO_Practice.txt",'r')
print("File Read Using Open and Readlines():",File_Object_ReadLines_Open.readlines())

# Iterating/Reading the Output List

for Read_Output in File_Object_ReadLines_Open.readlines():
    print("Readlines:",Read_Output,end='')

File_Object_ReadLines_Open.close()


# <!-- # File Writing Methods -->

# write(String)   -->This writes the string to the file.

# writelines(List)     -->This writes the sequence to the file. No line endings are appended to each sequence item. It’s up to you to add the appropriate line ending(s)


# write method

File_Write_Sample_Data = ["Schmitt","King","Ferguson","Labrune","bergulfsen","Nelson","Piestrzeniewicz",
"Keitel","Murphy","Lee","Freyre","Berglund","Petersen","Saveley","Natividad","Young","Leong","Hashimoto","Victorino","Oeztan",
"Franco","de Castro","Rancé","Bertrand","Tseng","King","Kentary","Frick","Karttunen","Ashworth","Cassidy","Taylor","Devon","Tamuri",
"Barajas","Young","Walker","Citeaux","Gao","Saavedra","Young","Kloss","Ibsen","Fresnière","Camino","Thompson","Bennett","Roulet","Messner"
"Accorti","Da Silv","Tonini","Pfalzheim","Lincoln","Franken","OHara","Rovelli","Huxley","Hernandez","Harrison","Holz","Klaeboe","Schuyler","Anderse","Koskitalo","Dewey"
"Frick","Huang","Brown","Graham","Brown","Brown","Calaghan","Suominen","Cramer","Cervantes","Fernandez","Chandler","McKenna",
"Lebihan","Henriot","Kuger","MacKinlay","Josephs","Yoshido","Young","Rodriguez","Urs","Nelson","Cartrain","Pipps","Cruz","Moroni"
"Shimamura","Perrier","Müller","McRoy","Donnermeyer","Hernandez","Feuer","Lewis","Larsson","Frick","Mendel","Murphy""Choi"]


# Create New File With Name:File_Write.txt

with open("File_Write.txt","a") as F_Write:
    for Write_Content in File_Write_Sample_Data:
        Temp_Text = Write_Content + '--'   # Here '--' is added to serve as a Separator
        F_Write.write(Temp_Text)

# Read the Created File To Check Weather Contents Written or !

with open("File_Write.txt","r") as F_read:
    print(F_read.read())



# writelines method

File_WriteLines_Sample_Data = ["Schmitt","King","Ferguson","Labrune","bergulfsen","Nelson","Piestrzeniewicz",
"Keitel","Murphy","Lee","Freyre","Berglund","Petersen","Saveley","Natividad","Young","Leong","Hashimoto","Victorino","Oeztan",
"Franco","de Castro","Rancé","Bertrand","Tseng","King","Kentary","Frick","Karttunen","Ashworth","Cassidy","Taylor","Devon","Tamuri",
"Barajas","Young","Walker","Citeaux","Gao","Saavedra","Young","Kloss","Ibsen","Fresnière","Camino","Thompson","Bennett","Roulet","Messner"
"Accorti","Da Silv","Tonini","Pfalzheim","Lincoln","Franken","OHara","Rovelli","Huxley","Hernandez","Harrison","Holz","Klaeboe","Schuyler","Anderse","Koskitalo","Dewey"
"Frick","Huang","Brown","Graham","Brown","Brown","Calaghan","Suominen","Cramer","Cervantes","Fernandez","Chandler","McKenna",
"Lebihan","Henriot","Kuger","MacKinlay","Josephs","Yoshido","Young","Rodriguez","Urs","Nelson","Cartrain","Pipps","Cruz","Moroni"
"Shimamura","Perrier","Müller","McRoy","Donnermeyer","Hernandez","Feuer","Lewis","Larsson","Frick","Mendel","Murphy""Choi"]


# Create New File With Name:File_Write.txt

with open("File_WriteLines.txt","a+") as F_Write:
    F_Write.writelines("\n".join(File_WriteLines_Sample_Data))

# Read the Created File To Check Weather Contents Written or !

with open("File_WriteLines.txt","r") as F_read:
    print(F_read.read())


File IO method 

 File_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'r')


File_IO_Functions_Practice.tell()     #-->Tells the Cursor Position

File_IO_Functions_Practice.readline(4)     

File_IO_Functions_Practice.tell()     #-->Tells the Cursor Position



File_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'r')


File_IO_Functions_Practice.seek(10)     #-->Places the Cursor To The Position Specified.

# File_IO_Functions_Practice.readline(4)     

File_IO_Functions_Practice.tell()     #-->Tells the Cursor Position


File_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'r')


File_IO_Functions_Practice.seekable()     #-->Returns True/False;True If File Supports Seeking.



readableFile_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'r')


File_IO_Functions_Practice.readable()     #-->Returns True/False;True If File Supports Reading.

File_IO_Functions_Practice_1 = open("Python_FileIO_Practice.txt",'w')


File_IO_Functions_Practice_1.readable()     #-->Returns True/False;True If File Supports Reading



File_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'r')


File_IO_Functions_Practice.fileno()     #--> Retuens a integer assigned to a file object by the operating system



File_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'r')


File_IO_Functions_Practice.flush()     #--> Clears Buffer and Writes Data to file.
In [ ]:
File_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'r')


File_IO_Functions_Practice.mode     #--> Returns mode of the File Which is Opened.i.e r,w,a.,
In [ ]:
File_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'r')


File_IO_Functions_Practice.name    #--> Returns Name of the File
In [ ]:
File_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'w')


File_IO_Functions_Practice.truncate()    #--> Empties Contents in a File.Raises Error if File mode in r.
In [ ]:
File_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'w')


File_IO_Functions_Practice.writable()    #--> Returns True/False;True If File Supports Writing.
In [ ]:
File_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'w')


File_IO_Functions_Practice.close()    #--> Closes the File.
In [ ]:
File_IO_Functions_Practice = open("Python_FileIO_Practice.txt",'w')

File_IO_Functions_Practice.closed    #--> Returns True/False;Checks Weather File Closed or not