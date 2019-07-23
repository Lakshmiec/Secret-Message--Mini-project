import os
def rena_files():
     file_list= os.listdir(r"C:\Users\3 Kutties\OneDrive\Documents\prank")
     print(file_list)
     print("The current"+os.getcwd())
     os.chdir(r"C:\Users\3 Kutties\OneDrive\Documents\prank")
     for file_name in file_list:
          file_table=str.maketrans("0123456789", "          ","0123456789")
          os.rename(file_name,file_name.translate(file_table))
rena_files()