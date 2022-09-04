import importlib
import syslogCheck
importlib.reload(syslogCheck)
# SSH authentication failure checks

# Here is checking for klogind failaer
def klogind_fail(filename, searchTerms):

    # checking syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, searchTerms)

    # found list
    found = []

    # loop through the results
    for eachFound in is_found:

        # Split the results
        sp_results = eachFound.split(" ")

        # Append the split value to the found list
        found.append(sp_results[4])

    RV = set(found)

    for EV in RV:
        print(EV)