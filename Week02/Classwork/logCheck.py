# Here I'm importing sys,re, and yaml to our code
import re, sys, yaml

# From line 5 to line 11 are trying to open the Yaml file
try:
    with open('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)
except EnvironmentError as e:
    print(e.strrerror)
def _syslog(filename, service, term):
    terms = keywords[service][term]
# Here I tried to sprlit the terms
    listOfKeywords = terms.split(",")
    # Here I'm trying to open a file, with open makes python close a file if something goes wrong
    with open(filename) as f:
        # Trying to read what's in the file and it will save in a variable
        contents = f.readlines()
    # Lists
    results = []
    # Here will loop through the list returned. 
    for line in contents:
        # This time we trying to loop through keyword that we have.
        # In side the loop we trying to do the following:
        #   frist we will check if the line contains any of the keyword then it will print
        #   and then if eachKeyword in line
        #   Finally it will returned results using the regular expression
        # In line 31 it will append the returned keywords to the results list
        for eachKeyword in listOfKeywords:
            x = re.findall(r''+eachKeyword+'', line)
            for found in x:
                results.append(found)

    # From line 34 to line 36 we are checking to see if there are results to print out
    if len(results) == 0:
        print("No Results")
        sys.exitt(1)
    results = sorted(results) 
    return results
