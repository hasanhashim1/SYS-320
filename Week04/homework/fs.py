import os, argparse, re
import sys
import yaml
# Here we are opening the yaml file to search for the terms
try:
    with open('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)
except EnvironmentError as e:
    print(e.strerror)

#parser
parser = argparse.ArgumentParser(

    description="Traverses directories and builds a forensic body file",
    epilog="Developed by Hasan Hashim 10/05/2022"
)
# Here I'm trying to add an arguments to the fs.py which are -d and -s
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
parser.add_argument("-s", "--search", required="True", help="Specify Search Terms: 'SHELL', 'SQL', 'TRV', 'CMS'")

# Now we have to parse the arguments
args = parser.parse_args()
rootDir = args.directory
searchTerms = keywords[args.search]

# Here we are getting information from cmd to Checke if passed argument is directory or not
if not os.path.isdir(rootDir):
    print("Invalid Directory => {} ".format(rootDir))
    exit()

# Line 33 we trying to define a flist for our outputs
flist = []

# Crawling the specified Directory
for root, subfolders, filenames in os.walk(rootDir):
    for f in filenames:
        fileList = root + "\\" + f
        flist.append(fileList)

def _syslog(filename,service):
    #Query the Ymal for the terms specified inside
    #Service is main, term is sub
    terms = service
    # Here I'm trying to split the etries using a comm to be clear
    listOfKeywords = terms.split(", ")
    # Opening a file 
    with open(filename) as f:
        # read in the file and save the output into a variable
        contents = f.readlines()
    # Now we are listting the results
    results = []

    # line 59 is a forloop to loop through the list and give us  the entries in each line
    for line in contents:
        # Loops through keywords
        for eachKeyword in listOfKeywords:
            # if the line contains the keyword it is printed out
            x = re.findall(r''+eachKeyword+'', line)
            for found in x:
                results.append(found)

    # Now we need to check to see if results are present
    #Sort the results
    results = sorted(results)
    cleanResults = []
    #Print the results to the cli
    for line in results:
        print(line)
    return cleanResults
#call for _syslog
for f in flist:
    _syslog(f, searchTerms)