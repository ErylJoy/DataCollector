# Traffic Data Collector
The purpose of this tool is to collect data on a road segments every 5 minutes.
The data will be collected and stored in an SQLite3 database called data.db


## Usage
The `segements.csv` file contains id, co-ordinate pairs of locations to be tested, the co-ordinates are in the form `longitude,latitude`.


```
usage: main.py [-h] [-v] csvFile apiKey

Retrieve data from TomTom on a road every 5 minutes

positional arguments:
  csvFile        The file to load segments data from
  apiKey         A TomTom API key

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Output collected data to terminal
```



## Reference 
- TomTom API documentation 
https://developer.tomtom.com/traffic-api/traffic-api-documentation
- Python docs sqlite3 https://docs.python.org/3/library/sqlite3.html
- https://pythonexamples.org/python-sqlite3-check-if-table-exists/