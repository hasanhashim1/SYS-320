import logCheck, importlib
importlib.reload(logCheck)

# Here is the SSH authentication when fails
def apache_events(filename, service, term):
    # Here I added the logCheck to return the results
    is_found = logCheck._syslogs(filename, service, term)
    # Here I'm trying to found list
    found = []
    # We have a loop to go through the results
    for eachFound in is_found:
        # Here I split the results
        sp_results = eachFound.split(" ")
        found.append(sp_results[3] + " " + sp_results[0] + " " + sp_results[1])
    # Here I'm trying to remove duplicates by using set and convert the list to a dictionary
    h = set(found)
    # Lines 23 to 24 are for printing the results
    for eachValue in h:
        print(eachValue)