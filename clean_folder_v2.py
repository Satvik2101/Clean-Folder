import os
import shutil

cur_dir= os.getcwd()

def make_folder(name):
    if (os.path.exists('.\\'+name)):
            return
    else:
        os.makedirs('.\\'+name)

if os.path.exists(os.path.join(cur_dir,'clean_folder.txt'))==False:

    txt_file_create=open('clean_folder.txt','w')
txt_file= open('clean_folder.txt','r+')

txt_data= txt_file.read()
txt_file.seek(0)

folders_list = [ x  for x in os.listdir() if os.path.isdir(x)== True and x in txt_data]
print (folders_list)
def unpack(folders):
    for folder in folders:
        files = os.listdir(folder)
        print (files)
        while len(os.listdir(folder)) != 0:
            for file in files:
                if os.path.isdir(file)==False:
                    print (file)
                    try:
                        shutil.move(os.path.join(cur_dir,folder,file),os.path.join(cur_dir,file))
                    except FileExistsError as e:
                        print("The file {} already exists or requires administrator permission to be moved.Please decide what to do manually.Error message: {}".format(os.path.join(cur_dir,file), e))
                        
                else:
                    unpack(file)

    
        if len(os.listdir(folder))==0:
            os.rmdir(folder)
unpack(folders_list)

files= [x for x in os.listdir() if os.path.isdir(x)== False and x != 'clean_folder_v2.py' and x!='clean_folder.txt']
extensions =[os.path.splitext(x)[1] for x in files]
print (extensions)
folders_created=[]
for file in files:
    extension = os.path.splitext(file)[1]
    print (extension)
    
    if extensions.count(str(extension))>1:
        print (extensions.count(str(extension)))

        make_folder(extension)
        
        folders_created.append(extension)
        try:
            shutil.move(os.path.join(cur_dir,file),extension)
        except:
            print("The file {} already exists or requires administrator permission to be moved.Please decide what to do manually.Error message: {}".format(os.path.join(cur_dir,file), e))
    else:
        make_folder("others")
        folders_created.append("others")
        try:
            shutil.move(os.path.join(cur_dir,file),"others")
        except:
            print("The file {} already exists or requires administrator permission to be moved.Please decide what to do manually.Error message: {}".format(os.path.join(cur_dir,file), e))
   
for folder in folders_created:
    txt_file.write(folder+"\n")
    
txt_file.close()



