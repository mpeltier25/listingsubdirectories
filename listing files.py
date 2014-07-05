This program will pick a root directory and search through all subfolders until it lists all the files within the root and subdirectories.
import os
def listingfiles():
    """In order to run listing files, simply run the .py program, and pick your directory. For example: /home/name/Desktop/test folder. Once the program is running, it will search whatever directory you choose for the appropriate files with various extensions, such as .txt files and more. it will also keep track of how many types of files it has found. For example, it will keep count of how many text files that it has found within the subdirectories of the root directory you have specified."""
    #Prompt the user for the root directory they wish to search
    directory=input("Enter the directory you wish to search ex. /home/name/Desktop/test folder\n")
    #These counters are going to keep track of how many types of each file there are
    txtcounter=0
    pngcounter=0
    jpegcounter=0
    jpgcounter=0
    doccounter=0
    docxcounter=0
    xlscounter=0
    xlsxcounter=0
    pycounter=0
    blankcounter=0
    sqlcounter=0
    mp3counter=0
    zipcounter=0
    bz2counter=0
    tgzcounter=0
    for currentdir, alldirs, allfiles in os.walk(directory):
        #For the filename in the allfiles in the directory, it will search for all the files and list the appropriate files with the extensions as well as how many of that type of file there are.
        for filename in allfiles:
        #If the file with a certain extension was found, it will print the name of the file as well as the filename and the directory it was located in, and will also print out the counter of how many of that type of file has been found.
            if filename.endswith(".txt"):
               txtcounter=txtcounter+1
               print ("The file with extension .txt", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of text files are:", txtcounter)
            if filename.endswith(".png"):
               pngcounter=pngcounter+1
               print ("The file with extension .png", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of png files are:", pngcounter)
            if filename.endswith(".jpeg"):
               jpegcounter=jpegcounter+1
               print ("The file with extension .jpeg", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of jpeg files are:", jpegcounter)
            if filename.endswith(".jpg"):
               jpgcounter=jpgcounter+1
               print ("The file with extension .jpg", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of jpg files are:", jpgcounter)
            if filename.endswith(".doc"):
               doccounter=doccounter+1
               print ("The file with extension .doc", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of doc files are:", doccounter)
            if filename.endswith(".docx"):
               docxcounter=docxcounter+1
               print ("The file with extension .docx", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of docx files are:", docxcounter)
            if filename.endswith(".xls"):
               xlscounter=xlscounter+1
               print ("The file with extension .xls", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of xls files are:", xlscounter)
            if filename.endswith(".xlsx"):
               xlsxcounter=xlsxcounter+1
               print ("The file with extension .xlsx", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of xlsx files are:", xlsxcounter)
            if filename.endswith(".py"):
               pycounter=pycounter+1
               print ("The file with extension .py", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of py files are:", pycounter)
            if filename.endswith("."):
               blankcounter=blankcounter+1
               print ("The file with no extension", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of no extension files are:", blankcounter)
            if filename.endswith(".sql"):
               sqlcounter=sqlcounter+1
               print ("The file with extension .sql", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of sql files are:", sqlcounter)
            if filename.endswith(".mp3"):
               mp3counter=mp3counter+1
               print ("The file with extension .mp3", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of mp3 files are:", mp3counter)
            if filename.endswith(".zip"):
               zipcounter=zipcounter+1
               print ("The file with extension .zip", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of zip files are:", zipcounter)
            if filename.endswith(".bz2"):
               bz2counter=bz2counter+1
               print ("The file with extension .bz2", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of bz2 files are:", bz2counter)
            if filename.endswith(".tgz"):
               tgzcounter=tgzcounter+1
               print ("The file with extension .tgz", filename, "was found here:\n", (os.path.join(currentdir,filename)), "\nThe number of tgz files are:", tgzcounter)
listingfiles()
