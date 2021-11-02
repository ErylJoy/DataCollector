#Traffic Data Collector
The purpose of this tool is to collect data on a specific road segment every 5 minutes.
The data will be collected and stored in an SQLite3 database called data.db


##Usage
```
Retrieve data from TomTom on a road every 5 minutes

positional arguments:
  segmentId      The ID of the segment of road
  location       The location longitude, lattitude to record data on
  apiKey         A TomTom API key

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Output collected data to terminal
```



##Reference 
- TomTom API documentation 
https://developer.tomtom.com/traffic-api/traffic-api-documentation
- Python docs sqlite3 https://docs.python.org/3/library/sqlite3.html
- https://pythonexamples.org/python-sqlite3-check-if-table-exists/