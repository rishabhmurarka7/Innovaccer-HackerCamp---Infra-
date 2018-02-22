# ------------------------------------------------------------------#
# Author  : Rishabh Murarka                                         # 
# Roll No.: 20172111                                                # 
#     Submitted as part of Infrastructure Engineering Assignment    # 
# ------------------------------------------------------------------#

import os
import subprocess
import shutil
import sys
import collections
import time


def folderCategorization():
    path = raw_input("Enter the path to the folder for which categorization of files is to be performed: ")
    reorg_dir = path
    exclude = ()
    remove_emptyfolders = True

    for root, dirs, files in os.walk(reorg_dir):
        for name in files:
            subject = root+"/"+name
            if name.startswith("."):
                extension = ".hidden_files"
            elif not "." in name:
                extension = ".without_extension"
            else:
                extension = name[name.rfind("."):]
            if not extension in exclude:
                new_dir = reorg_dir+"/"+extension[1:]
                if not os.path.exists(new_dir):
                    os.mkdir(new_dir)
                shutil.move(subject, new_dir+"/"+name)

    def cleanup():
        filelist = []
        for root, dirs, files in os.walk(reorg_dir):
            for name in files:
                filelist.append(root+"/"+name)
        directories = [item[0] for item in os.walk(reorg_dir)]
        for dr in directories:
            matches = [item for item in filelist if dr in item]
            if len(matches) == 0:
                try:
                    shutil.rmtree(dr)
                except FileNotFoundError:
                    pass

    if remove_emptyfolders == True:
        cleanup()

def largest10Files():

    def val(v):
        return v[1]
    objects=[]

    path = raw_input("Enter the path to the folder for which top 10 files are to be displayed:")
    for root, directories, filenames in os.walk(path):
        for filename in filenames: 
            objects.append(root+ "/" +filename)

    currentsize = 0
    name = ""
    dict={}
    for item in objects:
            size = os.path.getsize(item)
            dict[item] = size

    d = sorted(dict.items(),key=val) 
    d.reverse()

    print 'The top 10 largest files in decreasing order of their sizes are:\n'

    for i in range(0,10):   
        print 'File',i+1,':',d[i][0]
        print 'The size of this file is:',d[i][1],'bytes'
        changed = os.path.getmtime(d[i][0])
        reform = time.ctime(changed)
        print "It was last modified at " + reform
        print '\n'

if __name__ == '__main__':

    print "Press 1 for categorization of files"
    print "Press 2 for finding the top 10 files acc. to their size"

    choice = raw_input("Enter your choice:")

    options = {1 : folderCategorization,
               2 : largest10Files
              } 

    choice = int(choice) 

    if choice == 1 or choice == 2:        
        options[choice]()   
    else:
        print 'Invalid Choice'
