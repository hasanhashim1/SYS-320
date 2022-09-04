import importlib
import syslogCheck
importlib.reload(syslogCheck)

# checkign the FTP connections
def ftp_connection(filename, searchTerms):

    # Checking syslogCheck and it will return the results
    is_found = syslogCheck._syslog(filename, searchTerms)

    # found list
    found = []

    # loop through the results
    for eachFound in is_found:
        # Split the results
        sp_results = eachFound.split(" ")
        # Append the split value to the found list
        found.append(sp_results[3])



    hosts = set(found)
    for eachHost in hosts:
        print(eachHost)