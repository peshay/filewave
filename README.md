[![Build Status](https://travis-ci.org/peshay/filewave.svg?branch=testcase)](https://travis-ci.org/peshay/filewave)
[![GitHub release](https://img.shields.io/github/release/peshay/filewave.svg)]()
[![GitHub tag](https://img.shields.io/github/tag/peshay/filewave.svg)]()
[![license](https://img.shields.io/github/license/peshay/filewave.svg)]()

# FileWaveAPI.py

To simplify usage of [FileWave](https://www.filewave.com) API.

Requires: requests

## Install FileWaveAPI.py

You can install the FileWaveAPI module via pip

    pip install FileWaveAPI

## How to Use

### Authentication
For Authentication, you need the Shared Key from FileWave.

You can get it from

    FileWave Admin - Preferences - Inventory - Inventory Server - Shared Key

If there is no shared key in this section, check the Generate new key on Save option and select Ok in the preference dialog.
If there is a shared key, do NOT select to generate a new key on save.

### Python2/Python3 compatibility notes
The module is written to be fully compatible with Python2 and Python3.

If you use the key as binary object like this

    SHARED_SECRET = b"{c4397402-3021-4697-ae01-bf86b94105b1}"
your code will work with Python2 and Python3.

If you use it just as string like this

    SHARED_SECRET = "{c4397402-3021-4697-ae01-bf86b94105b1}"
it will only work with Python2.

### Logging
The module also provides logging for debug messages.
```python
    >>> import logging
```
set file, level and format for logging.
```python
    >>> logfile = 'MyLogFile.log'
    >>> loglevel = logging.INFO
    >>> logformat = '%(asctime)s - %(levelname)s - %(message)s'
    >>> logging.basicConfig(filename=logfile, level=loglevel, format=logformat)
```
If you don't want the requests and urllib3 module to log too much
```python
    >>> logging.getLogger("requests").setLevel(logging.WARNING)
    >>> logging.getLogger("urllib3").setLevel(logging.WARNING)
```
### Usage Examples
Import the module and provide all necessary information for an API connection.
```python
    >>> import FileWaveAPI
    >>> SHARED_SECRET = b"{c4397402-3021-4697-ae01-bf86b94105b1}"
    >>> SERVER_NAME = "filewave-server.example.com"
    >>> SERVER_PORT = "20443"
    >>> f = FileWaveAPI.v1(SHARED_SECRET, SERVER_NAME, SERVER_PORT)
```
Now you can List all queries.
```python
    >>> f.ViewAllQueries()
```
List just a specific query by ID.
```python
    >>> QueryID = 123
    >>> f.ViewQuery(QueryID)
```
Get the results of a query by ID.
```python
    >>> QueryID = 123
    >>> f.ViewQueryResult(QueryID)
```
Do your own query.
```python
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
```
Delete a query.
```python
    >>> f.RemoveQuery(123)
    {'name': 'new test query', 'group': 0, 'fields': [{'component': 'DesktopClient', 'column': 'filewave_client_name'}], 'main_component': 'DesktopClient', 'criteria': {'operator': 'is', 'component': 'DesktopClient', 'column': 'filewave_client_name', 'qualifier': 'me'}, 'id': 123, 'favorite': False, 'version': 1}
```

More information about the FileWave Restful API can be found at https://www.filewave.com/item/restful-api
