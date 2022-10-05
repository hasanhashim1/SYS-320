# File to traverse a given directory and it's sub directories and retrieve all the files.
import os, argparse, sys

#parser
parser = argparse.ArgumentParser(

    description ="Traverses a directory and builds a forensic body file",
    epilog="Developed by Hasan Hashim, 20220930"
)

# add an argument to pass
parser.add_argument("-d", "--directory", required=True, help="Directory that you want to traverse")

# parse the arguments
args = parser.parse_args()

rootdir = args.directory

# check if the given argument is a directory

if not os.path.isdir(rootdir):
    print(f"Invalid Directory => {rootdir}")
    exit()
# list to save files
fList = []
# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):

    for f in filenames:
        #windows
        # fileList = rootdir + "\\" + f

        #linux
        fileList = rootdir + "/" + f
        # print(fileList)

        fList.append(fileList)

def statFile(toStat):

    # i is going to be the varible for used for each of the metadata elements
    i = os.stat(toStat, follow_symlinks=False)

    # mode
    mode = i[0]

    # inode
    inode = i[1]

    # uid
    uid = i[4]

    # guid
    guid = i[5]

    # file size
    fsize = i[6]

    # access time
    atime = i[7]

    # modification time
    mtime = i[8]

    # ctime windows is the birth of the file , when it was created
    ctime = i[9]

    crtime = i[9]

    print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(toStat, inode, mode, uid, guid, fsize, atime, mtime, ctime, crtime))

for eachFile in fList:
    statFile(eachFile)