import os
import shutil
import sys

if os.path.exists('clean_folder.txt') == False:
    print ("clean_folder.txt file has not been created or has been deleted.")
    sys.exit()

else:
    txt_file= open('clean_folder.txt','r+')
    txt_data = txt_file.read()
    

cur_dir= os.getcwd()
folders_list=[ x for x in os.listdir() if os.path.isdir(x) == True and x in txt_data]

for folder in folders_list:
    files = os.listdir(folder)
    print (files)
    while len(os.listdir(folder)) != 0:
        for file in files:
            if os.path.isdir(file)==False:
                print (file)
                try:
                    shutil.move(os.path.join(cur_dir,folder,file),os.path.join(cur_dir,file))
                except OSError:
                    pass                        
            else:
                unpack(file)

    
    if len(os.listdir(folder))==0:
        os.rmdir(folder)


    
