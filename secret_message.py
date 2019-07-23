import os
def rena_files():
     file_list= os.listdir(r"C:\Users\3 Kutties\OneDrive\Documents\prank")  #returns a list containing the names of the entries in the directory given by path
     print(file_list)
     print("The current working directory"+os.getcwd())             # to get current working directory
     os.chdir(r"C:\Users\3 Kutties\OneDrive\Documents\prank")        #to change the current working directory
     for file_name in file_list:
          file_table=str.maketrans("0123456789", "          ","0123456789")
          os.rename(file_name,file_name.translate(file_table))    # for renaming the files
rena_files()
