import os
import shutil


cur_dir= os.getcwd()

def make_folder(name): #Checks to see if a folder exists, makes it if it doesn't.
    if (os.path.exists('.\\'+name)):
            return
    else:
        os.makedirs('.\\'+name)

if os.path.exists(os.path.join(cur_dir,'clean_folder.txt'))==False: #creates clean_folder.txt if it doesn't exist

    txt_file_create=open('clean_folder.txt','w')
txt_file= open('clean_folder.txt','r+')

txt_data= txt_file.read() 
txt_file.seek(0)

make_folder('error_files')
if os.path.exists("others"): #takes all files in 'others' folders and copies them to current directory
    files_others= os.listdir('others')
    while len(os.listdir('others')) != 0:
        for file in files_others:
            if os.path.isdir(file)==False:
                print (file)
                try:
                    shutil.move(os.path.join(cur_dir,'others',file),os.path.join(cur_dir,file))
                except OSError:
                    pass
                    shutil.move(os.path.join('others',file),'error_files')
            else:
                unpack(file)

    
    if len(os.listdir('others'))==0:
        os.rmdir('others')


files= [x for x in os.listdir() if os.path.isdir(x)== False and x != 'clean_folder_v3.py' and x!='clean_folder.txt'] #list of files(excluding folders) in current directory, excluding this program and its text file
extensions =[os.path.splitext(x)[1] for x in files] #list of extensions of files
print (extensions)
folders_created=[] #list of folders that will be created
for file in files:
    extension = os.path.splitext(file)[1] #takes extension of file using splitext
    print (extension)
    if os.path.exists(extension): #sees if that particular file already has a dedicated folder from a previous run of clean_folder
        try:
            shutil.move(os.path.join(cur_dir,file),extension) #if yes, it moves it to that folder
        except OSError:
            pass
            shutil.move(os.path.join(cur_dir,file),'error_files')
        files.remove(file)
        extensions.remove(extension)
    else:
        pass
print (extensions)
for file in files:
    extension = os.path.splitext(file)[1]
    if extensions.count(str(extension))>1: #checks to see how many times files of that extension occurs in list 'extensions'
        print ("hello")
        print (extensions.count(str(extension))) #if more than 1, creates a folder for that extension 

        make_folder(extension)
        
        folders_created.append(extension) #appends to list 'folders_created'
        try:
            shutil.move(os.path.join(cur_dir,file),extension) #moves file to folder of that extension
        except OSError:
            pass
            shutil.move(os.path.join(cur_dir,file),'error_files')
    else:
        make_folder("others") # if only 1 file of an extension exists, it is put in others folder
        folders_created.append("others")
        try:
            shutil.move(os.path.join(cur_dir,file),"others")
        except OSError:
            pass
            shutil.move(os.path.join(cur_dir,file),'error_files')

for folder in folders_created:
    txt_file.write(folder+"\n")
    
txt_file.close()

if len(os.listdir('error_files'))== 0 :
    os.rmdir('error_files')

else:
    print ("The following files could not be moved due to an unknown error. Please move them manually from folder \'error_files\'")
    print (os.listdir('error_files'))

os.system('pause')




''' Working:
When the program is run for the first time, it doesn't harm existing folders. Takes stray files and sorts them extension wise
Creates folder for each file type that exists more than once. All the rest are put in 'others' folder

When run the next time, it unpacks 'others' folders, in case a file that has been put there now has another file of same extension.
Same thing is done again. If a file now placed has a folder already dedicated to its extension, it is put there

All the while , it writes the name of the folders created by it in clean_folder.txt . This is so that they can be unpacked
using unpack.py, without harming any other folders.
'''








