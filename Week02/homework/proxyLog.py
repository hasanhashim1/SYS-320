import logCheck, importlib
importlib.reload(logCheck)




def events(filename, service, term):
    # Here I added the logCheck to return the results
    is_found = logCheck._syslog(filename, service, term)
    return set(is_found)

def opened(filename, service, term):
    # Here I made a hosts and I called it hs
    hs = events(filename, service, term)
    # Now I made a empty list to work on
    found = []
    # Here I created a max length for our output
    ml = {}
  
# From line 34 to line 46 will get all of the info (tx/rx) and hosts
def bytes(filename, service, term):
    # Here I made a hosts and I called it hs
    hs = events(filename, service, term)
    # Now I made a empty list to work on
    found = []
    # Here I'm getting thelength of the host
    ml = max([len(i[0]) for i in hs])
    # looping through the hosts
    for host in hs:
        # Now we have to append all of the formatted host
        found.append(f"{host[0] : >{ml}} | {host[1]}, {host[2]}")
    for entry in set(found):
        print(entry)


 # Line 43: In this function I tried to find the max length, and I did the following:
 # Line 44: I Calculated the max host
 # Line 46: and then the URL length 
 # Line 47: Looping through in side the hosts
 # Line 48: And then I split the host entry
 # Line 49: Next I appented the split value that I did to the found list to work with
 # Line 50: last but not lease is printing everything
    def gm(idx):
        return max([len(h.split(" ")[idx]) for h in hs])
    ml["host"] = gm(2)
    ml["addr"] = gm(4)
    for entry in set(found):
        print(entry)