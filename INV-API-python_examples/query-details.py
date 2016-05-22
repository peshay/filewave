#! /usr/bin/env python
# list the details of a given query
# server details can either be defined in here, or passed as parameters
SHARED_SECRET = b"{c4397402-3021-4697-ae01-bf86b94105b1}"
SERVER_NAME = "demo.filewave.ch"
SERVER_PORT = "20443"

# DO NOT CHANGE ANYTHING BELOW THIS LINE
import sys
import FileWaveAPI
import json


def checkinput(ARGUMENTS):
    if len(ARGUMENTS) == 5:
        SHARED_SECRET = ARGUMENTS[3]
        SERVER_NAME = ARGUMENTS[1]
        SERVER_PORT = ARGUMENTS[2]
        QUERY_ID = ARGUMENTS[4]
        return(SERVER_NAME, SERVER_PORT, SHARED_SECRET, QUERY_ID)

    elif len(ARGUMENTS) == 2:
        QUERY_ID = ARGUMENTS[1]
        return(SERVER_NAME, SERVER_PORT, SHARED_SECRET, QUERY_ID)
    else:
        print ("Usage : python ./querydetails.py "
               "SERVERNAME PORTNUMBER \"SHARED_SECRET\" QUERY_ID or")
        print ("        python ./querydetails.py "
               "QUERY_ID       #if remaining parameters are in the script")
        sys.exit(1)

if len(sys.argv) > 2:
    SERVER_NAME, SERVER_PORT, SHARED_SECRET, QUERY_ID = checkinput(sys.argv)
else:
    try:
        QUERY_ID = sys.argv[1]
    except:
        print ("Usage : python ./querydetails.py "
               "SERVERNAME PORTNUMBER \"SHARED_SECRET\" QUERY_ID or")
        print ("        python ./querydetails.py "
               "QUERY_ID       #if remaining parameters are in the script")
        sys.exit(1)

# get the data from inventory
f = FileWaveAPI.v1(SHARED_SECRET, SERVER_NAME, SERVER_PORT)
print (json.dumps(f.ViewQuery(QUERY_ID), indent=1))
