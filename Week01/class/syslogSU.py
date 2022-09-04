import importlib
import syslogCheck
importlib.reload(syslogCheck)
# SSH authentication failure checks

# User session opening
def su_open(filename, searchTerms):

    # checking syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, searchTerms)

    # found list
    found = []

    # loop through the results
    for eachFound in is_found:

        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list
        found.append(sp_results[5])

    hosts = set(found)

    for eachHost in hosts:
        print(eachHost)