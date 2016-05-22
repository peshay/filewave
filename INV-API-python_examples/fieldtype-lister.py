#! /usr/bin/env python3
# returns available components ( data fields ) as JSON

SHARED_SECRET = "e2M0Mzk3NDAyLTMwMjEtNDY5Ny1hZTAxLWJmODZiOTQxMDViMX0="
SERVER_NAME = "demo.filewave.ch"
SERVER_PORT = "20443"

# DO NOT CHANGE ANYTHING BELOW THIS LINE

# libraries
import FileWaveAPI
import json

# get the data from inventory
f = FileWaveAPI.v1(SHARED_SECRET, SERVER_NAME, SERVER_PORT)
print (json.dumps(f.ListComponents, indent=4))
