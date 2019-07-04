# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:41:38 2019
@author: M.Faisal
"""
# importing librariries
import shutil
import win32api
from pathlib import Path
import platform
import os
# %%
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
# %%
print(platform.platform())
print(platform.system())
print(platform.release())
print(platform.version())
# %%
try:            # Making Folder 
    os.makedirs("/Users/user/Desktop/copy_folder",exist_ok=True)
except Exception:
    pass
# %%
ll_files=[]# all files that matches will be stored in this folder 
Folders=[]  
file_stored=[]
temp=0   
words=['acedmy','admiral','advance','air force','aircraft',
       'aircraft carrier','ally','ammo','ammunation','amphibious vehicle',
       'armistice','armor','armoured vehicle','armory','arms'] # Add words that you want to search and match
for drive in drives:
    for r,d,f in os.walk(drive):
        root=r.replace('\\','/')
        if(root[2:]!="/Users/user/Desktop/copy_folder"):
           file=[s.lower() for s in f]
           for w in file:
               for k in words:
                   if k in w:
                       print("Matched Word is :"+k)
                       data_folder=Path(r)
                       file_to_open=data_folder/str(w)
                       if file_to_open not in file_stored:
                            file_stored.append(file_to_open)
                            temp=temp+1
                            print(temp)
                            print(file_to_open) # printing name of file that has matched word
                            print("Root is :",r)
                            print("subfolder are :",d)
                            try:
                              print("complete path is :",file_to_open)
                              shutil.copy(file_to_open,"/Users/user/Desktop/copy_folder") # second argument is folder name in which files will be saved
                              file_to_open.close()
                            except Exception:
                                   pass
        else:
            pass