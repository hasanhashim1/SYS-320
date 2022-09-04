import importlib
import syslogCheck
importlib.reload(syslogCheck)
# SSH authentication failure checks


# SSH authentication failures
def ssh_fail(filename, searchTerms):

    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, searchTerms)

    # found list
    found = []

    # Here it will loop through the results
    for eachFound in is_found:

        # Here we split the results
        sp_results = eachFound.split(" ")

        # Here we should append the split value to the found list
        found.append(sp_results[8])


    hosts = set(found)
    for eachHost in hosts:
        print(eachHost)


        