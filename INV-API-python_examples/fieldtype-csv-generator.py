#! /usr/bin/env python3
# list all query components
# server details can either be defined in here, or passed as parameters
SHARED_SECRET = "{c4397402-3021-4697-ae01-bf86b94105b1}"
SERVER_NAME = "demo.filewave.ch"
SERVER_PORT = "20443"
CSVFILE = "components.csv"


# DO NOT CHANGE ANYTHING BELOW THIS LINE
import sys
import FileWaveAPI


def checkinput(ARGUMENTS):
    if len(ARGUMENTS) == 5:
        SHARED_SECRET = ARGUMENTS[3]
        SERVER_NAME = ARGUMENTS[1]
        SERVER_PORT = ARGUMENTS[2]
        CSVFILE = ARGUMENTS[4]
        return(SERVER_NAME, SERVER_PORT, SHARED_SECRET, CSVFILE)
    else:
        print ("Usage : python ./fieldtype-csv-generator.py "
               "SERVERNAME PORTNUMBER \"SHARED_SECRET\" CSVFILE")
        sys.exit(1)

if len(sys.argv) > 2:
    SERVER_NAME, SERVER_PORT, SHARED_SECRET, CSVFILE = checkinput(sys.argv)

# get the data from inventory and write to csv
f = FileWaveAPI.v1(SHARED_SECRET, SERVER_NAME, SERVER_PORT)
f.ListComponentsCSV(CSVFILE)
