# File to traverse a given directory and it's subdirectories and retrieve all the files.

import os, sys





# Get information from the commandline
#print(sys.argv)

# Directory to traverse
rootdir = sys.argv[1]

#print(rootdir)

# In our story, we will traverse a directory

# Check if the argument is a directory (to test on Mac, possible directory is ~/Applications)
if not os.path.isdir(rootdir):
    print("Invalid Directory => {} ".format(rootdir))
    exit()


# List to save files
fList = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):

    for f in filenames:

        #print(root  + "/" + f)
        fileList = root  + "/" + f
        #print(fileList)
        fList.append(fileList)

#print(fList)

def statFile(toStat):

    # i is going to be the variable used for each of the metadata elements
    i = os.stat(toStat==False) #changed comma to period because comma was making code error

    # mode
    mode = i[0] 
    
    #inode
    inode=i[1]

    # uid
    uid = i[4]

    # gid
    gid = i[5]

    # filesize
    fsize = i[6]

    # access  time
    atime = i[7]

    # modification time
    mtime = i[8]

    # ctime => windows is the birth of the file, when it was created
    # unix it is when attributes of the file changes
    ctime = i[9]
    crtime = i[9]

    print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(toStat, inode, mode, uid, gid, fsize, atime, mtime, ctime, crtime))

for eachFile in fList:
    
    statFile(eachFile)


#Vs code file path: cd ~/Desktop/SYS-320-01/Week4/Classwork