
import re, sys
def _syslog(filename, listOfKeywords):

    # Open syslog file and save as 'contents'
    with open(filename) as f:
        # Read file into 'contents'
        contents = f.readlines()

    # List to store the results
    results = []
    # Loopping for each element in syslog
    for line in contents:
        # Loopping for each element in keyword
        for eachKeyword in listOfKeywords:
            # If element 'line' contains element 'keyword'
            # Then print the occurrences
            x = re.findall(r"" + eachKeyword + "", line)
            # print(x)

            for found in x:
                # Append the returned key words to the results list
                results.append(found)

    # Here is check to see if there are results
    if len(results) == 0:
        print("No Results")
        sys.exit(1)
    # Here it sort the list
    results = sorted(results)
    # Remove duplicates (convert to set)
    results = set(results)
    return results