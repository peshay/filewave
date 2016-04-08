#! /usr/bin/env python
"""FileWave API Module

To simplify usage of FileWave API. https://www.filewave.com

Authentication:

For Authentication, you need the Shared Key from FileWave.
You can get it from
    FileWave Admin - Preferences - Inventory - Inventory Server - Shared Key
If there is no shared key in this section,
check the Generate new key on Save option and select Ok in the preference dialog.
If there is a shared key, do NOT select to generate a new key on save.

Python2/Python3 compatibility notes:

The module is written to be fully compatible with Python2 and Python3.
If you use the key as binary object like this
    SHARED_SECRET = b"{c4397402-3021-4697-ae01-bf86b94105b1}"
your code will work with Python2 and Python3.
If you use it just as string like this
    SHARED_SECRET = "{c4397402-3021-4697-ae01-bf86b94105b1}"
it will only work with Python2.

Logging:
The module also provides logging for debug messages.
    >>> import logging
set file, level and format for logging.
    >>> logfile = 'MyLogFile.log'
    >>> loglevel = logging.INFO
    >>> logformat = '%(asctime)s - %(levelname)s - %(message)s'
    >>> logging.basicConfig(filename=logfile, level=loglevel, format=logformat)
If you don't want the requests and urllib3 module to log too much
    >>> logging.getLogger("requests").setLevel(logging.WARNING)
    >>> logging.getLogger("urllib3").setLevel(logging.WARNING)

Usage Example:
Import the module and provide all necessary information for an API connection.
    >>> import FileWaveAPI
    >>> SHARED_SECRET = b"{c4397402-3021-4697-ae01-bf86b94105b1}"
    >>> SERVER_NAME = "filewave-server.example.com"
    >>> SERVER_PORT = "20443"
    >>> f = FileWaveAPI.v1(SHARED_SECRET, SERVER_NAME, SERVER_PORT)
Now you can List all queries.
    >>> f.ViewAllQueries()
List just a specific query by ID.
    >>> QueryID = 123
    >>> f.ViewQuery(QueryID)
Get the results of a query by ID.
    >>> QueryID = 123
    >>> f.ViewQueryResult(QueryID)
Do your own query.
    >>> query = {'criteria': {'column': 'filewave_client_name',
    ...                       'component': 'DesktopClient',
    ...                       'operator': 'is',
    ...                       'qualifier': 'me'},
    ...          'fields': [{'column': 'filewave_client_name',
    ...                      'component': 'DesktopClient'}],
    ...          'main_component': 'DesktopClient',
    ...          'name': 'new test query'}
    >>> f.PostNewQuery(query)
    {'name': 'new test query', 'group': 0, 'fields': [{'component': 'DesktopClient', 'column': 'filewave_client_name'}], 'main_component': 'DesktopClient', 'criteria': {'operator': 'is', 'component': 'DesktopClient', 'column': 'filewave_client_name', 'qualifier': 'me'}, 'id': 123, 'favorite': False, 'version': 1}
Delete a query.
    >>> f.RemoveQuery(123)
    {'name': 'new test query', 'group': 0, 'fields': [{'component': 'DesktopClient', 'column': 'filewave_client_name'}], 'main_component': 'DesktopClient', 'criteria': {'operator': 'is', 'component': 'DesktopClient', 'column': 'filewave_client_name', 'qualifier': 'me'}, 'id': 123, 'favorite': False, 'version': 1}

More information about the FileWave Restful API can be found at https://www.filewave.com/item/restful-api

:copyright: (c) 2015 by Andreas Hubert.
:license: The MIT License (MIT), see LICENSE for more details.
"""

__version__ = "0.1"

import base64
import logging
import requests
import json
# to disable warnings about self-signed certs
requests.packages.urllib3.disable_warnings()

# set logger
log = logging.getLogger(__name__)


class api(object):
    """Provide all function compatible for the API."""
    def __init__(self, SHARED_SECRET, SERVER_NAME, SERVER_PORT):
        """Provide action, when object gets created."""
        # Encode SHARED_SECRET with base64
        self.SHARED_SECRET = SHARED_SECRET
        self.SERVER_NAME = SERVER_NAME
        self.SERVER_PORT = SERVER_PORT
        E_STRING = base64.encodestring(SHARED_SECRET)
        if not isinstance(E_STRING, str):
            self.SHARED_SECRET_ENCODED = E_STRING.decode('ascii').rstrip()
        else:
            self.SHARED_SECRET_ENCODED = E_STRING.rstrip()

        log.debug('Set Encoded Authorization Key to {0}'
                  .format(self.SHARED_SECRET_ENCODED))

    def Request(self, URL, action, data):
        """Send a request to the server."""
        REQUEST_URL = "https://{0}:{1}{2}".format(self.SERVER_NAME,
                                                  self.SERVER_PORT, URL)
        log.debug('Set query URL to {0}'.format(REQUEST_URL))
        HEADERS = {'content-type': 'application/json',
                   'Authorization': self.SHARED_SECRET_ENCODED}
        if action == 'get':
            log.debug('Starting GET request.')
            request = requests.get(REQUEST_URL,
                                   headers=HEADERS, verify=False)
        elif action == 'post':
            log.debug('Starting POST request.')
            request = requests.post(REQUEST_URL, data=json.dumps(data),
                                    headers=HEADERS, verify=False)
        elif action == 'delete':
            log.debug('Starting DELETE request.')
            request = requests.delete(REQUEST_URL,
                                      headers=HEADERS, verify=False)
        result = request.json()
        return result

    def GetRequest(self, URL, data={}):
        """Send a GET request to the server."""
        return self.Request(URL, 'get', data)

    def PostRequest(self, URL, data={}):
        """Send a POST request to the server."""
        return self.Request(URL, 'post', data)

    def DeleteRequest(self, URL, data={}):
        """Send a DELETE request to the server."""
        return self.Request(URL, 'delete', data)


class v1(api):
    """API v1 based class."""
    def __init__(self, SHARED_SECRET, SERVER_NAME, SERVER_PORT):
        super(v1, self).__init__(SHARED_SECRET, SERVER_NAME, SERVER_PORT)

    """From now on, Functions that only work with API v1."""
    def ViewAllQueries(self):
        """Viewing all available queries."""
        URL = "/inv/api/v1/query/"
        return self.GetRequest(URL)

    def ViewQuery(self, id):
        """Viewing a specific query."""
        URL = "/inv/api/v1/query/{0}".format(id)
        return self.GetRequest(URL)

    def ViewQueryResult(self, id):
        """Viewing query results."""
        URL = "/inv/api/v1/query_result/{0}".format(id)
        return self.GetRequest(URL)

    def PostNewQuery(self, query):
        """Posting a new query."""
        URL = "/inv/api/v1/query/"
        return self.PostRequest(URL, query)

    def RemoveQuery(self, id):
        """Removing a query."""
        URL = "/inv/api/v1/query/{0}".format(id)
        return self.GetRequest(URL)
