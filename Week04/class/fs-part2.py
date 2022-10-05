# File to traverse a given directory and it's sub directories and retrieve all the files.
import os, argparse, sys

#parser
parser = argparse.ArgumentParser(

    description ="Traverses a directory and builds a forensic body file",
    epilog="Developed by Hasan Hashim, 20220930"
)


# Add argument to fs.py
parser.add_argument(
    "-d",
    "--directory",
    required=True,
    help="Directory that you want to traverse.",
)

# Parse arguments
args = parser.parse_args()

rootdir = args.directory

# In our story, we will traverse a directory
# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print(f"Invalid directory => {rootdir}")
    sys.exit()

# List to save files
f_list = []

# Crawl through the provided directory
for root, _, filenames in os.walk(rootdir):

    for f in filenames:

        f_list.append(root + "/" + f)


def stat_file(to_stat):
    # i is going to be the variable used for each of the metadata elements
    i = os.stat(to_stat, follow_symlinks=False)

    # mode
    mode = i[0]
    # inode
    inode = i[1]
    # uid
    uid = i[4]
    # gid
    gid = i[5]
    # file size
    fsize = i[6]
    # access time
    atime = i[7]
    # modification time
    mtime = i[8]
    # ctime => windows: birth of file, creation time
    #          unix: when attributes of the file change
    ctime = i[9]
    crtime = i[9]

    print(
        "0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(
            to_stat, mode, inode, uid, gid, fsize, atime, mtime, ctime, crtime
        )
    )


for each_file in f_list:
    stat_file(each_file)