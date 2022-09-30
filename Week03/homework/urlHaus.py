
# Week 3 By Hasan Hashim
# Fixed: On line 3 I added a issing import of `re` with csv
import csv, re

# Fixed: On line 6 I renamed function `ur1HausOpen` to `urlHausOpen` and `searchTerm` to `searchTerms`
def urlHausOpen(filename, searchTerms):
    # Fixewd: On line 8 I replaced `while` with `with` and I removed quotes around `'filename'`
    # On line 9 we are trying to open a file and restored in f
    with open(filename) as f:
        # I fixed the following:
        #       I replaced the following:
        #           `csv.review` with `csv.reader`
        #           `==` with `=`
        #           `filename` with `f`
        #           `f` with `f.readlines()`
        # On line 17 wecreated a csv reader object
        contents = csv.reader(f.readlines())
    # On line 19 I'm trying to skip the first 9 lines
    for skipped_line in range(9):
        # On ilne 21 we going to the next item in the iterator
        next(contents)
    # Fixed: I fixed the loops it were going in the opposite of the right order.
    # line 24 is going through the contents
    for eachLine in contents:
        # line 26 is going over searchTerms
        for keyword in searchTerms:
            # Fixed: I replaced the `r+keyword+` with `r'.*'+keyword+r'.*'`
            x = re.findall(r'.*'+keyword+r'.*', eachLine[2])
            # line 30 is Printing info
            for _ in x:
                # Don't edit this line. It is here to show how it is possible
                # to remove the "tt" so programs don't convert the malicious
                # domains to links that an be accidentally clicked on.
                the_url = eachLine[2].replace("http", "hxxp")
                the_src = eachLine[4]

                # I fixed the following:
                #    replaced `"+60` with `"*60` - becouse we can't add it int to the string
                #    replaced `""",format` with  `""".format`
                # I included formatting place for the info and url
                
                
                print("""
URL: {}
Info: {}
{}""".format(the_url, the_src, "*"*60))